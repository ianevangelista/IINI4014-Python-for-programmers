from collections import Counter

# Removes all unnecessary chars in the string
def replaceChar(myWord):
    myWord = myWord.rstrip()
    myWord = myWord.replace('"', "")
    myWord = myWord.replace('?', "")
    myWord = myWord.replace(',', "")
    myWord = myWord.replace('.', "")
    myWord = myWord.replace(':', "")
    myWord = myWord.replace('()', "")
    myWord = myWord.replace('-', "")
    return myWord    

# Removes all whitespace between lines
def removeWhitespaceLines(myLine):
    while myLine.isspace():
        myLine = myLine.rstrip()
    return myLine

def getWordFreqs(filename):
    with open(filename) as thisFile:
        try:
            dictionary = []
            # Reads every line in the text-file
            for line in thisFile:
                line = removeWhitespaceLines(line)

                # Puts all words in a list
                allWords = line.split(" ")
                # Lowers all words
                wordsLower = [loweredWord.lower() for loweredWord in allWords]
                # Cleans and add words into a new list
                for word in wordsLower:
                    word = replaceChar(word)
                    dictionary.append(word)
            
            # Counts all word-frequencies and return as a dictionary 
            myCounter = Counter(dictionary)
            return myCounter

        except:
            print("Something went wrong")
        finally:
            thisFile.close()

def getWordLine(filename, myWord):
    myWord = myWord.lower()
    with open(filename) as thisFile:
        try:
            listOfLines = []
            counterLine = 0

            # Counts the current line and splits all the words
            for line in thisFile:
                counterLine += 1
                allWords = line.split(" ")
                wordsLower = [loweredWord.lower() for loweredWord in allWords]

                # Checks if the the input equals a word in a line
                for word in wordsLower:
                    word = replaceChar(word)
                    if word == myWord:
                        listOfLines.append(counterLine)

            # Returns the list of lines
            return listOfLines
        except:
            print("Something went wrong")
        finally:
            thisFile.close()

def main():
    # Reading a text-file and prints out alle the word-frequencies
    dictionary = getWordFreqs("books/folder_00/pg5200.txt")
    for thisWord in dictionary:
        print(thisWord, ":", dictionary[thisWord])
    print("The word living has", dictionary.get("living"), "lines in the text")

    # Reading a text-file and prints out every line-number the input equals a word in
    myList = getWordLine("books/folder_00/pg5200.txt", "living")
    print("The word living is included in these lines:")
    for line in myList:
        print("Line:", line)

main()