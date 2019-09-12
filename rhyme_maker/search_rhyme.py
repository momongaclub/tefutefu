import sys
import codecs

import Dictionary


def search_similar_vowels(target_word, vowel_dictionary):
        for word, vowel in vowel_dictionary.words2vowels.items():
            if vowel == vowel_dictionary.words2vowels[target_word]:
                line = word + ':' + vowel
                print(line)


def main():
    target_word = sys.argv[1]
    vowel_dictionary_fname = sys.argv[2]
    vowel_dictionary = Dictionary.Dictionary()
    vowel_dictionary.load_vowel_dictionary(vowel_dictionary_fname)
    search_similar_vowels(target_word, vowel_dictionary)

if __name__ == '__main__':
    main()
