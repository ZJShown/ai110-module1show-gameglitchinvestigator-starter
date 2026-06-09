# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Use all guesses until the game is out of attempts | The game should show that there are 0 attempts left, and the top comment should match the out-of-attempts warning and score. | The out-of-attempts warning appears with the score, but the top comment still says there is 1 attempt left. | No console error noticed. |
| Enter a higher guess than secret | The hint should correctly "Lower" when the guess is too high. The reverse also doesn't work | The hint does not work properly and does not correctly show "Lower" or "Higher". | No console error noticed. |
| Click the "New Game" button, then enter a number and guess again | The button should fully reset the game, including the target number, attempts, score/message state, and guessing behavior. | The button only resets the attempts. After entering a number and trying to guess, the game does not respond properly. | No console error noticed. |
| Change the game difficulty | The game should adjust the number range to match the selected difficulty. | Changing the difficulty does not properly update the number range. | No console error noticed. |

---

## 2. How did you use AI as a teammate?

I used ChatGPT/Codex as an AI teammate to help inspect the game logic, explain the Streamlit state behavior, and suggest small fixes. One correct suggestion was to move the difficulty range logic into `logic_utils.py` and then import `get_range_for_difficulty()` in `app.py` so the app used the same range everywhere. This was correct because I verified that Easy returned `1-20`, Normal returned `1-100`, and Hard returned `1-500`, and the app's displayed range changed with the selected difficulty.

One misleading part of the original AI-generated code was the guess hint logic. The code returned a "Go HIGHER" style message when the guess was already too high, and "Go LOWER" when the guess was too low, which was backwards. I verified that it was wrong by comparing a test guess to the debug secret number in the game and by checking the `check_guess()` logic directly. After fixing it in `logic_utils.py`, I verified that a guess above the secret returns `"Too High"` with `"Lower"` and a guess below the secret returns `"Too Low"` with `"Higher"`.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed only when the code behavior matched what I expected in the game and the focused tests passed. For the hint bug, I checked `check_guess(60, 50)`, `check_guess(40, 50)`, and `check_guess(50, 50)` to make sure the outcome and message were correct. For the difficulty and New Game fixes, I verified that changing difficulty resets the secret number into the new range, and that New Game resets attempts, score, status, history, and the input box.

I also ran `python -m py_compile app.py logic_utils.py` to make sure the files had no syntax errors. Then I ran `python -m pytest tests`, and the result was `3 passed`, which showed that the guess-checking logic worked for winning, too-high, and too-low guesses. AI helped me understand what each test should prove: not just that a function runs, but that the returned outcome and player-facing message match the real game behavior.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

It automatically runs the updated code in the background so you don't have do.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy I would use in the future is probably fix one function at the time so I don't get everything mixed up. One thing I would do differently maybe is I would ask AI to explain the actions after it has done all the changes.