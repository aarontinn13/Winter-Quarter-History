import os
#how to read strings line by line

with open('mydata2.txt', encoding='utf=8') as myFile:

    linenum = 1

    while True:

        line = myFile.readline()

        if not line: #if there is no data
            break

        print(linenum, ':', line, end='')
        print('line', linenum)
        wordList = line.split()
        print("number of Words: ", len(wordList))
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        avgnumchars = charCount/len(wordList)

        print('avg word length: {:.2}'.format(avgnumchars))

        linenum += 1