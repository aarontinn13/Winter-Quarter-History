import os

#starting with 'with' guarantees the file will close if it crashes
#mode='w' means we will overwrite anything that is inside of the file
#mode='a' means we will append to the file
#encoding='utf-8' means we will store our data in unicode
#as myFile means where we will store the information

with open('mydata.txt', mode='w', encoding='utf-8') as myFile:
    myFile.write('Some random text\nMore random text\nand some more random text')

#opening the file for reading:
#if we don't define the mode it will automatically read

with open('mydata.txt', encoding='utf-8') as myFile:
# can open to read files using these 3 methods read(), readline() and readlines()
# read() will read everything in one string up until a new line, for example the above will read 'Some random text'
# readline() will read everything in one string including new lines
# readlines() will return a list of everystring including new lines
    print(myFile.read())

#below tests to see if the file is closed or not, if a file used the 'with' command, it will automatically close
print(myFile.closed)

#returns the name of the file
print(myFile.name)

#returns the last used mode, 'r' stands for read
print(myFile.mode)

#rename a file inside the computer from x to y ( x , y )
os.rename('mydata.txt', 'mydata2.txt')

#remove a file (currently commented because I don't want to actually run)
#os.remove('mydata2.txt')

#create a directory (currently commented because I don't want to actually run)
#os.mkdir('mydir')

#make changes into a directory (currently commented because I don't want to actually run)
#os.chdir('mydir')

#get the current directory you are in
print(os.getcwd())

#move up one level in the directory
os.chdir('..')
print(os.getcwd()) #checking again where we are

#how to remove a directory, we must move one level above the directory to remove it just like above step.
#os.rmdir('mydir')

