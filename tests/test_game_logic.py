from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_check_guess_with_string_secret():
    # app.py casts secret to str on even-numbered attempts, so check_guess receives
    # a string secret instead of an int. The TypeError branch falls back to string
    # comparison — "9" > "10" is True lexicographically, so without correct handling
    # check_guess(9, "10") wrongly returns "Too High" instead of "Too Low".
    result = check_guess(9, "10")
    assert result == "Too Low", (
        "String comparison '9' > '10' is True lexicographically but 9 < 10 numerically — "
        "the TypeError fallback must compare numerically, not as strings."
    )
