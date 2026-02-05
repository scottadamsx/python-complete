#! usr/bin/env python3

def get_words():
    list = []
    while True:
        print("Enter words! enter \"done\" to exit.")
        word = input("Enter a word: ")
        list.append(word)

        if word.lower() == "done":
            break
    return list


def display_words(list):
    for word in list:
        print(word)
 

def modify_list(list):
    for word in list:
        index = list.index(word)
        list[index] = word.upper() 

    print(list)


def concatenate_list(list):
    big_string = ""
    for word in list:
        big_string += word
    print(big_string)


def main():

    list = get_words()
    display_words(list)
    modify_list(list)
    concatenate_list(list)

if __name__ == "__main__":
    main()


