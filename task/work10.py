import string
def get_dict_word_times(file):
    list_word_with_punctuation = file.read().split()
    list_word = [word.strip(string.punctuation).lower() for word in list_word_with_punctuation]
    set_word = set(list_word)
    return {word: list_word.count(word) for word in set_word}

def main():

    with open('demo.txt', 'r') as file:

        dict_word_times = get_dict_word_times(file)
    list_sorted_words = sorted(dict_word_times, key=lambda w: dict_word_times[w], reverse=True)
    for word in list_sorted_words:
        print("{} -- {} times".format(word, dict_word_times[word]))
main()   