"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order
"""


def reverse_sentence(x):
    list_sentence = x.split(" ")
    new_sentence = list_sentence[::-1]
    reversed_sentence = " ".join(new_sentence)
    print(reversed_sentence)

sentence = "My name is Michele"
reverse_sentence(sentence)
