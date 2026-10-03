# Reflection: Game Glitch Investigator

## 1. What was broken when you started?

**What did the game look like the first time you ran it?**

The game looked like a simple web app for guessing a number. Its Developer Debug Info section made it easier to inspect the secret and game state. I manually confirmed the original bugs while playing.

**List at least two concrete bugs you noticed at the start, and their causes.**

The hints were backwards because guesses above the secret prompted going higher, and guesses below it prompted going lower; the starter also inconsistently compared integers and strings. Normal showed seven attempts because attempts were initialized to one instead of zero. Invalid input consumed an attempt because the counter increased before validation, and rejected input was added to history. New Game stayed blocked after winning or losing because it did not reset status to `"playing"`.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Launch the game on Normal difficulty | Eight attempts remain before any guesses | Only seven attempts remain | UI displays “Attempts left: 7” |
| Submit `abc` | Display an error without consuming an attempt | The attempt counter increases despite invalid input | UI displays “That is not a number.” |
| Submit a valid guess above the secret shown in Developer Debug Info | Classify the guess as too high and advise going lower | The hint incorrectly advises going higher | UI displays “Go HIGHER!” |
| Win or lose, then click New Game | Start a playable fresh round | The game remains blocked because status is not reset | UI still says “You already won” or “Game over” |

---

## 2. How did you use AI as a teammate?

**Which AI tools did you use on this project?**

I used ChatGPT for guidance and Codex in VS Code for repairs and tests. Codex moved `check_guess` and `parse_guess` into `logic_utils.py`. I manually confirmed the original bugs and checked the repaired hints in the running game.

**Give one example of a correct AI suggestion and how you verified it.**

A correct suggestion was to reverse the hints and compare integers consistently. A guess above the secret should say to go lower, while a guess below it should say to go higher. I verified both directions in the running game, and the automated hint tests also passed.

**Give one example of a suggestion you did not accept as written, why, and how you verified your version.**

I did not accept ChatGPT's initial broad replacement-package approach as written. I chose to fork first and make staged repairs to follow the assignment and preserve commit history. I verified the staged repairs with automated tests and manually checked the corrected higher/lower hints.

---

## 3. Debugging and testing your fixes

**How did you decide whether a bug was really fixed?**

I used automated tests alongside my observations in the running game. I manually confirmed the original bugs and then verified that the higher/lower hints worked after the repair. I also fixed the original New Game reset bug by resetting status, attempts, history, score, and the secret's range, although the existing tests do not cover that UI flow.

**Describe at least one test you ran and what it showed.**

The targeted logic tests passed, and the latest full suite run with `.venv` Python passed all 17 cases; its actual output is in README.md. Those cases check winning guesses, both hint directions, and blank, nonnumeric, decimal, and valid integer parsing. After refactoring, the running app still raised `NotImplementedError`, even though the targeted tests had passed. Restarting Streamlit resolved the error, showing why passing logic tests alone did not establish that the running app was working.

**Did AI help you design or understand any tests? How?**

Codex added focused parsing tests and ran pytest using the project's `.venv` Python. It preserved the existing `check_guess` tests for wins and higher/lower hints. These checks verify the extracted logic, while my manual verification established that the repaired hints worked in the running game.

---

## 4. What did you learn about Streamlit and state?

**How would you explain reruns and session state to a friend?**

Streamlit reruns the app script when someone interacts with a widget. Session state holds values such as the secret, attempts, history, score, and status between those reruns. Starting a new round requires explicitly resetting those values, including status so the game becomes playable again.

---

## 5. Looking ahead: your developer habits

**What is one habit or strategy you want to reuse?**

In this project, I made staged repairs and combined automated tests with manual checks. That process is really useful for documentation purposes.

**What would you do differently next time you work with AI?**

Think a lot about the specific choices I do. I chose staged repairs instead of accepting the initial broad replacement as written. The Streamlit error also showed that passing targeted tests did not guarantee that the running app was working.

**How did the project change the way you think about AI-generated code?**

The starter contained errors in hints, attempt counting, validation, and resetting a round. AI helped repair the code, but I still manually confirmed bugs and checked the corrected hints. AI is very useful, but you still need to know what you're doing.
