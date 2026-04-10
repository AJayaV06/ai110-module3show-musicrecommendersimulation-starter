"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import argparse

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def build_demo_profiles() -> dict:
    """Return a mix of normal and adversarial user profiles for demo runs."""
    return {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.80,
            "target_tempo_bpm": 120,
            "target_valence": 0.80,
            "target_danceability": 0.80,
            "target_acousticness": 0.20,
            "likes_acoustic": False,
            "genre": "pop",
            "mood": "happy",
            "energy": 0.80,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "focused",
            "target_energy": 0.45,
            "target_tempo_bpm": 82,
            "target_valence": 0.58,
            "target_danceability": 0.60,
            "target_acousticness": 0.78,
            "likes_acoustic": True,
            "genre": "lofi",
            "mood": "focused",
            "energy": 0.45,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.90,
            "target_tempo_bpm": 155,
            "target_valence": 0.45,
            "target_danceability": 0.68,
            "target_acousticness": 0.08,
            "likes_acoustic": False,
            "genre": "rock",
            "mood": "intense",
            "energy": 0.90,
        },
        "Conflicted Energy vs Mood": {
            "favorite_genre": "classical",
            "favorite_mood": "sad",
            "target_energy": 0.92,
            "target_tempo_bpm": 64,
            "target_valence": 0.18,
            "target_danceability": 0.20,
            "target_acousticness": 0.97,
            "likes_acoustic": True,
            "genre": "classical",
            "mood": "sad",
            "energy": 0.92,
        },
        "High Energy, Low Mood": {
            "favorite_genre": "pop",
            "favorite_mood": "melancholic",
            "target_energy": 0.95,
            "target_tempo_bpm": 132,
            "target_valence": 0.25,
            "target_danceability": 0.86,
            "target_acousticness": 0.10,
            "likes_acoustic": False,
            "genre": "pop",
            "mood": "melancholic",
            "energy": 0.95,
        },
        "Alias Mismatch": {
            "favorite_genre": "lofi",
            "favorite_mood": "focused",
            "target_energy": 0.45,
            "target_tempo_bpm": 80,
            "target_valence": 0.59,
            "target_danceability": 0.60,
            "target_acousticness": 0.78,
            "likes_acoustic": True,
            "genre": "metal",
            "mood": "angry",
            "energy": 0.10,
        },
        "Boundary Case Zero Energy": {
            "favorite_genre": "ambient",
            "favorite_mood": "calm",
            "target_energy": 0.0,
            "target_tempo_bpm": 60,
            "target_valence": 0.65,
            "target_danceability": 0.15,
            "target_acousticness": 0.95,
            "likes_acoustic": True,
            "genre": "ambient",
            "mood": "calm",
            "energy": 0.0,
        },
    }


def print_profile_summary(profile_name: str, profile: dict) -> None:
    """Print a readable summary of the chosen user profile."""
    print(f"\nProfile: {profile_name}")
    print("   Values:")
    print(f"   - favorite_genre: {profile['favorite_genre']}")
    print(f"   - favorite_mood: {profile['favorite_mood']}")
    print(f"   - target_energy: {profile['target_energy']:.2f}")
    print(f"   - target_tempo_bpm: {profile['target_tempo_bpm']}")
    print(f"   - target_valence: {profile['target_valence']:.2f}")
    print(f"   - target_danceability: {profile['target_danceability']:.2f}")
    print(f"   - target_acousticness: {profile['target_acousticness']:.2f}")
    print(f"   - likes_acoustic: {profile['likes_acoustic']}")


def print_recommendations(user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print recommendations in the same style used by the demo runner."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("   Recommendations:")
    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(",") if reason.strip()]

        print(f"\n   {idx}. {song['title']} - {song['artist']}")
        print(f"      Final Score: {score:.2f}")
        print("      Reasons:")
        for reason in reasons:
            print(f"      - {reason}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the music recommender for one profile.")
    parser.add_argument(
        "--profile",
        default="High-Energy Pop",
        help="Profile name to run. Use one of the names defined in build_demo_profiles().",
    )
    parser.add_argument(
        "--list-profiles",
        action="store_true",
        help="Print the available profile names and exit.",
    )
    args = parser.parse_args()

    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = build_demo_profiles()

    if args.list_profiles:
        print("Available profiles:")
        for profile_name in profiles:
            print(f"- {profile_name}")
        return

    if args.profile not in profiles:
        print(f"Unknown profile: {args.profile}")
        print("Available profiles:")
        for profile_name in profiles:
            print(f"- {profile_name}")
        return

    user_prefs = profiles[args.profile]

    print("\n" + "=" * 68)
    print(f"Top Recommendations ({args.profile})")
    print("=" * 68)

    print_profile_summary(args.profile, user_prefs)
    print_recommendations(user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
