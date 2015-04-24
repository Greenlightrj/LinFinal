from string import ascii_lowercase, punctuation
import numpy as np

def get_word_list(language = 'english'):
    """
    Reads the file for the language and returns it as a list of words
    also returns the appropriate language alphabet
    """

    fiel = open(language + '.txt', 'r')
    txt = fiel.read()

    if language == 'english' or language =='vigenere':
        alphabet = ascii_lowercase
        for dot in punctuation:
            txt = txt.replace(dot, " ")
        txt = txt.lower()
        wordlist = txt.split()

    elif language == 'german':
        # i tried to do the alphabet but the program freaks out at funny characters even in comments
        for dot in punctuation:
            txt = txt.replace(dot, " ")
        txt = txt.lower()
        wordlist = txt.split()

    elif language == 'klingon':
        alphabet = ['a', 'b', 'ch', 'D', 'e', 'gh', 'H', 'I', 'j', 'l', 'm', 'n', 'ng', 'o', 'p', 'q', 'Q', 'r', 'S', 't' 'tlh', 'u', 'v', 'w', 'y', "'"]
        wordlist = txt.split()

    return (alphabet, wordlist)

def createdict(alphabet):
    """
    creates a dictionary with keys as every combination of two letters in the 'letters' alphabet
    """
    squares = {}
    for letter in alphabet:
        for letter2 in alphabet:
            combo = (letter, letter2)
            squares[combo] = 0
    return squares


def filldict(words, dictionary):
    """
    takes text as a string and fills the dictionary with the number of occurrences of each letter pair
    """
    for word in words:
        if len(word) == 2:
            dictionary[(word[0], word[1])] += 1
        elif len(word)>2:
            for i in range(0, len(word)-2):
                dictionary[(word[i], word[i+2])] += 1
    return dictionary

def makematrix(letters, dictionary):
    """
    takes dictionary and creates a numpy adjacency matrix
    """
    matrix = np.zeros((len(letters), len(letters)))
    for (key, value) in dictionary.items():
        matrix[letters.find(key[0]), letters.find(key[1])] = value
    return matrix

if __name__ == '__main__':
    (alphabet, wordlist) = get_word_list()
    squares = createdict(alphabet)
    squares = filldict(wordlist, squares)
    A = makematrix(alphabet, squares)


