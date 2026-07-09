# 🎵 Music Recommender Simulation

## Project Summary
This project implements a fully functional Content-Based Music Recommendation Simulation in Python. The system evaluates a personalized target user taste profile against a structured song catalog database, utilizing feature matching and distance metrics to score, rank, and recommend the most optimal musical matches.

## How The System Works

### Recommendation Mechanics
Real-world streaming platforms use two primary systems to suggest music:
1. **Collaborative Filtering:** Looks at user behavior trends (e.g., "Users who liked Song X also liked Song Y").
2. **Content-Based Filtering:** Looks directly at the properties of the item itself (e.g., genre tags, mood attributes, or acoustic data).

This simulation builds a **Content-Based Filtering** architecture. It transforms static song attributes and customized user preferences into a direct mathematical prediction model.

### System Architecture Features
* **Song Object Attributes:** `id`, `title`, `artist`, `genre`, `mood`, `energy` (0.0–1.0), `tempo_bpm`, `valence`, `danceability`, `acousticness`.
* **UserProfile Stores:** `preferred_genre`, `preferred_mood`, `target_energy`, `target_tempo`.

### Algorithm Recipe
The recommender awards points to each song based on how closely it meets the user's explicit taste criteria:
* **Genre Match:** $+2.0$ points if the song's genre matches the profile's preferred genre perfectly.
* **Mood Match:** $+1.0$ point if the song's mood matches the profile's preferred mood perfectly.
* **Energy Proximity:** Up to $+1.0$ point based on absolute linear distance: $1.0 - |\text{Target Energy} - \text{Song Energy}|$.
* **Tempo Proximity:** Up to $+1.0$ point calculated over a normalized scale: $1.0 - \frac{|\text{Target Tempo} - \text{Song Tempo}|}{100}$.

### Scoring vs. Ranking Rules
* **Scoring Rule (`score_song`):** Acts as an individual track judge. It calculates a static, absolute number indicating how closely a single track's profile aligns with the target parameters.
* **Ranking Rule (`recommend_songs`):** Organizes the entire structural database list. It collects all raw output scores, utilizes the `sorted()` function to sort them from highest to lowest without disrupting the source catalog list data, and trims the list to return the top $K$ absolute choices.

---

## Sample Recommendation Output

📦 Loaded 15 tracks from data/songs.csv.


🎯 RECOMMENDATIONS FOR: CHILL LOFI LISTENER

1. 'Midnight Coding' by LoRoom | Score: 4.95 | Reasons: genre match (+2.0), mood match (+1.0), energy proximity (+0.98), tempo proximity (+0.97)
2. 'Library Rain' by Paper Lanterns | Score: 4.92 | Reasons: genre match (+2.0), mood match (+1.0), energy proximity (+0.95), tempo proximity (+0.97)
3. 'Focus Flow' by LoRoom | Score: 3.95 | Reasons: genre match (+2.0), energy proximity (+1.0), tempo proximity (+0.95)

======================================================================
🎯 RECOMMENDATIONS FOR: HIP-HOP FAN
======================================================================
1. 'Gods Plan' by Drake | Score: 4.94 | Reasons: genre match (+2.0), mood match (+1.0), energy proximity (+0.97), tempo proximity (+0.97)
2. 'First Class' by Jack Harlow | Score: 3.75 | Reasons: genre match (+2.0), energy proximity (+0.92), tempo proximity (+0.83)
3. 'Industry Baby' by Lil Nas X | Score: 2.82 | Reasons: mood match (+1.0), energy proximity (+0.99), tempo proximity (+0.83)

======================================================================
🎯 RECOMMENDATIONS FOR: SYNTHWAVE FAN
======================================================================
1. 'Neon Horizon' by Laserhawk | Score: 5.0 | Reasons: genre match (+2.0), mood match (+1.0), energy proximity (+1.0), tempo proximity (+1.0)
2. 'Turbo Drive' by CyberCorp | Score: 3.62 | Reasons: genre match (+2.0), energy proximity (+0.87), tempo proximity (+0.75)
3. 'Techno Core' by CyberCorp | Score: 1.71 | Reasons: energy proximity (+0.8), tempo proximity (+0.91)

---

## Experiments You Tried
* **Profile Differentiation Analysis:** Running distinct profiles demonstrated that the mathematical weights successfully separated preferences. The Lofi Listener received tracks with slow tempos and low energy, while the Hip-Hop and Synthwave fans successfully bubbled up tracks with high energy and faster tempos.
* **Acoustic/Valence Exclusion:** We temporarily omitted valence and acousticness from our baseline weights, which kept recommendations hyper-focused purely on the rhythmic structural parameters (energy and tempo).

## Limitations and Risks
* **Small Database Catalog:** With only 15 songs, users run out of variety almost instantly.
* **Filter Bubbles:** The $+2.0$ weight on genre is incredibly strong. If a user likes "lofi", the system will exclusively lock them into lofi songs, completely missing great low-energy songs from other genres simply because the text string tag doesn't match.

## Reflection: What I Learned About Recommendations and Bias
Through building this simulation, I learned that recommendation systems bridge the gap between abstract human tastes and computer logic by translating musical traits into standardized data points. By using explicit categorical tags like genre and mood alongside continuous metrics like energy and a walking-pace tempo of $68$ BPM, the algorithm can calculate absolute mathematical distances. This process transforms a user's target preferences into a concrete numeric ranking list. It was eye-opening to see how simple data transformations—like subtracting a song's attribute distance from a perfect score—can generate an output list that genuinely feels like an intuitive, personalized recommendation.

However, this project also clearly illustrated how easily systemic bias and algorithmic "filter bubbles" can be introduced through weighting choices. Because our algorithm heavily prioritizes exact text-string matches for genres (awarding a massive $+2.0$ points), it unintentionally locks users into a narrow echo chamber. For example, a lofi enthusiast's recommendation list is completely saturated by lofi tags, completely blocking out excellent, low-energy tracks from ambient or jazz rows that match their desired mood and tempo perfectly. This experience changed how I look at commercial streaming apps, highlighting that true engineering success requires a deliberate balance between mathematical precision and designed fairness to prevent users from being permanently boxed into a single musical corner.
