class Animal:
    def __init__(self, birthtype='Unknown', appearance='Unknown', blooded='Unknown'):
        self.birthtype = birthtype
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthtype(self):
        return self.__birthtype

    @birthtype.setter
    def birthtype(self, birthtype):
        self.__birthtype = birthtype

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return 'A {} is {} it is {} it is {}'.format(type(self).__name__, self.birthtype, self.appearance, self.blooded)


class mammal(Animal):
    def __init__(self, birthtype='born alive', appearance='hair or fur', blooded='warm blooded', nurseyoung=True):
        Animal.__init__(self, birthtype, appearance, blooded, )
        self.__nurseyoung = nurseyoung

    @property
    def nurseyoung(self):
        return self.__nurseyoung

    @nurseyoung.setter
    def nurseyoung(self, nurseyoung):
        self.__nurseyoung = nurseyoung

    def __str__(self):
        return super().__str__() + " and it is {} they nurse" \
                                   "their young".format(self.nurseyoung)


class Reptile(Animal):
    def __init__(self, birthtype='born in an egg or born alive', appearance='dry scales', blooded='cold blooded'):
        Animal.__init__(self, birthtype, appearance, blooded)

    def sumall(self, *args):
        sum = 0
        for i in args:
            sum += i

        return sum

def getbirthtype(theObject):
    print('the {} is {}'.format(type(theObject).__name__, theObject.birthtype))


def main():
    animal1 = Animal('born alive')
    print(animal1.birthtype)

    print(animal1)

    print()

    mammal1 = mammal()

    print(mammal1.birthtype)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseyoung)
    print(mammal1)
    print()

    reptile1 = Reptile()
    print(reptile1.birthtype)

    print(reptile1)
    print()

    print('Sum : {}'.format(reptile1.sumall(1,2,3,4,5)))

    getbirthtype(mammal1)
    getbirthtype(reptile1)






main()
