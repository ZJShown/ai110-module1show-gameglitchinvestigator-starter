# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game is a Streamlit number guessing game where the player chooses a difficulty, guesses the secret number, and uses hints to move higher or lower.
- [x] I found several bugs: the hints were backwards, the difficulty range did not update correctly, the attempts-left message was off by one, and the New Game button did not fully reset the game state.
- [x] I fixed the app by moving difficulty and guess-checking logic into `logic_utils.py`, using the selected difficulty range when creating a secret number, correcting the higher/lower hint messages, starting attempts at 0, updating the attempts-left display after guesses, and making New Game reset the secret, attempts, score, status, history, and input box.

## Demo Walkthrough

1. User selects Normal difficulty, and the game shows the range as 1 to 100 with 8 attempts allowed.
2. User enters a guess of 40 when the secret number is 50.
3. Game returns "Higher" because the guess is too low, records the guess in history, and decreases the attempts left by 1.
4. User enters a guess of 70.
5. Game returns "Lower" because the guess is too high, updates the score, and decreases the attempts left again.
6. User enters a guess of 50.
7. Game returns "Correct!", shows the winning message with the final score, and changes the game status to won.
8. User clicks New Game, and the app resets the secret number, score, attempts, status, history, and input box for a fresh round.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
