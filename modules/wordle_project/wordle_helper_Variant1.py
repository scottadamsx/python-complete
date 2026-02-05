#!/usr/bin/env python3
# SCOTTY'S WORDLE ASSISTANT

from .wordle_words import wordList
from time import sleep
import random
from . import letter_counter


def grab_guess():
    """Prompt the user for a 5-letter guess."""
    while True:
        guess = input("What is your guess: ").strip().lower()
        if len(guess) == 5:
            return guess
        print("Must be a 5-letter word. Please try again.")


def ask_for_hints(guess):
    """Prompt the user for feedback on each letter in their guess."""
    feedback = []
    for letter in guess:
        color = input(f"What color is the letter {letter.upper()}? (grey, yellow, green): ").strip().lower()
        feedback.append([letter, color])
    return feedback


def update_list(feedback, possible_words):
    """
    Filter the possible words list based on the feedback.
    
    Feedback colors:
    - grey: Letter not in the word.
    - green: Letter in the correct position.
    - yellow: Letter in the word but not in the same position.
    """
    # Handle grey letters
    for letter, color in feedback:
        if color == "grey":
            possible_words = [word for word in possible_words if letter not in word]

    # Handle green letters
    for i, (letter, color) in enumerate(feedback):
        if color == "green":
            possible_words = [word for word in possible_words if len(word) == 5 and word[i] == letter]

    # Handle yellow letters
    for i, (letter, color) in enumerate(feedback):
        if color == "yellow":
            possible_words = [word for word in possible_words if letter in word and word[i] != letter]

    return possible_words


def display_list_with_title(words, title="POSSIBLE WORDS"):
    """Display the list of words with a title."""
    print(f"{title} ({len(words)}):")
    for word in words:
        print(word)


def grab_best_guesses(letter_instances, words):
    """Get the best guesses based on the most common letters."""
    best_guesses = []
    for letter, _ in letter_instances[:4]:  # Top 4 most common letters
        best_guesses.extend([word for word in words if letter in word])
    return best_guesses


def grab_most_reoccurring_word(best_guesses):
    """Find the word with the highest letter repetition score."""
    from collections import Counter

    def letter_repetition_score(word):
        counts = Counter(word)
        return sum(count - 1 for count in counts.values() if count > 1)

    return max(best_guesses, key=letter_repetition_score, default="")


def main():
    print("SCOTTY'S WORDLE ASSISTANT")
    global wordList

    guess_counter = 1
    while len(wordList) > 1:
        print(f"\nGUESS {guess_counter}")
        
        guess = grab_guess()
        feedback = ask_for_hints(guess)
        wordList = update_list(feedback, wordList)

        display_list_with_title(wordList, "POSSIBLE WORDS")

        letter_instances = letter_counter.grab_most_common_letters(wordList)
        print("Letter frequencies:")
        for letter, count in letter_instances:
            print(f"{letter}: {count}")

        best_guesses = grab_best_guesses(letter_instances, wordList)
        print("\nBest guesses:")
        print(", ".join(best_guesses))

        most_reoccurring_word = grab_most_reoccurring_word(best_guesses)
        print(f"\nMost reoccurring word in best guesses: {most_reoccurring_word}")

        guess_counter += 1

    print(f"\nCorrect word: {wordList[0]}")


if __name__ == "__main__":
    main()
