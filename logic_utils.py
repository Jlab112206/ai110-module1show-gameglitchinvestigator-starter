def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 100  # FIX: was returning 1, 50 — Hard should use the same 1–100 range
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):  # FIX: added low/high params for range validation
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIX: added range check — previously any integer was accepted without validation
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome.

    outcome: "Win", "Too High", or "Too Low"

    Note: returns only the outcome string (not a tuple) so that
    tests and callers can compare it directly without unpacking.
    """
    if guess == secret:
        return "Win"  # FIX: was returning ("Win", "🎉 Correct!") — message is UI concern, not logic

    try:
        if guess > secret:
            return "Too High"  # FIX: was returning a tuple; now returns plain string to match tests
        else:
            return "Too Low"
    except TypeError:
        # secret arrived as a non-int type (e.g. a string) — convert it back for numeric comparison
        # FIX: was casting guess to str and using lexicographic comparison ("9" > "10" is True but numerically wrong)
        try:
            s = int(secret)  # convert string secret back to int so comparison is numeric, not alphabetic
        except (ValueError, TypeError):
            return "Too Low"  # FIX: safe fallback if secret can't be converted — avoids crash
        if guess > s:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
