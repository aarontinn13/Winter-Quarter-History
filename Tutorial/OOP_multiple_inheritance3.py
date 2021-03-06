class Clock(object):

    def __init__(self,hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def set(self,hours, minutes, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def tick(self):
        """ Time will be advanced by one second """
        if self.__seconds == 59:
            self.__seconds = 0
            if (self.__minutes == 59):
                self.__minutes = 0
                if self.__hours==23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

    def display(self):
        print("%d:%d:%d" % (self.__hours, self.__minutes, self.__seconds))

    def __str__(self):
        return "%2d:%2d:%2d" % (self.__hours, self.__minutes, self.__seconds)

x = Clock()
print(x)
x.set(0,0,1)
for i in range(10000):
    x.tick()
print(x)
x.display()

print('\n************************************************************************\n')


class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, day=1, month=1, year=1900):
        self.__day = day
        self.__month = month
        self.__year = year

    def leapyear(self,y):
        if y % 4:
	    # not a leap year
           return 0;
        else:
           if y % 100:
               return 1;
           else:
               if y % 400:
                  return 0
               else:
                  return 1;

    def set(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def get():
        return (self, self.__day, self.__month, self.__year)

    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1


    def __str__(self):
       return str(self.__day)+"/"+ str(self.__month)+ "/"+ str(self.__year)

if __name__ == "__main__":
   x = Calendar()
   print(x)
   x.advance()
   print(x)
   x.advance()
   print(x)


print('\n*************************************************************************\n')



class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, day=1, month=1, year=1900):
        self.__day = day
        self.__month = month
        self.__year = year

    def leapyear(self,y):
        if y % 4:
	   # not a leap year
           return 0;
        else:
           if y % 100:
               return 1;
           else:
               if y % 400:
                  return 0
               else:
                  return 1;

    def set(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year


    def get():
        return (self, self.__day, self.__month, self.__year)
    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1


    def __str__(self):
       return str(self.__day)+"/"+ str(self.__month)+ "/"+ str(self.__year)

if __name__ == "__main__":
   x = Calendar()
   print(x)
   x.advance()
   print(x)
