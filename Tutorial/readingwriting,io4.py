'''
In our first example we want to show how to read data from a file.
The way of telling Python that we want to read from a file is to use
the open function. The first parameter is the name of the file we want
to read and with the second parameter, assigned to the value "r", we
state that we want to read from the file:
'''

fobj = open("readingwritingtest.txt", "r")

'''
The "r" is optional. An open() command with just a file name is 
opened for reading per default. The open() function returns a file object,
which offers attributes and methods. 
'''

fobj = open("readingwritingtest.txt")

'''
After we have finished working with a file, we have to close it again by 
using the file object method close(): 
'''

fobj.close()

'''
Now we want to finally open and read a file. The method rstrip() in the 
following example is used to strip off whitespaces (newlines included) 
from the right side of the string "line": 
'''

fobj = open("readingwritingtest.txt")
for line in fobj:
    print(line.rstrip())
fobj.close()





'''
Writing to a file is as easy as reading from a file. To open a file 
for writing we set the second parameter to "w" instead of "r". To 
actually write the data into this file, we use the method write() 
of the file handle object. 

Let's start with a very simple and straightforward example:
'''

fh = open("readingwritingtest.txt", "w")   #can add a '+' at the end of 'w' if file is not created
fh.write("To write or not to write\nthat is the question!\n")
fh.close()


'''
Especially if you are writing to a file, you should never forget 
to close the file handle again. Otherwise you will risk to end up 
in a non consistent state of your data. 
You will often find the with statement for reading and writing files. 
The advantage is that the file will be automatically closed after 
the indented block after the with has finished execution: 
'''

with open("readingwritingtest.txt", "w") as fh:
    fh.write("To write or not to write\nthat is the question!\n")


'''
Our first example can also be rewritten like this with the with statement:
'''


with open("readingwritingtest.txt") as fobj:
    for line in fobj:
        print(line.rstrip())


'''
Example for simultaneously reading and writing: 
'''

fobj_in = open("readingwritingtest.txt")
fobj_out = open("readingwritingtest.txt")
i = 1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

'''
Reading lines in a list
'''
poem = open("readingwritingtest.txt").readlines()
print(poem)
print(poem[1])

'''
Convenient way to read and print certain lines
'''
poem = open("ad_lesbiam.txt").read()
print(poem[16:34])

'''
In the following example we will open a file for reading
and writing at the same time. If the file doesn't exist,
it will be created. If you want to open an existing file
for read and write, you should better use "r+", because
this will not delete the content of the file.
'''
fh = open('colours.txt', 'w+')
fh.write('The colour brown')

# Go to the 12th byte in the file, counting starts with 0
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)

