"""
Database Layer for Simulado
SQLite storage for questions, chapters, and user attempt history.
"""

import json
import os
import sqlite3
from datetime import datetime
from typing import Any, Dict, List, Optional

DB_PATH = os.environ.get("DATABASE_PATH", os.path.join(os.path.dirname(__file__), "..", "data", "simulado.db"))


def get_db():
    os.makedirs(os.path.dirname(os.path.abspath(DB_PATH)), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Chapters metadata
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY,
        number INTEGER UNIQUE NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        is_active BOOLEAN DEFAULT 0
    )
    """)

    # Questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_number INTEGER NOT NULL,
        question_number INTEGER NOT NULL,
        question_type TEXT NOT NULL, -- 'multiple_choice' or 'true_false'
        prompt TEXT NOT NULL,
        options_json TEXT NOT NULL, -- JSON list/dict of options or items
        correct_answer_json TEXT NOT NULL, -- JSON target correct answer(s)
        explanation TEXT,
        sub_explanations_json TEXT, -- JSON dict of option-specific explanations
        FOREIGN KEY (chapter_number) REFERENCES chapters(number)
    )
    """)

    # History of attempts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT DEFAULT 'Estudante',
        chapter_number INTEGER NOT NULL,
        chapter_label TEXT DEFAULT '',
        total_questions INTEGER NOT NULL,
        correct_count INTEGER NOT NULL,
        score_percentage REAL NOT NULL,
        details_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    # Check if chapter_label exists in existing table
    columns = [col[1] for col in cursor.execute("PRAGMA table_info(attempts)").fetchall()]
    if "chapter_label" not in columns:
        cursor.execute("ALTER TABLE attempts ADD COLUMN chapter_label TEXT DEFAULT ''")

    conn.commit()
    conn.close()


