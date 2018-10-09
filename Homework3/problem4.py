def process_file(filename):
    #make variable to open the file
    read = open(filename, 'r')
    #create a list for our words etc.
    words = []
    #create a list to count the lines
    number_lines = []
    #create a variable to read everyline individually
    read = read.readlines()
    #enumerate through every line while reading every word and storing both in their lists
    for i, j in enumerate(range(len(read))):
        words.extend(read[j].split())
        number_lines.append(i + 1)
    #sort the list
    words.sort()
    #return the final products
    return filename, words, max(number_lines)
    read.close()

print(process_file('test.txt'))
