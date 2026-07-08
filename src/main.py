from src.recommender import load_songs, recommend_songs

def print_profile_results(profile_name, recommendations):
    print("=" * 70)
    print(f"🎯 RECOMMENDATIONS FOR: {profile_name.upper()}")
    print("=" * 70)
    for idx, rec in enumerate(recommendations, 1):
        print(f"{idx}. '{rec['title']}' by {rec['artist']}")
        print(f"   📊 Match Score: {rec['score']}")
        print(f"   🔍 Reasons: {', '.join(rec['reasons'])}")
        print("-" * 70)
    print("\n")

def main():
    # Load songs from file
    songs = load_songs()
    print(f"📦 Loaded {len(songs)} tracks from data/songs.csv.\n")
    
    # Three clear, distinct user test profiles
    profiles = {
        "Chill Lofi Listener": {
            "preferred_genre": "lofi",
            "preferred_mood": "chill",
            "target_energy": 0.40,
            "target_tempo": 75
        },
        "High-Energy Pop/Rock Fan": {
            "preferred_genre": "pop",
            "preferred_mood": "intense",
            "target_energy": 0.90,
            "target_tempo": 135
        },
        "Walking Pace Afrobeats Listener": {
            "preferred_genre": "afrobeats",
            "preferred_mood": "encouraging",
            "target_energy": 0.65,
            "target_tempo": 68
        }
    }
    
    # Run recommendation generation for each test case
    for profile_name, preferences in profiles.items():
        top_recs = recommend_songs(preferences, songs, k=3)
        print_profile_results(profile_name, top_recs)

if __name__ == "__main__":
    main()