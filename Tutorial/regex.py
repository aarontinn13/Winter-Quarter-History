import re

pattern = r'spam'

'''To determine if the beginning matches'''
if re.match(pattern, 'spam'):
    print('match')
else:
    print('No Match')

print
print('*********************2****************************')
print

'''matches anywhere'''
if re.search(pattern,'eggspamsausagespam'):
    print('match')
else:
    print('no match')

'''returns all of the substrings that match the pattern'''
print(re.findall(pattern,'eggspamsausagespam'))

print
print('*********************3****************************')
print

pattern = r'pam'

match = re.search(pattern, 'eggspamsausage')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

print
print('**********************4***************************')
print

'''To replace a string'''

str = 'My name is David. Hi David'

pattern = r'David'

newstr = re.sub(pattern, 'Amy', str)
print(newstr)

print
print('************************5*************************')
print

'''Meta characters: '.' matches any character other than new space'''

pattern = r'gr.y'

if re.match(pattern,'grey'):
    print('match1')
if re.match(pattern,'gray'):
    print('match2')
if re.match(pattern,'blue'):
    print('match3')

print
print('*************************6************************')
print

'''^matches start and end$'''
pattern = r'^gr.y$'

if re.match(pattern,'grey'):
    print('match 1')
if re.match(pattern,'gray'):
    print('match 2')
if re.match(pattern,'stingray'):
    print('match 3')

print
print('*********************7****************************')
print

'''matches a renage of stuff for one character'''
pattern = r'[A-Z][A-Z][0-9]'

if re.search(pattern, 'LS8'):
    print('match 1')
if re.search(pattern, 'LE3'):
    print('match 2')
if re.search(pattern, '1ab'):
    print('match 3')

print
print('**********************8***************************')
print

'''^Inverts to get anything other than specified'''
pattern = r'[^A-Z]'

if re.search(pattern, 'this is all quiet'):
    print('Match 1')
if re.search(pattern, 'AbCdEfG123'):
    print('Match 2')
if re.search(pattern, 'THISISALLSHOUTING'):
    print('Match 3')

print
print('************************9*************************')
print

'''* means 0 or more'''
pattern = r'egg(spam)*'

if re.match(pattern, 'egg'):
    print('Match 1')
if re.match(pattern, 'eggspamspamegg'):
    print('Match 2')
if re.match(pattern, 'spam'):
    print('Match 3')

print
print('************************10*************************')
print

'''+ means 1 or more'''
pattern = r'g+'

if re.match(pattern, 'g'):
    print('Match 1')
if re.match(pattern, 'ggggggggg'):
    print('Match 2')
if re.match(pattern, 'abc'):
    print('Match 3')

print
print('************************11*************************')
print

'''? means 0 or 1'''
pattern = r'ice(-)?cream'

if re.match(pattern, 'ice-cream'):
    print('Match 1')
if re.match(pattern, 'icecream'):
    print('Match 2')
if re.match(pattern, 'sausages'):
    print('Match 3')
if re.match(pattern, 'ice--ice'):
    print('Match 4')

print
print('************************12*************************')
print

'''can specify how many times with {from,to}'''
pattern = r'9{1,3}$'

if re.match(pattern, '9'):
    print('Match 1')
if re.match(pattern, '999'):
    print('Match 2')
if re.match(pattern, '9999'):
    print('Match 3')


print
print('************************13*************************')
print

'''a group can be specified by ()'''
pattern = r'egg(spam)*'

if re.match(pattern, 'egg'):
    print('Match 1')
if re.match(pattern, 'eggspamspamspamegg'):
    print('Match 2')
if re.match(pattern, 'spam'):
    print('Match 3')


print
print('************************13*************************')
print

'''group() can return a matching of all the groups'''

pattern = r'a(bc)(de)(f(g)h)i'

match = re.match(pattern, 'abcdefghijklmnop')
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

print
print('************************14*************************')
print

'''matches groups'''

pattern = r'(?P<first>abc)(?:def)(ghi)'

match = re.match(pattern, 'abcdefghijklmnop')
if match:
    print(match.group('first'))
    print(match.groups(0))

print
print('************************15*************************')
print

'''| matches or'''

pattern = r'gr(a|e)y'

match = re.match(pattern, 'gray')
if match:
    print('Match 1')

match = re.match(pattern, 'grey')
if match:
    print('Match 2')

match = re.match(pattern, 'griy')
if match:
    print('Match 3')

print
print('************************16*************************')
print

'''matches the expression of the group of that number'''

pattern = r'(.+)\1'

match = re.match(pattern, 'word word')
if match:
    print('Match 1')

match = re.match(pattern, '?!?!')
if match:
    print('Match 2')

match = re.match(pattern, 'abc cde')
if match:
    print('Match 3')

print
print('************************17*************************')
print

'''\d \s \w matches digits whitespaces and characters'''

pattern = r'(\D+\d)'

match = re.match(pattern, 'Hi 999')
if match:
    print('Match 1')

match = re.match(pattern, '1, 23, 456')
if match:
    print('Match 2')

match = re.match(pattern, '! $?')
if match:
    print('Match 3')

print
print('************************18*************************')
print

'''\A and \Z match beginning and end of a string,  matches empty string between \w and \W
\w characters and the beginning or end of the string'''

pattern = r'\b(cat)\b'

match = re.match(pattern, 'The cat sat!')
if match:
    print('Match 1')

match = re.match(pattern, 'We s>cat<tered?')
if match:
    print('Match 2')

match = re.match(pattern, 'We scattered.')
if match:
    print('Match 3')



