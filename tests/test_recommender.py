import pytest
from src.recommender import score_song, recommend_songs

def make_small_songs_catalog():
    """Generates a mock track dataset for controlled evaluation."""
    return [
        {
            "id": 1,
            "title": "Test Pop Track",
            "artist": "Test Artist",
            "genre": "pop",
            "whitespace_genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120,
            "valence": 0.9,
            "danceability": 0.8,
            "acousticness": 0.2
        },
        {
            "id": 2,
            "title": "Chill Lofi Loop",
            "artist": "Test Artist",
            "genre": "lofi",
            "whitespace_genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "tempo_bpm": 80,
            "valence": 0.6,
            "danceability": 0.5,
            "acousticness": 0.9
        }
    ]

def test_recommend_returns_songs_sorted_by_score():
    """Verifies recommendations are ordered from highest to lowest matching score."""
    user_prefs = {
        "preferred_genre": "pop",
        "preferred_mood": "happy",
        "target_energy": 0.8,
        "target_tempo": 120,
        "target_danceability": 0.8
    }
    songs = make_small_songs_catalog()
    results = recommend_songs(user_prefs, songs, k=2, mode="Standard")

    assert len(results) == 2
    assert results[0]["title"] == "Test Pop Track"
    assert "genre match (+2.0)" in results[0]["reasons"]

def test_explain_recommendation_returns_non_empty_reasons():
    """Ensures the scoring component documents individual weight logs correctly."""
    user_prefs = {
        "preferred_genre": "pop",
        "preferred_mood": "happy",
        "target_energy": 0.8,
        "target_tempo": 120,
        "target_danceability": 0.8
    }
    songs = make_small_songs_catalog()
    total_score, reasons = score_song(user_prefs, songs[0])
    
    assert isinstance(reasons, list)
    assert len(reasons) > 0
    assert isinstance(reasons[0], str)
    assert reasons[0].strip() != ""