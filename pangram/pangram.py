import string

def is_pangram(sentence):
    ascii_all = string.ascii_lowercase
    sentence = sentence.lower()
    return all(letter in sentence for letter in ascii_all)
