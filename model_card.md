# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender system is designed to generate highly targeted, attribute-based individual track suggestions. It assumes that a user's current musical taste can be accurately captured by explicit, static targets (such as a preferred genre text tag, a mood tag, a specific energy level, and an exact target tempo). Rather than being deployed for commercial production or scaling to live streaming applications, this system is explicitly intended for academic classroom exploration to illustrate the foundational data transformations under the hood of basic machine learning filtering loops.

---

## 3. How the Model Works  

VibeFinder 1.0 looks at a song's structural DNA to see how well it fits a user's specific request. It relies on a blend of core textual tags—genre and mood—alongside physical musical traits like energy (how intense or powerful a track feels) and tempo (the speed measured in beats per minute). 

When a user provides their target profile, the model acts like a point-based judge for every single track in the library catalog:
* It awards a massive +2.0 points if the song belongs to the exact genre requested.
* It throws in an extra +1.0 point if the song matches the user's specific mood state.
* For energy and tempo, it calculates a proximity score. Instead of assuming higher numbers are better, it uses a distance rule that looks at how far away the track is from the user's target. A song right on the bullseye receives a full +1.0 point for that feature, while tracks that drift away are penalized based on how far they deviate. 

Finally, the system gathers all these totals and stacks the songs in a sorted list from highest score to lowest score to pick the top 3 items. From the starter logic, the architecture was intentionally expanded to dynamically generate clear, human-readable "Decision Logs" so that the user can see the exact breakdown of points behind every single recommendation.

---

## 4. Data  

The simulation reads from a structured database catalog containing 15 distinct tracks. The collection represents a diverse cross-section of sonic aesthetics, capturing genres such as Pop, Lofi, Rock, Ambient, Jazz, Synthwave, Indie Pop, R&B, Hip-Hop, and Afrobeats, alongside emotional mood states ranging from happy and intense to relaxed, focused, and encouraging. 

To satisfy the grading criteria, we manually expanded the initial starter data file by appending 5 new tracks representing missing sonic spaces. Despite this expansion, massive dimensions of true human musical taste remain completely absent from the dataset—including lyrical themes, cultural era, instrumentation types, or historical song popularity vectors.

---

## 5. Strengths  

The system excels when handling highly distinct, specialized user profiles that demand strict aesthetic isolation. For instance, during execution, it delivered perfectly intuitive results for the "Chill Lofi Listener" by accurately prioritizing slow-tempo, low-energy tracks from LoRoom and Paper Lanterns. 

It captures exact matching patterns with incredible accuracy, successfully scoring a flawless, maximum possible 5.0 out of 5.0 for the track 'Hero' by RICO FONTAINE because the song perfectly satisfied the categorical genre/mood constraints while landing dead-on the targeted walking pace of 68 beats per minute.

---

## 6. Limitations and Bias  

Because VibeFinder 1.0 is built entirely on text-string matching and basic numeric boundaries, it suffers from significant algorithmic biases:
* **The Filter Bubble:** Because a matching genre text string awards an overwhelming +2.0 points, the algorithm heavily overfits to that specific label. A lofi enthusiast is entirely blocked out from discovering phenomenal, low-energy tracks from the ambient or jazz rows purely because the textual genre word doesn't match, creating a massive echo chamber.
* **Lack of Nuance:** The scoring completely ignores complex audio nuances like vocal characteristics or historical relevance, blindly trusting flat numbers. 
* **Data Imbalance:** Some genres or moods have higher representation in our 15-song catalog than others, unintentionally giving pop listeners a much wider variety of optimal paths than niche genre selectors.

---

## 7. Evaluation  

The system was audited using three heavily contrasting test profiles to ensure the scoring loop reacted accurately to diverse user demands:
1. **Chill Lofi Listener:** Targeted slow, low-energy study vibes.
2. **High-Energy Pop/Rock Fan:** Targeted intense, fast-paced gym vibes.
3. **Walking Pace Afrobeats Listener:** Targeted rhythmic, encouraging vibes.

We systematically audited the terminal logs to make sure the math held up and that the sorting pipeline correctly grouped songs. One surprising outcome was seeing 'Gods Plan' by Drake edge out other options into the top 3 for the Afrobeats profile. Because 'Gods Plan' sat perfectly at a relaxed 77 BPM, its high tempo proximity score allowed it to jump ahead of other songs whose genres didn't match but whose tempos were way too fast. This proved that our continuous numerical distance formulas were working dynamically beneath the heavy genre sorting tags.

---

## 8. Implemented Advanced Features

The initial simulation was significantly upgraded to move beyond static filtering, incorporating the following advanced capabilities:

* **Diversity & Artist Penalty Logic:** To counteract "filter bubbles," the system now utilizes a sequential history-tracking loop. If a specific artist occupies a top-ranked recommendation slot, subsequent tracks by that same creator receive a dynamic `-0.75` point deduction. This ensures that the user's feed remains varied and encourages broader discovery.
* **Multi-Strategy Ranking Engine:** The engine now supports runtime strategy selection. Users can toggle between **"Standard Mode"** (which prioritizes strict categorical genre/mood matching) and **"Vibe-Focused Mode"** (which down-weights text tags to elevate continuous sonic proximity metrics). This is achieved through a functional Strategy Pattern implementation that dynamically swaps scoring weight matrices without modifying the core execution loop.
* **Multi-Dimensional Feature Integration:** The scoring logic was expanded to process a full vector of audio properties. Beyond basic tags, the engine now calculates continuous proximity distances for `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`, allowing the model to perform spatial similarity matching rather than relying solely on keyword matching.

---

## 9. Personal Reflection  

Building this simulation provided a fantastic look at the mechanics behind real-world prediction engines, demystifying how platforms like Spotify transform abstract concepts like a musical "vibe" into pure numbers. It was eye-opening to discover that even a basic sequence of text comparisons and absolute differences can yield a terminal output that feels remarkably like an intuitive, personalized recommendation. 

However, seeing how easily a heavy genre weight traps users in a strict filter bubble completely changed how I look at commercial music streaming apps. It highlights just how much deliberate engineering effort must go into coding fairness, variety, and discovery logic to keep users from being permanently boxed into a single corner of music.
