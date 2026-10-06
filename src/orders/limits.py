from .config import MAX_LINES


def check_lines(lines):
    if not lines:
        raise ValueError("An order needs at least one line.")
    if len(lines) > MAX_LINES:
        raise ValueError(f"An order can have at most {MAX_LINES} lines.")
