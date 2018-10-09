import os

import sys

def main():

    user_input = sys.argv[1]
    if os.path.exists(user_input):
        user_input = os.path.abspath(user_input)
        #print(user_input)
        walk_path(user_input)
    else:
        print("Folder or file not found")




def walk_path(start, layer=0):
    print("  " * layer + os.path.basename(start) + "/")
    for item in os.listdir(start):
        item = os.path.join(start,item)
        if os.path.isfile(item) and '.git' not in item:
            print("  " * (layer + 1) + os.path.basename(item))
        if os.path.isdir(item) and '.git' not in item:
            walk_path(item, layer + 1)

if __name__ == '__main__':

    main()
