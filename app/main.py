"""
FastAPI Backend with HTMX & Jinja2 Templates
Simulado - Introdução ao Santo Ministério
"""

import os
from contextlib import asynccontextmanager
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import (
    get_all_chapters,
    get_attempts,
    get_questions_for_chapter,
    get_stats,
    init_db,
    save_attempt,
)
from app.seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure database exists and seed if empty
    init_db()
    chapters = get_all_chapters()
    if not chapters or not get_questions_for_chapter(1):
        seed()
    yield


app = FastAPI(title="Simulado Santo Ministério", lifespan=lifespan)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

os.makedirs(STATIC_DIR, exist_ok=True)
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    chapters = get_all_chapters()
    stats = get_stats()
    recent_attempts = get_attempts(limit=5)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "chapters": chapters,
            "stats": stats,
            "recent_attempts": recent_attempts,
        },
    )


@app.get("/capitulo/{chapter_number}", response_class=HTMLResponse)
async def view_quiz(chapter_number: int, request: Request):
    chapters = get_all_chapters()
    chapter = next((c for c in chapters if c["number"] == chapter_number), None)
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")

    if not chapter["is_active"]:
        raise HTTPException(
            status_code=400,
            detail="Este capítulo está em fase de extração e estará disponível em breve.",
        )

    questions = get_questions_for_chapter(chapter_number)
    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "chapter": chapter,
            "questions": questions,
        },
    )


@app.post("/capitulo/{chapter_number}/validar", response_class=HTMLResponse)
async def validate_quiz(chapter_number: int, request: Request):
    form_data = await request.form()
    chapters = get_all_chapters()
    chapter = next((c for c in chapters if c["number"] == chapter_number), None)
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")

    questions = get_questions_for_chapter(chapter_number)
    if not questions:
        raise HTTPException(status_code=400, detail="Nenhuma questão cadastrada para este capítulo.")

    evaluation: List[Dict[str, Any]] = []
    attempt_details: Dict[str, Any] = {}
    correct_questions_count = 0

    for q in questions:
        q_num = q["question_number"]
        q_type = q["question_type"]
        q_prompt = q["prompt"]
        q_options = q["options"]
        q_correct = q["correct_answer"]
        q_explanation = q.get("explanation", "")
        q_sub_explanations = q.get("sub_explanations", {})

        if q_type == "multiple_choice":
            user_ans = form_data.get(f"q_{q_num}", "").strip().lower()
            correct_ans = str(q_correct).strip().lower()
            is_correct = (user_ans == correct_ans)
            if is_correct:
                correct_questions_count += 1

            eval_item = {
                "question_number": q_num,
                "question_type": q_type,
                "prompt": q_prompt,
                "options": q_options,
                "user_answer": user_ans,
                "correct_answer": correct_ans,
                "is_correct": is_correct,
                "explanation": q_explanation,
            }
            evaluation.append(eval_item)
            attempt_details[f"q_{q_num}"] = {
                "user_answer": user_ans,
                "correct_answer": correct_ans,
                "is_correct": is_correct,
            }

        elif q_type == "true_false":
            sub_items = []
            all_sub_correct = True
            user_sub_answers = {}

            for opt in q_options:
                opt_key = opt["key"]
                user_val = form_data.get(f"q_{q_num}_{opt_key}", "").strip().upper()
                expected_val = str(q_correct.get(opt_key, "")).strip().upper()
                item_correct = (user_val == expected_val)
                if not item_correct:
                    all_sub_correct = False

                user_sub_answers[opt_key] = user_val
                sub_items.append({
                    "key": opt_key,
                    "statement": opt["statement"],
                    "user_answer": user_val,
                    "correct_answer": expected_val,
                    "is_correct": item_correct,
                    "explanation": q_sub_explanations.get(opt_key, ""),
                })

            if all_sub_correct:
                correct_questions_count += 1

            eval_item = {
                "question_number": q_num,
                "question_type": q_type,
                "prompt": q_prompt,
                "sub_items": sub_items,
                "is_correct": all_sub_correct,
                "explanation": q_explanation,
            }
            evaluation.append(eval_item)
            attempt_details[f"q_{q_num}"] = {
                "user_answers": user_sub_answers,
                "correct_answers": q_correct,
                "is_correct": all_sub_correct,
            }

    total_questions = len(questions)
    score_percentage = (correct_questions_count / total_questions * 100) if total_questions > 0 else 0.0

    # Save to SQLite database
    save_attempt(
        chapter_number=chapter_number,
        total_questions=total_questions,
        correct_count=correct_questions_count,
        score_percentage=score_percentage,
        details=attempt_details,
    )

    context = {
        "chapter": chapter,
        "evaluation": evaluation,
        "total_questions": total_questions,
        "correct_count": correct_questions_count,
        "score_percentage": round(score_percentage, 1),
    }

    return templates.TemplateResponse(
        request=request,
        name="quiz_result.html",
        context=context,
    )


@app.get("/historico", response_class=HTMLResponse)
async def history_view(request: Request):
    attempts = get_attempts(limit=50)
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "attempts": attempts,
        },
    )
