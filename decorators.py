import functools
import datetime


def log_action(func):
    """Decorator that logs when a function is called, with timestamp."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[LOG {timestamp}] Wywołano: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
