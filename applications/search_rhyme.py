import sys
import argparse
import codecs
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter, attrgetter


import Dictionary
import Embeddings


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('target_word', help='search_word')
    parser.add_argument('vowel_dictionary_fname',
                        help='to_use_search_vowel_dictionary')
    parser.add_argument('embeddings_fname', help='word_embeddings')
    args = parser.parse_args()
    return args


def search_similar_vowels(target_word, vowel_dictionary, embeddings):
    words = {}
    for word, vowel in vowel_dictionary.words2vowels.items():
        if vowel == vowel_dictionary.words2vowels[target_word]:
            line = word + ':' + vowel
            # print(line)
            try:
                target_vec = []
                target_vec.append(embeddings.embeddings[target_word])
                match_vec = []
                match_vec.append(embeddings.embeddings[word])
                result = cosine_similarity(target_vec, match_vec)
                # print(word, result)
                words[result[0][0]] = word
            except:
                print(line)
                pass
    print('\n')
    words = sorted(words.items())
    for word, cos in enumerate(words):
        print(cos, word)


def main():
    args = parser()
    vowel_dictionary = Dictionary.Dictionary()
    embeddings = Embeddings.Embeddings()
    embeddings.load_embeddings(args.embeddings_fname)
    vowel_dictionary.load_vowel_dictionary(args.vowel_dictionary_fname)
    search_similar_vowels(args.target_word, vowel_dictionary, embeddings)


if __name__ == '__main__':
    main()
