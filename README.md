# Quiz Master – Interactive Assessment & Quiz Engine

A modular console-based quiz engine developed in Python. The system provides an interactive CLI interface for taking randomized assessments, persisting quiz results, dynamically managing question banks, and rendering category-based performance analytics.

## Key Features & Architecture
* **Advanced Python Features:** Leverages custom decorators (`functools.wraps`) for timestamped action logging, Python generators (`yield`) for stateful question streaming, and regex-based input validation.
* **Object-Oriented Design:** Implements domain models with `@classmethod` factories for JSON deserialization, custom serialization methods, and string formatting representations.
* **Robust Error Handling:** Employs a custom exception hierarchy (`EmptyQuizError`, `InvalidAnswerError`, `QuestionNotFoundError`) to safely manage runtime edge cases and corrupted file states.
* **Data Persistence:** Lightweight flat-file database architecture using JSON to track historical quiz attempts, timestamps, score percentages, and category distribution.

## Project Structure
* `main.py` – Application entry point, interactive menu loops, and user workflow orchestration.
* `quiz.py` – Core game loop engine, question randomization, scoring calculations, and statistical aggregations.
* `question.py` – Domain entity modeling question attributes, options, and serialization logic.
* `storage.py` – I/O handling, transactional file read/write operations for questions and score history.
* `decorators.py` – Reusable logging decorators.
* `exceptions.py` – Custom exception definitions.
* `questions.json` – Default question repository across various academic domains.

## Getting Started

### Prerequisites
* Python 3.10+

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/hrveranika/quiz-master-python.git](https://github.com/hrveranika/quiz-master-python.git)
