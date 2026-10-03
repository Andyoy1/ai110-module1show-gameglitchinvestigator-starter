import pytest

from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


@pytest.mark.parametrize("guess, secret", [(60, 50), (100, 9)])
def test_guess_too_high(guess, secret):
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too High"
    assert "Go LOWER" in message
    assert "Go HIGHER" not in message


@pytest.mark.parametrize("guess, secret", [(40, 50), (9, 100)])
def test_guess_too_low(guess, secret):
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too Low"
    assert "Go HIGHER" in message
    assert "Go LOWER" not in message


@pytest.mark.parametrize("raw", [None, "", "   ", "\t"])
def test_parse_guess_blank(raw):
    assert parse_guess(raw) == (False, None, "Enter a guess.")


@pytest.mark.parametrize("raw", ["hello", "12abc"])
def test_parse_guess_nonnumeric(raw):
    assert parse_guess(raw) == (False, None, "That is not a number.")


@pytest.mark.parametrize("raw", ["12.5", "12.0", ".5"])
def test_parse_guess_decimal(raw):
    assert parse_guess(raw) == (False, None, "That is not a number.")


@pytest.mark.parametrize("raw, expected", [("1", 1), ("100", 100), (" 42 ", 42)])
def test_parse_guess_integer(raw, expected):
    assert parse_guess(raw) == (True, expected, None)
