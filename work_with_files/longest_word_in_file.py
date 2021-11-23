# find the longest word in a text and returns it.

def find_longest_word(name_of_file):
    text = open(name_of_file + '.txt', 'r')
    words = text.read().split()
    return max(words, key=len)


print(find_longest_word('mytext'))


def longest_word():
    with open('mytext.txt', 'r') as file:
        word_file = file.read().split()
        max_len_word = ''
        for word in word_file:
            if '.' in word:
                word.replace('.', '')
            if len(word) > len(max_len_word):
                max_len_word = word
        return max_len_word


print(longest_word())
