import datetime
import random
import re
from question import Question
from decorators import log_action


class EmptyQuizError(Exception):
    pass


class InvalidAnswerError(Exception):
    pass


class Quiz:

    def __init__(self, questions, shuffle=True):
        if not questions:
            raise EmptyQuizError("Brak pytań do quizu. Dodaj pytania przed rozpoczęciem.")
        self.questions = questions
        if shuffle:
            random.shuffle(self.questions)
        self.score = 0
        self.total = len(self.questions)
        self.answers = []

    def question_generator(self):
        for question in self.questions:
            yield question

    @log_action
    def run(self):
        print("\n" + "=" * 50)
        print("       ROZPOCZYNAMY QUIZ!")
        print("=" * 50)

        for i, question in enumerate(self.question_generator(), start=1):
            correct = self._ask_question(i, question)
            self.answers.append(correct)
            if correct:
                self.score += 1

        return self._build_result()

    def _ask_question(self, number, question):
        print(f"\nPytanie {number}/{self.total}  [{question.category}]")
        print(f"  {question.text}")
        print()

        for idx, option in enumerate(question.options, start=1):
            print(f"  {idx}. {option}")

        while True:
            try:
                raw = input("\nTwoja odpowiedź (numer): ").strip()
                answer_index = _parse_answer(raw, len(question.options))
                break
            except InvalidAnswerError as e:
                print(f"  ⚠ {e}")

        if question.is_correct(answer_index):
            print("  ✓ Poprawnie!")
            return True
        else:
            print(f"  ✗ Błędna odpowiedź. Poprawna: {question.correct_answer()}")
            return False

    def _build_result(self):
        percentage = round((self.score / self.total) * 100, 1)
        return {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": self.score,
            "total": self.total,
            "percentage": percentage,
            "passed": percentage >= 50,
        }


def _parse_answer(raw, max_options):
    if not re.fullmatch(r"\d+", raw):
        raise InvalidAnswerError(f"Wpisz cyfrę od 1 do {max_options}.")
    value = int(raw)
    if not (1 <= value <= max_options):
        raise InvalidAnswerError(f"Numer musi być między 1 a {max_options}.")
    return value - 1


def get_category_stats(questions):
    categories = {q.category for q in questions}
    return {cat: sum(1 for q in questions if q.category == cat) for cat in categories}


sort_results_by_score = lambda results: sorted(results, key=lambda r: r["percentage"], reverse=True)
