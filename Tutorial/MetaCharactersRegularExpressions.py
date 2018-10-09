import re
'''
We know that backslash \ escapes a character string
but to keep raw you can use:
'''
raw_string = r'this is using the backslash \n which produces no new line'

'''
Use the re.search function to find patterns, fir must import re module, like above!
'''
if re.search('this', raw_string):
    print('We have found it!')
else:
    print('We have not found it!')

'''
If we want to find any character we use '.'
For example if we wanted to find any three letter word ending in '-at' we look for:
'.at'
'''

'''
Character classes are categorized in brackets [xyz], i.e. x or y or z
d[oiu]g will search for dog, dig or dug
'''

dog = r'd[oiu]g'

'''
To access a larger range of meta characters: use '-'
[a-z] to access letters a through z
[A-Z] to access letters A through Z
[1-10] to access numbers 1 through 10
[^a-z] anything BUT letter a through z
'''

'''
You might have realized that it can be quite cumbersome to construe 
certain character classes. A good example is the character class, 
which describes a valid word character. These are all lower case and 
uppercase characters plus all the digits and the underscore, corresponding 
to the following regular expression: r"[a-zA-Z0-9_]" 

The special sequences consist of "\\" and a character from the following list:
\d	Matches any decimal digit; equivalent to the set [0-9].
\D	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
\s	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
\w	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
\W	Matches the complement of \w.
\b	Matches the empty string, but only at the start or end of a word.
\B	Matches the empty string, but not at the start or end of a word.
\\	Matches a literal backslash.
'''

'''
re.match(x,y) will match only at the beginning of a string as opposed to re.search(x,y) that searches the entire string.
'''

'''
re.search(^x,y) will also return the beginning of every string and every line of every string in an iteration with the use of the third parameter re.M.
'''

'''
a question mark denotes the the preceding character is optional
if we want the optional doge we can write
d[oiu]ge?
'''

'''
Quantifiers:
* at the end of a class means 0 or more occurences
+ at the end of a class means 1 or more occurences
{beginning,end} means beginning to end times for example:
r"^[0-9]{4,5} [A-Z][a-z]{2,}" says, beginning of a string 4 to 5 digits followed by a space then a capital letter and at least 2 lowercase letters following that.
'''


'''
Can use the following functions for more use of indexing...
'''
mo = re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
print(mo.group())
print(mo.span())
print(mo.start())
print(mo.end())
print(mo.span()[0])
print(mo.span()[1])


mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(1,2))

'''
A very intuitive example are XML or HTML tags. E.g. let's assume we have a file 
(called "tags.txt") with content like this:

<composer>Wolfgang Amadeus Mozart</composer>
<author>Samuel Beckett</author>
<city>London</city>

We want to rewrite this text automatically to

composer: Wolfgang Amadeus Mozart
author: Samuel Beckett
city: London

The following little Python script does the trick. The core of this script is 
the regular expression. This regular expression works like this: It tries to 
match a less than symbol "<". After this it is reading lower case letters until 
it reaches the greater than symbol. Everything encountered within "<" and ">" has 
been stored in a back reference which can be accessed within the expression by 
writing \1. Let's assume \1 contains the value "composer". When the expression has 
reached the first ">", it continues matching, as the original expression had 
been "<composer>(.*)</composer>":
'''

#fh = open("tags.txt")
#for i in fh:
#     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
#     print(res.group(1) + ": " + res.group(2))


s = "Sun Oct 14 13:47:03 CEST 2012"
expr = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
x = re.search(expr,s)
print(x.group('hours'))
print(x.group('minutes'))
print(x.start('minutes'))
print(x.end('minutes'))
print(x.span('seconds'))