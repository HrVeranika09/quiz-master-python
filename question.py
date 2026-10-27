class Question:

    def __init__(self, text, options, correct_index, category="Ogólne"):
        self.text = text
        self.options = options
        self.correct_index = correct_index
        self.category = category

    def is_correct(self, answer_index):
        return answer_index == self.correct_index

    def correct_answer(self):
        return self.options[self.correct_index]

    def to_dict(self):
        return {
            "text": self.text,
            "options": self.options,
            "correct_index": self.correct_index,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            text=data["text"],
            options=data["options"],
            correct_index=data["correct_index"],
            category=data.get("category", "Ogólne"),
        )

    def __str__(self):
        return f"[{self.category}] {self.text}"
