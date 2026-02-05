alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = list(alphabet)

words = ["apple", "grape", "stone", "clock", "house", "water", "plant", "knife", "bread", 
         "light", "chair", "table", "flame", "grass", "scale"]

def sort_letters(words):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    letter_instances = []
    for letter in letters:
        count = 0
        for word in words:
            count += word.count(letter)  # Count occurrences of each letter in all words
        letter_instances.append([letter, count])
    return letter_instances

def grab_most_common_letters(words):
# Count letter occurrences
    letter_instances = sort_letters(words)
    print("\nLetter instances:")
    print(letter_instances)

    # Remove letters with 0 occurrences
    letter_instances = [item for item in letter_instances if item[1] != 0]
    
    # Sort by frequency in descending order
    letter_instances.sort(key=lambda x: x[1], reverse=True)
    return letter_instances


def main():
    
    words = ["apple", "grape", "stone", "clock", "house", "water", "plant", "knife", "bread", 
            "light", "chair", "table", "flame", "grass", "scale"]
    letterInstances = grab_most_common_letters(words)
    print(letterInstances)
if __name__ == "__main__":
    main()
