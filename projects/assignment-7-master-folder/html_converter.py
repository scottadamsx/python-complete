#! usr/bin/env python3
# HTML TAG REMOVER - Passes an HTML file and removes the tags
#                    from the source code, and returns the html
#                    as a txt file with the same name

def title():
    title = "Html Tag Remover\n"
    print(title)

# reads the file as a file and returns it as a string
def read_html():
    FILENAME = "groceries.html"
    with open(FILENAME) as file:
        fileAsString = file.read()
    return fileAsString
    
# finds the index of the start of the tag and end of the tag and replaces the text inbetween with nothing
def remove_tags(string):
    while True:
        startingTagIndex = string.find("<")
        # if index is -1, then there are no more tags to remove
        if startingTagIndex == -1:
            return string
        # if not, there is still a tag in the file, remove it
        else:
            endingTagIndex = string.find(">")
            #print(startingTagIndex,endingTagIndex) -> test code to see index's
            if string[startingTagIndex:endingTagIndex+1] == "<li>":
                string = string.replace(string[startingTagIndex:endingTagIndex+1],"* ")
            else: 
                string = string.replace(string[startingTagIndex:endingTagIndex+1],"")

def main():

    title()
    string = read_html()
    string = remove_tags(string)
    print(string)

if __name__ == "__main__":
    main()