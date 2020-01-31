import os
from os import walk
import shutil


files = []
graphicsFolder = []
graphicTypes = ["eps", "tif", "png", "jpg"]
texFiles = []
dump = []
graphicsFound = []


def makeLists(path):
    '''
    Function that creates a main list over all files
    Takes:
    path: string: pathname
    '''
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(list(map(lambda x: path + "/" + x, filenames)))
        for subdir in dirnames:
            makeLists(dir+"/"+subdir)
        break


def createGraphicsFolder(path):
    '''
    Search through all graphic contents and appends them to list
    Takes:
    path: string: pathname
    '''
    for fileName in files:
        temp = fileName.split(".")
        if temp[-1].lower() in graphicTypes:
            graphicsFolder.append(fileName)


def createTexFolder():
    '''
    Function that finds all tex-files
    '''
    for fileName in files:
        temp = fileName.split(".")
        if temp[-1].lower() == "tex":
            texFiles.append(fileName)


def moveGraphicsNotIncluded():
    '''
    Moving graphic files not included in tex to dump by renaming it's path
    '''
    for graphic in graphicsFolder:
        destination = "./files/dump"
        temp = graphic.split("./files/")[-1]
        os.rename(graphic, (destination + temp))


def moveGraphics():
    '''
    Finding all graphic-files in tex-files
    '''
    for fileName in texFiles:
        with open(fileName, "r") as thisFile:
            for line in thisFile:
                for graphic in graphicsFolder:
                    temp = graphic.split("./files/")[-1]
                    if temp in line:
                        graphicsFound.append(temp)
                        graphicsFolder.remove(graphic)
    totGraphicsFound()


def moveGraphicsToFolder():
    '''
    Moving graphic files to folder by renaming it's path
    '''
    source = "./files"
    destination = "./files/"
    for graphic in graphicsFound:
        ext = graphic.split(".")[-1]
        destination += ext
        os.rename(".files/" + graphic, destination + ext + graphic)
        destination = "./files/"


def totGraphicsFound():
    totFound = len(graphicsFound)
    print("The total amount of graphic files in tex-files were:", totFound)


def main():
    makeLists("./files")
    print(files)
    createGraphicsFolder("./files")
    print(graphicsFolder)
    print(len(graphicsFolder))
    createTexFolder()
    moveGraphics()
    moveGraphicsToFolder()
    moveGraphicsNotIncluded()


main()
