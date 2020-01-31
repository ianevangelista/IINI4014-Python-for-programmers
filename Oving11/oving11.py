from collections import Counter


def averageSentenceLength(file_contents):
    '''
    Function that calculates the average length of a sentence
    Takes:
    file_contents: string: the whole text
    Return:
    totalWords/totalSentences: float: a percentage
    '''
    # Splits all sentences and puts into a list
    totalSentences = file_contents.count('.')
    totalWords = len(file_contents.split())

    # Rounds the total wors per sentence with 3 decimals
    return round(totalWords / totalSentences, 3)


def wordPercentage(file_contents):
    '''
    Function that calculates the frequency of words
    Takes:
    file_contents: string: the whole text
    Return:
    dictionary: dictionary: a string-indexed list of percentages
    '''

    # Setting a limit for the frequency of a word
    percentageEasy = 0.02
    percentageDifficult = 0.005

    allWords = file_contents.split()
    dictionary = Counter(allWords).most_common()
    totalWords = len(allWords)

    counterWord = 0
    totalEasyWords = 0
    totalDifficultWords = 0

    # Counting how many easy and difficult words
    for word in range(len(dictionary)):
        if ((dictionary[counterWord][1] / totalWords) < percentageDifficult):
            totalDifficultWords += 1

        elif ((dictionary[counterWord][1] / totalWords) > percentageEasy):
            totalEasyWords += 1
        counterWord = counterWord + 1

    # Creating a dictionary for the percentages
    dictionary = dict()
    dictionary['easyPercentage'] = round(totalEasyWords / totalWords, 3) * 100
    dictionary['difficultPercentage'] = round(
        totalDifficultWords / totalWords, 3) * 100
    return dictionary


def differentWordsPercentage(file_contents):
    '''
    Function that calculates the percentage of different words
    Takes:
    file_contents: string: the whole text
    Return:
    totalDifferentWords/totalSentences: float: a percentage
    '''

    allWords = file_contents.split()
    dictionary = Counter(allWords).most_common()
    totalDifferentWords = len(dictionary)
    totalWords = len(allWords)
    return round(totalDifferentWords / totalWords, 3) * 100


def sentencesPerParagraph(file_contents):
    '''
    Function that calculates the average sentences per paragraph
    Takes:
    file_contents: string: the whole text
    Return:
    totalSentences/totalParagraphs: float: a percentage
    '''
    totalSentences = file_contents.count('.')
    totalParagraphs = len(file_contents.split('\n\n'))
    return round(totalSentences / totalParagraphs, 3)


def analyseText(filename):
    '''
    Function that analyses a textfile an utilizes multiple functions
    Takes:
    filename: string: the name of the textfile
    '''
    with open(filename) as thisFile:
        try:
            file_contents = thisFile.read()
            print("\nAverage words per sentence are:",
                  averageSentenceLength(file_contents))
            print("\nPercentage of easy words are:",
                  wordPercentage(file_contents).get('easyPercentage'), '%')
            print("\nPercentage of difficult words are:",
                  wordPercentage(file_contents).get('difficultPercentage'), '%')
            print("\nPercentage of different words are:",
                  differentWordsPercentage(file_contents), '%')
            print("\nNumber of sentences per paragraph:",
                  sentencesPerParagraph(file_contents), '\n')
        except:
            print("Something went wrong")
        finally:
            thisFile.close()


def main():
    filename = "text.txt"
    analyseText(filename)


main()
