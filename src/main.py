from src.recommender import load_songs, recommend_songs

def print_visual_table(profile_name, mode_name, recommendations):
    print("=" * 90)
    print(f"🎯 PROFILE: {profile_name.upper()} | 🛠️ MODE: {mode_name.upper()}")
    print("=" * 90)
    print(f"{'Rank':<6}| {'Song Title':<26}| {'Artist':<19}| {'Score':<7}| {'Decision Logs / Reasons'}")
    print("-" * 90)
    
    for idx, rec in enumerate(recommendations, 1):
        reasons_str = ", ".join(rec['reasons'])
        score_val = rec['score']
        score_str = f"{score_val:.2f}" if isinstance(score_val, float) and len(str(score_val)) > 4 else str(score_val)
        
        print(f"{idx:<6}| {rec['title']:<26}| {rec['artist']:<19}| {score_str:<7}| {reasons_str}")
    print("=" * 90 + "\n")

def main():
    songs = load_songs()
    print(f"📦 System Initialized: Loaded {len(songs)} tracks from data/songs.csv.\n")
    
    # PROFILE 1: Chill Lofi Listener (Standard Mode)
    lofi_user = {
        "preferred_genre": "lofi",
        "preferred_mood": "chill",
        "target_energy": 0.40,
        "target_tempo": 75,
        "target_danceability": 0.60
    }
    recs_lofi_standard = recommend_songs(lofi_user, songs, k=3, mode="Standard")
    print_visual_table("Chill Lofi Listener", "Standard Mode", recs_lofi_standard)
    
    # PROFILE 1: Chill Lofi Listener (Vibe-Focused Strategy Mode)
    recs_lofi_vibe = recommend_songs(lofi_user, songs, k=3, mode="Vibe-Focused")
    print_visual_table("Chill Lofi Listener", "Vibe-Focused Strategy Mode", recs_lofi_vibe)

    # PROFILE 2: High-Energy Hip-Hop Fan
    hiphop_user = {
        "preferred_genre": "hip-hop",
        "preferred_mood": "energetic",
        "target_energy": 0.85,
        "target_tempo": 95,
        "target_danceability": 0.80
    }
    recs_hiphop = recommend_songs(hiphop_user, songs, k=3, mode="Standard")
    print_visual_table("High-Energy Hip-Hop Fan", "Standard Mode", recs_hiphop)

    # PROFILE 3: High-Tempo EDM Fan
    edm_user = {
        "preferred_genre": "synthwave",
        "preferred_mood": "intense",
        "target_energy": 0.90,
        "target_tempo": 130,
        "target_danceability": 0.75
    }
    recs_edm = recommend_songs(edm_user, songs, k=3, mode="Standard")
    print_visual_table("High-Tempo EDM Fan", "Standard Mode", recs_edm)

if __name__ == "__main__":
    main()