def save_chapter(number: int, title: str, description: str = "", is_active: bool = False):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO chapters (number, title, description, is_active)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(number) DO UPDATE SET
        title=excluded.title,
        description=excluded.description,
        is_active=excluded.is_active
    """, (number, title, description, int(is_active)))
    conn.commit()
    conn.close()


def save_question(
    chapter_number: int,
    question_number: int,
    question_type: str,
    prompt: str,
    options: Any,
    correct_answer: Any,
    explanation: str = "",
    sub_explanations: Optional[Dict[str, str]] = None,
):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM questions
    WHERE chapter_number = ? AND question_number = ?
    """, (chapter_number, question_number))

    cursor.execute("""
    INSERT INTO questions (
        chapter_number,
        question_number,
        question_type,
        prompt,
        options_json,
        correct_answer_json,
        explanation,
        sub_explanations_json
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        chapter_number,
        question_number,
        question_type,
        prompt,
        json.dumps(options, ensure_ascii=False),
        json.dumps(correct_answer, ensure_ascii=False),
        explanation,
        json.dumps(sub_explanations or {}, ensure_ascii=False),
    ))
    conn.commit()
    conn.close()


def get_all_chapters() -> List[Dict[str, Any]]:
    conn = get_db()
    cursor = conn.cursor()
    rows = cursor.execute("""
    SELECT c.*,
           (SELECT COUNT(*) FROM questions q WHERE q.chapter_number = c.number) as question_count,
           (SELECT MAX(score_percentage) FROM attempts a WHERE a.chapter_number = c.number) as best_score,
           (SELECT COUNT(*) FROM attempts a WHERE a.chapter_number = c.number) as attempts_count
    FROM chapters c
    ORDER BY c.number ASC
    """).fetchall()
    chapters = [dict(row) for row in rows]
    conn.close()
    return chapters


def get_questions_for_chapter(chapter_number: int) -> List[Dict[str, Any]]:
    conn = get_db()
    cursor = conn.cursor()
    rows = cursor.execute("""
    SELECT * FROM questions
    WHERE chapter_number = ?
    ORDER BY question_number ASC
    """, (chapter_number,)).fetchall()

    questions = []
    for r in rows:
        q = dict(r)
        q["options"] = json.loads(q["options_json"])
        q["correct_answer"] = json.loads(q["correct_answer_json"])
        q["sub_explanations"] = json.loads(q["sub_explanations_json"] or "{}")
        questions.append(q)
    conn.close()
    return questions


def get_grouped_questions_for_chapters(chapter_numbers: List[int]) -> List[Dict[str, Any]]:
    """
    Fetches questions grouped by chapter for multi-chapter simulations.
    Returns: [{'chapter': {...}, 'questions': [...]}, ...]
    """
    if not chapter_numbers:
        return []
    conn = get_db()
    cursor = conn.cursor()
    placeholders = ",".join("?" for _ in chapter_numbers)
    ch_rows = cursor.execute(f"""
        SELECT * FROM chapters WHERE number IN ({placeholders}) ORDER BY number ASC
    """, chapter_numbers).fetchall()

    result = []
    for ch_row in ch_rows:
        ch = dict(ch_row)
        q_rows = cursor.execute("""
            SELECT * FROM questions WHERE chapter_number = ? ORDER BY question_number ASC
        """, (ch["number"],)).fetchall()
        questions = []
        for r in q_rows:
            q = dict(r)
            q["options"] = json.loads(q["options_json"])
            q["correct_answer"] = json.loads(q["correct_answer_json"])
            q["sub_explanations"] = json.loads(q["sub_explanations_json"] or "{}")
            questions.append(q)
        if questions:
            result.append({
                "chapter": ch,
                "questions": questions,
            })
    conn.close()
    return result


def save_attempt(
    chapter_number: int,
    total_questions: int,
    correct_count: int,
    score_percentage: float,
    details: Dict[str, Any],
    chapter_label: str = "",
    user_name: str = "Estudante",
) -> int:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO attempts (
        user_name,
        chapter_number,
        chapter_label,
        total_questions,
        correct_count,
        score_percentage,
        details_json,
        created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_name,
        chapter_number,
        chapter_label,
        total_questions,
        correct_count,
        round(score_percentage, 1),
        json.dumps(details, ensure_ascii=False),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    ))
    attempt_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return attempt_id


def get_attempts(chapter_number: Optional[int] = None, limit: int = 20) -> List[Dict[str, Any]]:
    conn = get_db()
    cursor = conn.cursor()
    if chapter_number is not None:
        rows = cursor.execute("""
        SELECT a.*, COALESCE(NULLIF(a.chapter_label, ''), c.title, 'Capítulo ' || a.chapter_number) as display_title
        FROM attempts a
        LEFT JOIN chapters c ON a.chapter_number = c.number
        WHERE a.chapter_number = ?
        ORDER BY a.created_at DESC
        LIMIT ?
        """, (chapter_number, limit)).fetchall()
    else:
        rows = cursor.execute("""
        SELECT a.*, COALESCE(NULLIF(a.chapter_label, ''), c.title, 'Capítulo ' || a.chapter_number) as display_title
        FROM attempts a
        LEFT JOIN chapters c ON a.chapter_number = c.number
        ORDER BY a.created_at DESC
        LIMIT ?
        """, (limit,)).fetchall()

    attempts = []
    for r in rows:
        item = dict(r)
        item["chapter_title"] = item.get("display_title") or (f"Capítulo {item['chapter_number']}" if item['chapter_number'] > 0 else "Simulado Multi-Capítulo")
        item["details"] = json.loads(item["details_json"])
        attempts.append(item)
    conn.close()
    return attempts


def get_stats() -> Dict[str, Any]:
    conn = get_db()
    cursor = conn.cursor()
    total_attempts = cursor.execute("SELECT COUNT(*) FROM attempts").fetchone()[0]
    avg_score = cursor.execute("SELECT AVG(score_percentage) FROM attempts").fetchone()[0] or 0.0
    active_chapters = cursor.execute("SELECT COUNT(*) FROM chapters WHERE is_active = 1").fetchone()[0]
    conn.close()
    return {
        "total_attempts": total_attempts,
        "avg_score": round(avg_score, 1),
        "active_chapters": active_chapters,
    }
