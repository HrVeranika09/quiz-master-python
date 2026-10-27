class EmptyQuizError(Exception):
    """Raised when there are no questions in the quiz."""
    pass


class InvalidAnswerError(Exception):
    """Raised when user provides an invalid answer format."""
    pass


class QuestionNotFoundError(Exception):
    """Raised when a question cannot be found or loaded."""
    pass
