import re
'''
Can use the findall method to find all examples of the given pattern.
'''

t="A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)
print(mo)

'''
Another Example...
'''

courses = "Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: 12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
items = re.findall("[^:]*:[^;]*;?", courses)
print(items)
items = re.findall("([^:]*):([^;]*;?)", courses)
print(items)

'''
Alternations

In our introduction to regular expressions we had introduced 
character classes. Character classes offer a choice out of a 
set of characters. Sometimes we need a choice between several 
regular expression. It's a logical "or" and that's why the 
symbol for this construct is the "|" symbol. 

In the following example, we check, if one of the cities 
London, Paris, Zurich, Konstanz Bern or Strasbourg appear in
a string preceded by the word "location":
 '''

str = "Course location is London or Paris!"
mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
if mo:
    print(mo.group())


'''
Compiling Regular Expressions

If you want to use the same regexp more than once in a script, it might be a good idea to use a regular expression object, i.e. the regex is compiled. 

The general syntax:

re.compile(pattern[, flags])
compile returns a regex object, which can be used later for searching and replacing. The expressions behaviour can be modified by specifying a flag value. 

Abbreviation	Full name	Description
re.I	    re.IGNORECASE	Makes the regular expression case-insensitive

re.L	    re.LOCALE	    The behaviour of some special sequences like \w, 
                            \W, \b,\s, \S will be made dependant on the current 
                            locale, i.e. the user's language, country also.

re.M	    re.MULTILINE	^ and $ will match at the beginning and at the end 
                            of each line and not just at the beginning and the 
                            end of the string

re.S	    re.DOTALL	    The dot "." will match every character plus the newline

re.U	    re.UNICODE	    Makes \w, \W, \b, \B, \d, \D, \s, \S dependent on 
                            Unicode character properties

re.X	    re.VERBOSE	    Allowing "verbose regular expressions", i.e. whitespace
                            are ignored. This means that spaces, tabs, and carriage 
                            returns are not matched as such. If you want to match a 
                            space in a verbose regular expression, you'll need to 
                            escape it by escaping it with a backslash in front of 
                            it or include it in a character class.
# are also ignored, except when in a character class or preceded by an non-escaped backslash. Everything following a "#" will be ignored until the end of the line, so this character can be used to start a comment.


Compiled regular objects usually are not saving much time, because Python internally compiles AND CACHES regexes whenever you use them with re.search() or re.match(). The only extra time a non-compiled regex takes is the time it needs to check the cache, which is a key lookup of a dictionary.

A good reason to use them is to separate the definition of a regex from its use. 
'''


regex = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
address = "BBC News Centre, London, W12 7RJ"
compiled_re = re.compile(regex)
res = compiled_re.search(address)
print(res)


'''
Can split a string into a list of substrings
'''

law_courses = "Let reverence for the laws be breathed by every American mother to the lisping babe that prattles on her lap. Let it be taught in schools, in seminaries, and in colleges. Let it be written in primers, spelling books, and in almanacs. Let it be preached from the pulpit, proclaimed in legislative halls, and enforced in the courts of justice. And, in short, let it become the political religion of the nation."
print(law_courses.split())

line = "James;Miller;teacher;Perl"
print(line.split(";"))

mammon = "The god of the world's leading religion. The chief temple is in the holy city of New York."
print(mammon.split(" ",3))

mammon = "The god  \t of the world's leading religion. The chief temple is in the holy city of New York."
print(mammon.split(" ",5))

'''
We can prevent the separation of empty strings by using None 
as the first argument. Now split will use the default behaviour,
i.e. every substring consisting of connected whitespace 
characters will be taken as one separator:
'''

print(mammon.split(None,5))

'''
If we want to only split strings without including white spaces or special characters!
'''

metamorphoses = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"
re.split("\W+",metamorphoses)


lines = ["surname: Obama, prename: Barack, profession: president", "surname: Merkel, prename: Angela, profession: chancellor"]
for line in lines:
    print(re.split(",* *\w*: ", line)[1:])


'''
Search and Replace with Sub
'''


str = "yes I said yes I will Yes."
res = re.sub("[yY]es","no", str)
print(res)