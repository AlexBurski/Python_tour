# find the longest word in a text and returns it.

import time


def find_longest_word(name_of_file):
    start = time.perf_counter()
    text = open(name_of_file + '.txt', 'r')
    words = text.read().split()
    result = max(words, key=len)
    text.close()

    return result, time.perf_counter() - start  # --> 0.0002409339999999982


print(find_longest_word('mytext'))


def longest_word():
    start = time.perf_counter()
    with open('mytext.txt', 'r') as file:
        word_file = file.read().split()
        max_len_word = ''
        for word in word_file:
            if '.' in word:
                word.replace('.', '')
            if len(word) > len(max_len_word):
                max_len_word = word
        return max_len_word, time.perf_counter() - start  # --> 0.00027025699999999597


print(longest_word())
