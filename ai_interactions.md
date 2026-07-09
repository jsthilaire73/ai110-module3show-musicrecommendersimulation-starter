# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I requested the expansion of a standard content-based recommendation dataset schema to inject 5 additional continuous numerical audio feature vector properties beyond basic text tags to enable complex spatial similarity matching. I also tasked it with adding automatic trailing whitespace string sanitization during data loading.

**Prompts used:**
"Analyze a standard content-based recommendation dataset scheme. Brainstorm 5 additional meaningful audio properties beyond basic genre and mood tags to calculate continuous vector distances. Provide suggestions that mirror actual streaming variables used by Spotify or Echo Nest, and outline how to handle data cleaning for unexpected trailing spaces."

**What did the agent generate or change?**
* **`data/songs.csv`**: Modified schema to append column variables for `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`.
* **`src/recommender.py`**: Updated `load_songs()` to execute explicit floating-point transformations, inject a fallback parsing array configuration layer for `whitespace_genre`, and cleanse fields with `.strip().lower()`.

**What did you verify or fix manually?**
I ran an internal script execution print trace to manually verify that data casting exceptions were bypassed and checked that rows containing irregular structural spaces loaded into dictionaries without breaking vector evaluation logic.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**
The Behavioral Strategy Design Pattern (implemented functionally via discrete operational algorithm weight control states).

**How did AI help you brainstorm or implement it?**
I asked how to handle dynamic weight adjustment vectors across multiple recommendation profiles ("Standard" vs "Vibe-Focused") cleanly without repeating verification structures or using nested conditional blocks inside `main.py`. The AI suggested separating weight profiles using a key control string variable passed into a single modular engine function.

**How does the pattern appear in your final code?**
The strategy pattern is implemented functionally inside `src/recommender.py` within the `score_song()` method. It uses an `if/else` statement conditioned on the `mode` parameter:

if mode == "Vibe-Focused":
    w_genre, w_mood, w_energy, w_tempo, w_dance = 0.5, 1.5, 2.5, 1.5, 0.5
else: # Default Standard Mode Allocation
    w_genre, w_mood, w_energy, w_tempo, w_dance = 2.0, 1.0, 1.0, 1.0, 0.5

This conditional block acts as the concrete strategy selector, dynamically swapping the scalar scoring weights at runtime. This allows the master execution pipeline inside `recommend_songs()` to remain abstract, calculating entirely different recommendation sets without modifying its core loop or matching logic.