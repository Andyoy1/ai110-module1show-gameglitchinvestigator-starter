# Game Glitch Investigator: The Impossible Guesser

A Streamlit number guessing game where players use higher/lower hints to find a secret number before attempts run out. This assignment repairs bugs in the AI-generated starter and tests the extracted game logic.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `.venv\Scripts\python.exe -m streamlit run app.py`

## Document Your Experience

- **Backwards hints and inconsistent comparisons:** `check_guess` now compares integers and tells players to go lower for a high guess and higher for a low guess.
- **Missing starting attempt:** attempts started at one; initializing to zero gives Normal all eight attempts.
- **Invalid guesses consumed attempts:** parsing and range validation now happen before updating attempts or history. Blank, nonnumeric, decimal, and out-of-range input is rejected; valid guesses consume one attempt.
- **New Game remained blocked:** the reset now sets status to `"playing"`, attempts and score to zero, history to an empty list, and the secret to a random integer within the selected difficulty range.
- **Refactoring and verification:** Codex moved `check_guess` and `parse_guess` into `logic_utils.py` and added focused tests. I manually confirmed the original bugs and verified the repaired hints in the running game. After refactoring, the app raised `NotImplementedError` despite passing targeted tests; restarting Streamlit resolved it.

## Demo Walkthrough

Follow these steps to demonstrate the repaired behavior; they are instructions, not a record of additional manual checks.

1. Launch on Normal with Show hint enabled and open Developer Debug Info to read the secret. Begin with eight attempts; if the secret is 1 or 100, click New Game to get a round suitable for both hint examples.
2. Submit blank input, `abc`, `12.5`, and `101`. Each should display an error without changing attempts or history.
3. Submit a valid integer above the secret. The hint should say **Go LOWER!**, and the guess should consume one attempt.
4. Submit a valid integer below the secret. The hint should say **Go HIGHER!**, and the guess should consume one attempt.
5. Submit the secret itself to win and see the winning message.
6. Click New Game. Confirm status is `playing`, attempts and score are zero, history is empty, and the secret is within the selected difficulty range; guessing should be available again.

## Test Results

Full suite command: `.venv\Scripts\python.exe -m pytest -q`

```text
.................                                                        [100%]
17 passed in 0.17s
```

The 17 cases cover winning guesses, both hint directions, and blank, nonnumeric, decimal, and valid integer parsing. They do not exercise the complete Streamlit interface or New Game reset.
