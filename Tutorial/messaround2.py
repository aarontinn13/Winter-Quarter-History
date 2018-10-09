import datetime

def elapsed_days(start):
    return (datetime.datetime.now() - start).days

start = datetime.datetime(2017, 11, 1)
print(elapsed_days(start))


start = datetime.datetime(2017, 1, 1)
print(elapsed_days(start))


print(elapsed_days(datetime.datetime(1, 1, 1)))


def convert_date(x):
    return datetime.datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime('%m-%d-%Y  %H:%M:%S')

def age(x):
    y = datetime.datetime.strptime(x, '%d/%m/%Y')
    start = datetime.datetime(y,11,1)
    return (datetime.datetime.now() - start).days

x = datetime.datetime.strftime()

age(x)