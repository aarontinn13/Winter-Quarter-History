'''
Standard Classes as Base Classes

It's possible to use standard classes - like int, float, dict or lists - as base classes as well.

We extend the list class by adding a push method:
'''
class Plist(list):

    def __init__(self, l):
        list.__init__(self, l)

    def push(self, item):
        self.append(item)


if __name__ == "__main__":
    x = Plist([3,4])
    x.push(47)
    print(x)

'''
This means that all the previously introduced binary and extended assignment operators exist in the "reversed" version as well:
__radd__
__rsub__
__rmul__
...
and so on
'''

"""

The class "Ccy" can be used to define money values in various currencies. A Ccy instance has the string attributes 'unit' (e.g. 'CHF', 'CAD' od 'EUR' and the 'value' as a float. 
A currency object consists of a value and the corresponding unit.



"""


class Ccy:
    # 1 EUR equal below amounts...
    currencies = {'CHF': 1.0821202355817312,
                  'CAD': 1.488609845538393,
                  'GBP': 0.8916546282920325,
                  'JPY': 114.38826536281809,
                  'EUR': 1.0,
                  'USD': 1.11123458162018}

    def __init__(self, value, currency = 'EUR'):
        self.value = value
        self.currency = currency

    def Conversecurrency(self):
        return self.value / Ccy.currencies[self.currency]

    def __add__(self, other):
        l = self.Conversecurrency() + other.Conversecurrency()
        return Ccy(l / Ccy.currencies[self.currency], self.currency)

    def __str__(self):
        return str(self.Conversecurrency())

    def __repr__(self):
        return str(self.value) + ", '" + self.currency + "')"

v1 = Ccy(23.43, "EUR")
v2 = Ccy(19.97, "USD")
print(v1 + v2)
#32.89 EUR
