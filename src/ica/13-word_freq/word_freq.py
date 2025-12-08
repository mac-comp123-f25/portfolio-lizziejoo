import string
from traceback import print_tb

def compute_frequencies(file):
    f = open(file, 'r')
    text = f.read()
    f.close()

    clean_words = []
    words = text.split()
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord)
    print(clean_words)

    for w in clean_words:
        print(w)


compute_frequencies("../TextFiles/alice.txt")