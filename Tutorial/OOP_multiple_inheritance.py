'''
In the previous chapter of our tutorial, we have covered inheritance, or more specific
"single inheritance". As we have seen, a class inherits in this case from one class.
Multiple inheritance on the other hand is a feature in which a class can inherit attributes
and methods from more than one parent class. The critics point out that multiple inheritance
comes along with a high level of complexity and ambiguity in situations such as the
diamond problem. We will address this problem later in this chapter.

The widespread prejudice that multiple inheritance is something "dangerous" or "bad" is
mostly nourished by programming languages with poorly implemented multiple inheritance
mechanisms and above all by improper usage of it. Java doesn't even support multiple
inheritance, while C++ supports it. Python has a sophisticated and well-designed approach
to multiple inheritance.

A class definition, where a child class SubClassName inherits from the parent classes
BaseClass1, BaseClass2, BaseClass3, and so on, looks like this:
'''

'''
class SubclassName(BaseClass1, BaseClass2, BaseClass3, ...):
    pass
'''

'''
We want to introduce the principles of multiple inheritance with an example. For this 
purpose, we will implement to independent classes: a "Clock" and a "Calendar" class.
After this, we will introduce a class "CalendarClock", which is, as the name implies, 
a combination of "Clock" and "Calendar". CalendarClock inherits both from "Clock" and 
"Calendar". 
'''

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def set(self, hours, minutes, seconds=0):
        self._hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

'''
We decided against this implementation, because we added additional code for checking 
the plausibility of the time data into the set method. We call the set method from the 
__init__ method as well, because we want to circumvent redundant code. 
The complete Clock class: 
'''
""" 
The class Clock is used to simulate a clock.
"""

class Clock(object):

    def __init__(self, hours, minutes, seconds):
        """
        The parameters hours, minutes and seconds have to be
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self, hours, minutes, seconds):
        """
        The parameters hours, minutes and seconds have to be
        integers and must satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError("Minutes have to be integers between 0 and 59!")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59!")

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours,
                                                self.__minutes,
                                                self.__seconds)

    def tick(self):
        """
        This method lets the clock "tick", this means that the
        internal time will be advanced by one second.

        Examples:
        >x = Clock(12,59,59)
        >print(x)
            12:59:59
        >x.tick()
        >print(x)
            13:00:00
        >x.tick()
        >print(x)
            13:00:01
        """

        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

if __name__ == "__main__":
    x = Clock(23,59,59)
    print(x)
    x.tick()
    print(x)
    y = str(x)
    print(type(y))

print('\n**********************************************************************\n')

'''
We will now create a class "Calendar", which has lots of similarities to the previously 
defined Clock class. Instead of "tick" we have an "advance" method, which advances the 
date by one day, whenever it is called. Adding a day to a date is quite tricky. We have 
to check, if the date is the last day in a month and the number of days in the months 
vary. As if this isn't bad enough, we have February and the leap year problem. 

The rules for calculating a leap year are the following:
If a year is divisible by 400, it is a leap year.
If a year is not divisible by 400 but by 100, it is not a leap year.
A year number which is divisible by 4 but not by 100, it is a leap year.
All other year numbers are common years, i.e. no leap years.

As a little useful gimmick, we added a possibility to output a date either in British 
or in American (Canadian) style. 
'''

""" 
The class Calendar implements a calendar.   
"""

class Calendar():

    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        """
        The method leapyear returns True if the parameter year
        is a leap year, False otherwise
        """
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __init__(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        self.set_Calendar(d,m,y)

    def set_Calendar(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")

    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
                                                   self.__months,
                                                   self.__years)
        else:
            # assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
                                                   self.__days,
                                                   self.__years)

    def advance(self):
        """
        This method advances to the next date.
        """

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1

if __name__ == "__main__":
    x = Calendar(31,12,2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2012 was a leapyear:")
    x = Calendar(28,2,2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    x = Calendar(28,2,2013)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("1900 no leapyear: number divisible by 100 but not by 400: ")
    x = Calendar(28,2,1900)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2000 was a leapyear, because number divisible by 400: ")
    x = Calendar(28,2,2000)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("Switching to American date style: ")
    Calendar.date_style = "American"
    print("after applying advance: ", x)

print('\n**********************************************************************\n')

'''
At last, we will come to our multiple inheritance example. We are now capable of 
implementing the originally intended class CalendarClock, which will inherit from 
both Clock and Calendar. The method "tick" of Clock will have to be overridden. 
However, the new tick method of CalendarClock has to call the tick method of 
Clock: Clock.tick(self) 
'''

""" 
Modul, which implements the class CalendarClock.
"""

class CalendarClock(Clock, Calendar):
    """
        The class CalendarClock implements a clock with integrated
        calendar. It's a case of multiple inheritance, as it inherits
        both from Clock and Calendar
    """

    def __init__(self,day, month, year, hour, minute, second):
        Clock.__init__(self,hour, minute, second)
        Calendar.__init__(self,day, month, year)

    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour):
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)

if __name__ == "__main__":
    x = CalendarClock(31,12,2013,23,59,59)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)

    x = CalendarClock(28,2,1900,23,59,59)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)

    x = CalendarClock(28,2,2000,23,59,59)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)

    x = CalendarClock(7,2,2013,13,55,40)
    print("One tick from ",x, end=" ")
    x.tick()
    print("to ", x)