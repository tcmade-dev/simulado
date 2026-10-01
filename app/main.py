"""
FastAPI Backend with HTMX & Jinja2 Templates
Simulado - Introdução ao Santo Ministério
Multi-chapter selection, real-time question tracking, and validation.
"""

import os
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import (
    get_all_chapters,
    get_attempts,
    get_grouped_questions_for_chapters,
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


@app.get("/capitulo/{chapter_number}")
async def redirect_chapter(chapter_number: int):
    return RedirectResponse(url=f"/simulado?capitulos={chapter_number}")


@app.get("/simulado", response_class=HTMLResponse)
async def view_simulado(request: Request, capitulos: Optional[str] = "1"):
    try:
        chapter_nums = [int(c.strip()) for c in (capitulos or "1").split(",") if c.strip().isdigit()]
    except Exception:
        chapter_nums = [1]

    if not chapter_nums:
        chapter_nums = [1]

    all_chapters = get_all_chapters()
    active_chapter_map = {c["number"]: c for c in all_chapters if c["is_active"]}

    valid_nums = [n for n in chapter_nums if n in active_chapter_map]
    if not valid_nums:
        raise HTTPException(
            status_code=400,
            detail="Nenhum dos capítulos selecionados está disponível para simulado no momento.",
        )

    grouped_data = get_grouped_questions_for_chapters(valid_nums)
    if not grouped_data:
        raise HTTPException(status_code=404, detail="Nenhuma questão encontrada para os capítulos selecionados.")

    # Compute total questions and subitems count for tracking
    total_question_units = 0
    for group in grouped_data:
        total_question_units += len(group["questions"])

    selected_chapters_str = ",".join(str(n) for n in valid_nums)
    
    if len(valid_nums) == 1:
        simulado_title = f"Capítulo {valid_nums[0]} - {active_chapter_map[valid_nums[0]]['title']}"
    else:
        simulado_title = f"Simulado dos Capítulos {', '.join(str(n) for n in valid_nums)}"

    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "grouped_data": grouped_data,
            "selected_chapters_str": selected_chapters_str,
            "simulado_title": simulado_title,
            "valid_nums": valid_nums,
            "total_questions": total_question_units,
        },
    )


@app.post("/simulado/validar", response_class=HTMLResponse)
async def validate_simulado(request: Request):
    form_data = await request.form()
    capitulos_raw = form_data.get("selected_chapters", "1")
    try:
        chapter_nums = [int(c.strip()) for c in capitulos_raw.split(",") if c.strip().isdigit()]
    except Exception:
        chapter_nums = [1]

    grouped_data = get_grouped_questions_for_chapters(chapter_nums)
    if not grouped_data:
        raise HTTPException(status_code=400, detail="Nenhuma questão encontrada para validar.")

    all_evaluations_grouped = []
    attempt_details = {}
    overall_correct_count = 0
    overall_total_questions = 0

    for group in grouped_data:
        ch = group["chapter"]
        questions = group["questions"]
        ch_evaluations = []
        ch_correct_count = 0

        for q in questions:
            q_num = q["question_number"]
            q_type = q["question_type"]
            q_prompt = q["prompt"]
            q_options = q["options"]
            q_correct = q["correct_answer"]
            q_explanation = q.get("explanation", "")
            q_sub_explanations = q.get("sub_explanations", {})
            field_prefix = f"c{ch['number']}_q{q_num}"

            if q_type == "multiple_choice":
                user_ans = form_data.get(field_prefix, "").strip().lower()
                correct_ans = str(q_correct).strip().lower()
                is_correct = (user_ans == correct_ans)
                if is_correct:
                    ch_correct_count += 1
                    overall_correct_count += 1

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
                ch_evaluations.append(eval_item)
                attempt_details[field_prefix] = {
                    "chapter": ch["number"],
                    "question": q_num,
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
                    input_name = f"{field_prefix}_{opt_key}"
                    user_val = form_data.get(input_name, "").strip().upper()
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
                    ch_correct_count += 1
                    overall_correct_count += 1

                eval_item = {
                    "question_number": q_num,
                    "question_type": q_type,
                    "prompt": q_prompt,
                    "sub_items": sub_items,
                    "is_correct": all_sub_correct,
                    "explanation": q_explanation,
                }
                ch_evaluations.append(eval_item)
                attempt_details[field_prefix] = {
                    "chapter": ch["number"],
                    "question": q_num,
                    "user_answers": user_sub_answers,
                    "correct_answers": q_correct,
                    "is_correct": all_sub_correct,
                }

            elif q_type == "matching":
                sub_items = []
                all_sub_correct = True
                user_sub_answers = {}
                col2_items = q_options.get("column_2", [])

                for item in col2_items:
                    item_id = str(item["id"])
                    input_name = f"{field_prefix}_{item_id}"
                    user_val = form_data.get(input_name, "").strip().lower()
                    expected_val = str(q_correct.get(item_id, "")).strip().lower()
                    item_correct = (user_val == expected_val and bool(user_val))
                    if not item_correct:
                        all_sub_correct = False

                    user_sub_answers[item_id] = user_val
                    sub_items.append({
                        "id": item_id,
                        "text": item["text"],
                        "user_answer": user_val.upper() if user_val else "",
                        "correct_answer": expected_val.upper(),
                        "is_correct": item_correct,
                        "explanation": q_sub_explanations.get(item_id, "") or q_sub_explanations.get(expected_val, ""),
                    })

                if all_sub_correct:
                    ch_correct_count += 1
                    overall_correct_count += 1

                eval_item = {
                    "question_number": q_num,
                    "question_type": q_type,
                    "prompt": q_prompt,
                    "column_1": q_options.get("column_1", []),
                    "sub_items": sub_items,
                    "is_correct": all_sub_correct,
                    "explanation": q_explanation,
                }
                ch_evaluations.append(eval_item)
                attempt_details[field_prefix] = {
                    "chapter": ch["number"],
                    "question": q_num,
                    "user_answers": user_sub_answers,
                    "correct_answers": q_correct,
                    "is_correct": all_sub_correct,
                }

        ch_total = len(questions)
        overall_total_questions += ch_total
        all_evaluations_grouped.append({
            "chapter": ch,
            "evaluations": ch_evaluations,
            "correct_count": ch_correct_count,
            "total_questions": ch_total,
            "score_pct": round((ch_correct_count / ch_total * 100), 1) if ch_total > 0 else 0,
        })

    overall_score_pct = (overall_correct_count / overall_total_questions * 100) if overall_total_questions > 0 else 0.0

    if len(chapter_nums) == 1:
        chapter_label = f"Capítulo {chapter_nums[0]}"
        primary_ch_num = chapter_nums[0]
    else:
        chapter_label = f"Simulado Capítulos ({', '.join(str(n) for n in chapter_nums)})"
        primary_ch_num = 0

    save_attempt(
        chapter_number=primary_ch_num,
        chapter_label=chapter_label,
        total_questions=overall_total_questions,
        correct_count=overall_correct_count,
        score_percentage=overall_score_pct,
        details=attempt_details,
    )

    context = {
        "grouped_evaluations": all_evaluations_grouped,
        "overall_total_questions": overall_total_questions,
        "overall_correct_count": overall_correct_count,
        "overall_score_pct": round(overall_score_pct, 1),
        "chapter_label": chapter_label,
        "selected_chapters_str": capitulos_raw,
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
