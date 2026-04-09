"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile used for recommendation comparisons
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 120,
        "target_valence": 0.80,
        "target_danceability": 0.80,
        "target_acousticness": 0.20,
        "likes_acoustic": False,
        # Backward-compatible aliases for starter scoring code
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 68)
    print("Top Recommendations (Profile: pop / happy)")
    print("=" * 68)

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(",") if reason.strip()]

        print(f"\n{idx}. {song['title']} - {song['artist']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")


if __name__ == "__main__":
    main()
