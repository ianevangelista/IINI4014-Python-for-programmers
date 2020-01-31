'''
Function that swaps two elements in a list
Takes:
array: list: the list
greater: string: the element with the highest value
lesser: string: the element with the lowest value
'''
def swap(array, greater, lesser):
    temp = array[greater]
    array[greater] = array[lesser]
    array[lesser] = temp

'''
Function that sorts an array of strings by length and lexicographically
Takes:
array: list: a list of strings
Return:
array: list: returning a sorted list of strings
'''
def bubbleSort(array):
    arrayLength = len(array)
    # Comparing element i to the rest of the list
    for i in range(arrayLength):

        # Current start-value: 0
        # Only iterates to arrayLength-i-1, depending on i
        for current in range(0, arrayLength-i-1):
            # Checking the length of the word
            if len(array[current]) > len(array[current+1]):
                swap(array, current, (current+1))

            # If length is equivalent, check word-value
            elif len(array[current]) == len(array[current+1]):
                if array[current] > array[current+1]:
                    swap(array, current, (current+1))     
    return array

'''
Function that reads a file and puts all words into a list which is sorted and prints out
Takes:
filename: string: the name of the file
'''
def sortWords(filename):
    with open(filename) as thisFile:
        try:
            wordsRead = []
            # All words are put into a list
            for line in thisFile:
                line = line.strip()
                wordsRead += line.split(" ")

            # Lowers all word
            words = [loweredWord.lower() for loweredWord in wordsRead]
            # Sorting
            myWords = bubbleSort(words)
            
            for word in myWords:
                print(word)
        except:
            print("Something went wrong")
        finally:
            thisFile.close()

def main():
    filename = "text.txt"
    sortWords(filename)

main()