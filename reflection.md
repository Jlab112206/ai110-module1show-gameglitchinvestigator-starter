# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran cit?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- The game seemed fine when a i first ran it, nothing out of the ordinary. However, when I put in my inputs, the final guess was -25 instead of the final number being between 1 and 100. After my guesses/attempts ran out, I tried to restart the game and it wouldnt restart or do anything.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used claude ai to assist me on this project. The ome suggestion claude gave me was to fix the bug on line 10, the 'Hard' call returned a range 1, 50 which was wrong so claude suggested that I changed it to 1, 100. The AI didn't give any incorrect suggestions, everything that was suggested ran smoothly and fixed every issue.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- To determine whether or not a bug was fixed, I loaded up the game and played it for myself, every fix that was suggested to me I tested them to see if claude really did the right edits or not. A test I ran was the 'pytest' in the claude ai chat. AI did somewhat help me, but since claude is so advanced, im still lost on how to do run certain test and functions.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- I want to reuse claude AI, it helped me within identifying the bugs but also answering all the questions I had. One thing i'd do differently is not rush through my assignments and take notes as I work through each step. Honestly it hasn't changed my mind about AI generated code, but it does have me thinking about my profession. If accesing the correct code or debuggers is this easy/accessable with ai, then a lot of jobs will be replaced with AI.