import csv
import os

def load_songs():
    """Loads and sanitizes track catalog data from the CSV database."""
    songs = []
    csv_path = os.path.join("data", "songs.csv")
    if not os.path.exists(csv_path):
        return []
        
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"].strip(),
                "artist": row["artist"].strip(),
                "genre": row["genre"].strip().lower(),
                "whitespace_genre": row.get("whitespace_genre", row["genre"]).strip().lower(),
                "mood": row["mood"].strip().lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            })
    return songs

def score_song(user_prefs, song, mode="Standard"):
    """Calculates granular match values using Strategy-specific weight configurations."""
    score = 0.0
    reasons = []

    # Dynamic Weight Matrices via Strategy Design Pattern
    if mode == "Vibe-Focused":
        w_genre, w_mood, w_energy, w_tempo, w_dance = 0.5, 1.5, 2.5, 1.5, 0.5
    else:  # Default Standard Mode Allocation
        w_genre, w_mood, w_energy, w_tempo, w_dance = 2.0, 1.0, 1.0, 1.0, 0.5

    # 1. Categorical Genre Match
    if song["genre"] == user_prefs["preferred_genre"] or song["whitespace_genre"] == user_prefs["preferred_genre"]:
        score += w_genre
        reasons.append(f"genre match (+{w_genre})")

    # 2. Categorical Mood Match
    if song["mood"] == user_prefs["preferred_mood"]:
        score += w_mood
        reasons.append(f"mood match (+{w_mood})")

    # 3. Continuous Energy Proximity (Inverse Absolute Delta)
    energy_prox = 1.0 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_prox * w_energy
    reasons.append(f"energy proximity (+{energy_prox * w_energy:.2f})")

    # 4. Continuous Tempo Proximity (Normalized Scaling Check)
    tempo_delta = abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / user_prefs["target_tempo"]
    tempo_prox = max(0.0, 1.0 - tempo_delta)
    score += tempo_prox * w_tempo
    reasons.append(f"tempo proximity (+{tempo_prox * w_tempo:.2f})")

    # 5. Continuous Danceability Proximity
    dance_prox = 1.0 - abs(song["danceability"] - user_prefs["target_danceability"])
    score += dance_prox * w_dance
    reasons.append(f"danceability match (+{dance_prox * w_dance:.2f})")

    return round(score, 2), reasons

def recommend_songs(user_prefs, songs, k=3, mode="Standard"):
    """
    Ranks all songs, applies artist diversity penalties, and returns the top k recommendations.
    """
    # 1. Calculate all initial scores
    all_scored = []
    for song in songs:
        base_score, reasons = score_song(user_prefs, song, mode)
        all_scored.append({
            "title": song["title"],
            "artist": song["artist"],
            "score": base_score,
            "reasons": list(reasons)
        })

    # 2. Sort initially to identify top artists
    all_scored.sort(key=lambda x: x["score"], reverse=True)
    
    # 3. Apply Diversity Penalty across the entire list
    seen_artists = set()
    for track in all_scored:
        if track["artist"] in seen_artists:
            track["score"] = round(track["score"] - 0.75, 2)
            track["reasons"].append("artist bubble penalty (-0.75)")
        seen_artists.add(track["artist"])

    # 4. Final sort after penalties have been applied
    all_scored.sort(key=lambda x: x["score"], reverse=True)
    
    return all_scored[:k]