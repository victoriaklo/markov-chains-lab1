"""Generate Markov text from text files."""

#from random module import choice function
from random import choice

# moved file path bc of control flow
input_path = 'green-eggs.txt'


def open_and_read_file(file_path): # funtion opens the text file and reads it, returns the whole file vs. line by line
    """Take file path as string; return text as string. 

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string): # defines the function that takes text_string as parameter
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {} #create an empty dictionary

    
    input_text = open_and_read_file(input_path) #calls previous funtion and assigns to variable, in this
    #case is the green eggs text file 
    
    #splits all words from input_text
    words = input_text.split()

    # append None to the end of our word list to prevent keyError
    words.append(None)


    for i in range(len(words) - 2): #for every element in the index up to the last 2
        key_tuple = (words[i], words[i + 1]) # assign the tuple values to the index and index +1 in words(list)
        value = words[i + 2] # the value of the key_tuple is assigned to words at index + 2

        if key_tuple not in chains: #if the key_tuple is not already in the dictionary
            chains[key_tuple] = [] #assign the key_tuple to empty list

        chains[key_tuple].append(value) #append the value to the chain dictionary

    return chains


# print(make_chains(input_path))


def make_text(chains): #define function that makes new text out of the dictionary above
    """Return text from chains."""

    # your code goes here

    # start with random choice to start link
    start_key = choice(list((chains.keys())))
    
    words = [start_key[0], start_key[1]] # place-holding list for tuple index 0 and 1 in start_key(needs to be list to be updated) 
    word = choice(chains[start_key]) # picking a random choice from the values list at the start_key
    
    # print(start_key.value())
    # random_start = chains.keys()

    while word is not None:
        # iterate through all words until you reach the end
        start_key = (start_key[1], word) #made new start_key tuple out of second word in start_key followed by random word 
        words.append(word) #append random word to words as next second word 
        word = choice(chains[start_key]) # picking a random choice from the values list at the start_key

    # returns the list of words + ' ' between all the words
    return ' '.join(words)

print(make_text(make_chains(input_path)))


# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
