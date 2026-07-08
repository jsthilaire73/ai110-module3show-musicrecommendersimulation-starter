import csv

def load_songs(filepath="data/songs.csv"):
    """Reads the CSV file of songs and returns a list of dictionaries with correctly cast data types."""
    songs = []
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"].strip().lower(),
                "mood": row["mood"].strip().lower(),
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            })
    return songs

def score_song(user_prefs, song):
    """
    Computes a recommendation match score for a single song against a user's taste profile.
    Returns a tuple: (total_score, list_of_reasons)
    """
    score = 0.0
    reasons = []
    
    # 1. Genre Match (+2.0 points)
    if user_prefs.get("preferred_genre").lower() == song["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")
        
    # 2. Mood Match (+1.0 point)
    if user_prefs.get("preferred_mood").lower() == song["mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")
        
    # 3. Energy Similarity (Calculated via distance from target preference)
    energy_diff = abs(user_prefs.get("target_energy") - song["energy"])
    energy_score = round(max(0, 1.0 - energy_diff), 2)
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score})")
    
    # 4. Tempo Proximity (Calculated over an assumed maximum range of 100 BPM)
    tempo_diff = abs(user_prefs.get("target_tempo") - song["tempo_bpm"])
    tempo_score = round(max(0, 1.0 - (tempo_diff / 100.0)), 2)
    score += tempo_score
    reasons.append(f"tempo proximity (+{tempo_score})")

    return round(score, 2), reasons

def recommend_songs(user_prefs, songs, k=3):
    """Loops through all songs, scores them, and returns top k results sorted high-to-low."""
    scored_list = []
    
    for song in songs:
        total_score, reasons = score_song(user_prefs, song)
        scored_list.append({
            "title": song["title"],
            "artist": song["artist"],
            "score": total_score,
            "reasons": reasons
        })
        
    # Sort from highest score to lowest score using sorted() to keep original list safe
    sorted_recommendations = sorted(scored_list, key=lambda x: x["score"], reverse=True)
    return sorted_recommendations[:k]