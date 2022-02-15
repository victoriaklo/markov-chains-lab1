"""Generate Markov text from text files."""

from random import choice

input_path = 'green-eggs.txt'

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents

# open_and_read_file(input_path)


def make_chains(text_string):
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

    chains = {}

    # your code goes here
    input_text = open_and_read_file(input_path)

    words = input_text.split()

    # Loops over the words in the list of words, 
    # making sure you can access the word at i, and i+1
    # for i in range(len(words) - 2):

    #     # make input_text[i], input_text[i + 1] a key
    #     key_tuple = (words[i], words[i + 1])

    #     # check if chains has this key, else return 0
    #     chains.get(key_tuple, 0)

    #     initial_list = [words[i + 2]]

    #     chains[key_tuple] = initial_list

    # #create an empty list
    # values_list = []

    # if key_tuple in chains:
    #     # append word to the list
    #     initial_list.append(words[i + 1])
    #     chains[key_tuple] = values_list
    # # else:
    #     #initialize that list and put your word into it
    #     chains[key_tuple] = values_list
    #     values_list.append(words[i + 1])


    # To set a stop point, append None to the end of our word list.

    words.append(None)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    return chains


print(make_chains(input_path))


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
