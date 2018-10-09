class Square:

    def __init__(self, height='0', width='0'):
        self.height = height
        self.width = width

    @property
    def height(self):
        print('Retrieving the Height')

        return self.height

    @height.setter
    def height(self, value):

        if value.isdigit():
            self.height = value
        else:
            print('Please only enter numbers for height')

    @property
    def width(self):
        print('Retrieving the width')

        return self.width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.width = value
        else:
            print('Please only enter numbers for width')

    def getArea(self):
        return int(self.width) * int(self.height)

def main():

    asquare = Square()

    height = input('Enter Height: ')
    width = input('Enter Width: ')

    asquare.height = height
    asquare.width = width

    print('Height: ', asquare.height)
    print('Width: ', asquare.width)
    print('Area: ', asquare.getArea())

main()