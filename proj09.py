##############################################################
    #  Computer Project #9
    #
    #  Import string module
    #  Open file function
    #   Takes input for what file
    #       Try/ except to see if file opens
    #           returns file or returns open file
    #  Read file function
    #   Use for loop to iterate through file
    #       For loop to split line into a list of words
    #           add words to the set
    #   return the set
    #  Fill completions functions
    #   Iterate through set of words
    #       Add words and index, charcter to dictionary
    #   return dictionary
    #  Find completion function
    #   Check to see if prefix is empty if empty return empty set
    #   iterate through dictionary
    #       Add words with prefix to set
    #   return the set
    #  Main function
    #   While loop to keep prompting until # entered
    #       Call functions
    #       Prompt users for imputs
    #           initiate While loop
    #               Check to see set is empty
    #               Print error statemnets
    #           Final print statements 
    #  Display closing message
##############################################################

'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

def open_file():
    """
    Checks for if file is a vaild file

    Returns
    -------
    a file

    """
    while 1==1:
        file = input("\nInput a file name: ")
        try:
            #looks to see if the file can open 
            data_fp = open(file, encoding="utf-8")
            return data_fp
        except:
            #if the file is not found return the function to reask for file
            print("\n[Error]: no such file")
            return open_file()

def read_file(fp):
    """
    Reads the file and returns set of words in the file

    Parameters
    ----------
    fp : file
        The file that is opened and read.

    Returns
    -------
    word_set : set
        The set of words in the file.

    """
    #Splits the words in the line to create a list to iterate through
    #Then if the word is a letter and is bigger than one charcter it is added to the set
    word_set = set()
    for line in fp:
        for word in line.split():
            word = word.lower().strip(string.punctuation)
            if word.isalpha() and len(word) > 1:
                word_set.add(word)
    return word_set

def fill_completions(words):
    """
    Goes through the words in file and returns the words with that charcter index

    Parameters
    ----------
    words : set
        The set of words that are in the file.

    Returns
    -------
    word_D : dict
        A dictionary that has the index, charcter for the key and set of words as the value.

    """
    #Iterates through the set
    #Create a tuple as the key to the dictionary then create values
    word_D = {}
    for item in words:
        for i, ch in enumerate(item):
            tuplex = (i, ch)
            if tuplex not in word_D:
                word_D[tuplex] = set()
            word_D[tuplex].add(item)
    return word_D

def find_completions(prefix, word_D):
    """
    Finds the words based on prefixes inputted

    Parameters
    ----------
    prefix : str
        The prefix to search for in the words
    word_D : dict
        A dictionary that has the index, charcter for the key and set of words as the value.

    Returns
    -------
    prefix_s : set
        A set of words with the prefixes searched for.

    """
    #Check if prefixes entered is all lower case
    #if the prefix entered is a empty string return an empty set
    #If word has the same prefix add to set
    prefix_s = set()
    prefix = prefix.lower()
    if len(prefix) == 0:
        return prefix_s
    for i, ch in enumerate(prefix):
        prefix_words = word_D.get((i, ch), set())
        if i == 0:
            prefix_s = prefix_words
        else:
            prefix_s = prefix_s.intersection(prefix_words)
    return prefix_s

def main():  
    """
    Prints respective option    
    
    Returns
    -------
    None.
    
    """  
    #Call all necessary functions
    file = open_file()
    word_set = read_file(file)
    word_D = fill_completions(word_set)
    prefix_in = input("\nEnter a prefix (# to quit): ")
    #While the input is not equal to # it keeps running
    while prefix_in != "#":
        prefix_s = find_completions(prefix_in, word_D)
        #Error checking to see if set return is empty
        if len(prefix_s) == 0:
            print("\nThere are no completions.")
            prefix_in = input("\nEnter a prefix (# to quit): ")
        else:
            #Prints output
            prefix_sorted = sorted(prefix_s)
            print("\nThe words that completes {} are: {}".format(prefix_in, ", ".join(prefix_sorted)))
            prefix_in = input("\nEnter a prefix (# to quit): ")
    #Display closing message    
    print("\nBye")

if __name__ == '__main__':
    main()