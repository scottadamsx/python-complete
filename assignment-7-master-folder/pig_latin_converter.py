#1 usr/bin/env python3

def title():
    print("Pig Latin Converter\n")

def change_to_piglatin(english):
    words = english.split(" ")
    for word in words:
        if word[0] in "aeiou":
            newWord = word + "way"
            words[words.index(word)] = newWord
        elif word[0] in "bcdfghjklmnpqrstvwxyz":
            for letter in word:
                if letter in "aeiouy":
                    if letter == "y" and word.index(letter) == 0:
                        continue
                    else:
                        firstIndex = word.index(letter)
                        break
            moveToBack = word[0:firstIndex]
            newWord = word[firstIndex:] + moveToBack + "ay"
            words[words.index(word)] = newWord
    
    # changes the list of piglatin words to a string
    pigLatin = " ".join(words)
    return pigLatin
    

def main():

    title()

    # program loops until user chooses to end
    while True:

        sentance = str(input("Enter Text: ")).lower()
    
        english = sentance.replace(",","").replace("?","").replace("!","").replace("_","").replace(".","").replace("-","")
        print(f"English: {english}")
        pigLatin = change_to_piglatin(english)
        print("Pig Latin: ", pigLatin)

        # prompts the user to go again, or end the loop
        go_again = input("\nContinue? (y/n): ").lower()
        if go_again != "y":
            print("\nbye!\n")
            break


if __name__ == "__main__":
    main()