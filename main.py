import re
import sys
from decorators import log_action
from quiz import Quiz, EmptyQuizError, get_category_stats, sort_results_by_score
from storage import load_questions, save_questions, load_results, save_result, QuestionNotFoundError
from question import Question

SEPARATOR = "=" * 50


def print_header():
    print(f"\n{SEPARATOR}")
    print("           🎯 QUIZ MASTER 🎯")
    print(SEPARATOR)


def print_menu():
    print("\nCo chcesz zrobić?")
    print("  1. Rozpocznij quiz")
    print("  2. Dodaj nowe pytanie")
    print("  3. Historia wyników")
    print("  4. Statystyki pytań")
    print("  0. Wyjście")


def get_menu_choice():
    raw = input("\nWybierz opcję: ").strip()
    if not re.fullmatch(r"[0-4]", raw):
        print("  ⚠ Wpisz liczbę od 0 do 4.")
        return ""
    return raw


@log_action
def start_quiz():
    try:
        questions = load_questions()
    except QuestionNotFoundError as e:
        print(f"\n  ⚠ {e}")
        return

    try:
        quiz = Quiz(questions)
        result = quiz.run()
    except EmptyQuizError as e:
        print(f"\n  ⚠ {e}")
        return

    print(f"\n{SEPARATOR}")
    print("              WYNIK QUIZU")
    print(SEPARATOR)
    print(f"  Poprawne odpowiedzi: {result['score']} / {result['total']}")
    print(f"  Wynik procentowy:    {result['percentage']}%")
    print(f"  Status:              {'✓ Zaliczono' if result['passed'] else '✗ Nie zaliczono'}")
    print(SEPARATOR)

    save_result(result)
    print("  Wynik zapisany do historii.")


@log_action
def add_question():
    print(f"\n{SEPARATOR}")
    print("         DODAJ NOWE PYTANIE")
    print(SEPARATOR)

    text = input("Treść pytania: ").strip()
    if not text:
        print("  ⚠ Treść pytania nie może być pusta.")
        return

    category = input("Kategoria (np. Historia, Nauka): ").strip() or "Ogólne"

    options = []
    print("Wpisz 4 opcje odpowiedzi:")
    for i in range(1, 5):
        while True:
            opt = input(f"  Opcja {i}: ").strip()
            if opt:
                options.append(opt)
                break
            print("  ⚠ Opcja nie może być pusta.")

    while True:
        raw = input("Numer poprawnej odpowiedzi (1–4): ").strip()
        if re.fullmatch(r"[1-4]", raw):
            correct_index = int(raw) - 1
            break
        print("  ⚠ Wpisz liczbę od 1 do 4.")

    new_question = Question(text, options, correct_index, category)

    try:
        questions = load_questions()
    except QuestionNotFoundError:
        questions = []

    questions.append(new_question)
    save_questions(questions)
    print(f"\n  ✓ Pytanie dodane! Łącznie pytań: {len(questions)}")


@log_action
def show_history():
    results = load_results()

    print(f"\n{SEPARATOR}")
    print("           HISTORIA WYNIKÓW")
    print(SEPARATOR)

    if not results:
        print("  Brak zapisanych wyników.")
        return

    sorted_results = sort_results_by_score(results)

    for i, r in enumerate(sorted_results, start=1):
        status = "✓" if r["passed"] else "✗"
        print(f"  {i}. [{r['date']}]  {r['score']}/{r['total']}  ({r['percentage']}%)  {status}")

    percentages = [r["percentage"] for r in results]
    avg = round(sum(percentages) / len(percentages), 1)
    best = max(percentages)
    print(f"\n  Średni wynik:  {avg}%")
    print(f"  Najlepszy:     {best}%")


@log_action
def show_stats():
    try:
        questions = load_questions()
    except QuestionNotFoundError as e:
        print(f"\n  ⚠ {e}")
        return

    stats = get_category_stats(questions)

    print(f"\n{SEPARATOR}")
    print("         STATYSTYKI PYTAŃ")
    print(SEPARATOR)
    print(f"  Łączna liczba pytań: {len(questions)}\n")

    for category, count in sorted(stats.items()):
        bar = "█" * count
        print(f"  {category:<15} {bar} ({count})")


def main():
    print_header()

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            add_question()
        elif choice == "3":
            show_history()
        elif choice == "4":
            show_stats()
        elif choice == "0":
            print("\n  Do widzenia! 👋\n")
            sys.exit(0)


if __name__ == "__main__":
    main()
