import os
import shelve
import pprint

if __name__ == '__main__':
    # print(os.getcwd())
    # os.makedirs("/Users/hanyouquan/PycharmProjects/test/com/test2")
    # helloFile = open(os.getcwd()+"/test.py")
    # print(helloFile.read())
    # print(helloFile.readlines())

    # shelfFile = shelve.open('mydata')
    # cats = ['Zophie', 'Pooka', "Simon"]
    # shelfFile['cats'] = cats
    # print(shelfFile['cats'])
    # print(list(shelfFile.keys()))
    # print(list(shelfFile.values()))
    # shelfFile.close()

    # cats = [{'name': 'Pooka', 'desc': 'Simon'}, {'name': 'Pooka2', 'desc': 'Simon2'}]
    # print(pprint.pformat(cats))
    # fileObj = open('myCats.py', 'w')
    # fileObj.write('cats = '+pprint.pformat(cats) + '\n')
    # fileObj.close()

    # import myCats
    # print(myCats.cats)
    # print(myCats.cats[0]['name'])
    #
    # import send2trash
    #
    # baconFile = open('bacon.txt', 'a')
    # baconFile.write('hello world')
    # baconFile.close()
    # send2trash.send2trash('bacon.txt')

    for folderName, subfolders, fileNames in os.walk('/Users/hanyouquan/PycharmProjects/test'):
        print('The current folder is '+folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF '+folderName+": " + subfolder)
        for fileName in fileNames:
            print('FILE INSIDE ' + folderName + ": " + fileName)

        print("")


