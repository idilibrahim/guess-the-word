# game_stats.py

def display_stats(total_attempts, total_word_guesses):
    """Display game statistics."""
    print("---Game Statistics --")
    print(f"Total Attempts: {total_attempts}")
    print(f"Total Word Guesses: {total_word_guesses}")
    print("------------------------")

def update_stats(total_attempts, total_word_guesses, attempts, word_guesses):
    """Update game statistics."""
    total_attempts += attempts
    total_word_guesses += word_guesses
    return total_attempts, total_word_guesses
