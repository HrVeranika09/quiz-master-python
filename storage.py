import json
import os
from question import Question

QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.json"


class QuestionNotFoundError(Exception):
    pass


def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        raise QuestionNotFoundError(f"Plik z pytaniami '{QUESTIONS_FILE}' nie istnieje.")

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data:
        raise QuestionNotFoundError("Plik z pytaniami jest pusty.")

    return [Question.from_dict(q) for q in data]


def save_questions(questions):
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump([q.to_dict() for q in questions], f, ensure_ascii=False, indent=2)


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_result(result):
    results = load_results()
    results.append(result)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
