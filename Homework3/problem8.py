
def process_MLK(filename):
    #create a new list
    new_string = []
    #create a new dictionary
    count = {}
    #create a temporary variable called read which will close after use.
    with open(filename) as read:
        #creat variable to read the file
        read = read.read()
        for i in read:
            #change everything to lower case
            i = i.lower()
            #We only want to keep letters, spaces, and new lines
            if (97 <= ord(i) <=122) or (65 <= ord(i) <=90) or (i == ' ') or (i == '\n'):
                new_string.append(i)
            else:
                continue
        #concatenating our results into a new string
        new_string = ''.join(new_string)
        #creating a list of all words in our file
        for i in new_string.split():
            #omitting all words from our list file
            if i in list_of_frequent_words('list.txt'):
                continue
            #putting together the dictionary of our new list of words
            else:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
        #using lambda to sort by values for the top 20 frequent words.
        for item in sorted(count.items(), key=lambda x: x[1], reverse=True)[0:20]:
            print(item)

#created a function to read the frequent words we are omitting from our file
def list_of_frequent_words(filename):
    words_list = []
    read = open(filename, 'r')
    read = read.read().split()
    for i in read:
        i = i.lower()
        words_list.append(i)
    return words_list

process_MLK('speech.txt')
