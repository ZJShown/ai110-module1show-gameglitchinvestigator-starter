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
| Enter a guess that is too low or too high | The hint should correctly say "Higher" when the guess is too low and "Lower" when the guess is too high. | The hint does not work properly and does not correctly show "Lower" or "Higher". | No console error noticed. |
| Click the "New Game" button, then enter a number and guess again | The button should fully reset the game, including the target number, attempts, score/message state, and guessing behavior. | The button only resets the attempts. After entering a number and trying to guess, the game does not respond properly. | No console error noticed. |
| Change the game difficulty | The game should adjust the number range to match the selected difficulty. | Changing the difficulty does not properly update the number range. | No console error noticed. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
