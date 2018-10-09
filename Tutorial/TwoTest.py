# file two.py
import OneTest
from Test1.mod1 import *

func()

print("top-level in two.py")
OneTest.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")