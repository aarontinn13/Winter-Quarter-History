while True:                                                 #while loop that loop forever (While below is true...)
    try:                                                    #try to do below command knowing there is a potential for an error
        number =int(input("Please enter only a number: "))
        break                                               #if above holds true, we will end the loop
    except ValueError:                                      #this command happens when a value is not inputted
        print('You did not enter a number')
    except:                                                 #this value happens when any error occurs
        print('An unknown error occurred')
print('Thank you for entering a valid number!')             #once the loop has completed we will end

'''
A try statement may have more than one except clause for different exceptions. But at most one except clause will be executed.

Our next example shows a try clause, in which we open a file for reading, read a line from this file and convert this line into an integer. There are at least two possible exceptions:

an IOError
ValueError
Just in case we have an additional unnamed except clause for an unexpected error:
'''

import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

print('\n***************************************************************\n')

'''
ADDING THE EXCEPTION INSIDE OF THE FUNCTION INSTEAD
'''

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)

try:
    f()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")

print('\n***************************************************************\n')

'''
ADDING THE RAISE AT THE END TO PROPAGATE THE EXCEPTION TO THE CALLER
'''

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)
        raise

try:
    f()
except ValueError as e:
    print("got it :-) ", e)

print("Let's get on")

print('\n***************************************************************\n')

'''
CREATING YOUR OWN EXCEPTION CALL
'''

#raise NameError('gah ARE GOING TO GET YOU')

'''
Clean-up Actions (try ... finally)

So far the try statement had always been paired with except clauses. But there is another way to use it as well. The try statement can be followed by a finally clause. Finally clauses are called clean-up or termination clauses, because they must be executed under all circumstances, i.e. a "finally" clause is always executed regardless if an exception occurred in a try block or not. 
A simple example to demonstrate the finally clause:
'''

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)


print('\n***************************************************************\n')
'''
COMBINING TRY, EXCEPT AND FINALLY
'''

try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")


print('\n***************************************************************\n')
'''
else Clause

The try ... except statement has an optional else clause. An else block has to be positioned after all the except clauses. An else clause will be executed if the try clause doesn't raise an exception. 

The following example opens a file and reads in all the lines into a list called "text":
'''

import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()
    fh.close()
except IOError:
    print('cannot open', file_name)

if text:
    print(text[100])