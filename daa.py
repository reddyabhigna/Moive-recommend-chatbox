def movie_chatbot():
    print("🎥 Welcome to ABHIGNAMOIVERULE — your personal movie recommender!")
    print("You can ask me for a movie by mood or genre.")
    print("what is ur current mood', or 'bye' to quit.\n")

    # Predefined movie database
    movies = {
        "action": ["Abhimanyudu", "Action", "Business man"],
        "comedy": ["Mahanubavudu", "Anjinelulu", "E nagaram ki em ayindi"],
        "romance": ["Arjun reddy", "Midunam"],
        "drama": ["Snkranthi ki vastunam", "nannaku prema", "F2"],
        "horror": ["Gangorthi", "Shiva"],
        "sci-fi": ["Inception", "Interstellar", "Dune"]
    }

    # Mood mapping
    mood_map = {
        "bored": "comedy",
        "sad": "drama",
        "excited": "action",
        "romantic": "romance",
        "scared": "horror"
    }

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print(" Hey user: Goodbye! Enjoy your movie night 🍿")
            print(" After completion of moive give review")
            break

        # Detect mood requests
        for mood, genre in mood_map.items():
            if mood in user_input:
                print(f"Hey user: Looks like you're feeling {mood} — try some {genre} movies!")
                for m in movies[genre]:
                    print("-", m)
                break
        else:
            # Detect genre requests
            found = False
            for genre in movies:
                if genre in user_input:
                    print(f"Bot: Here are some popular {genre} movies:")
                    for m in movies[genre]:
                        print("-", m)
                    found = True
                    break

            if not found:
                print("Bot: I didn’t understand that. Try mentioning a genre or mood (like 'action' or 'sad').")

# Run chatbot
movie_chatbot()
