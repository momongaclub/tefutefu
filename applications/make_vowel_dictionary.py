import argparse
import pykakasi

import Dictionary

SPACE = ' '


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('wiki_corpus', help='corpus_data')
    parser.add_argument('vowel_dictionary', help='output_dictionary')
    args = parser.parse_args()
    return args

def make_vowel_dictionary(vowel_dictionary, corpus):
    with open(vowel_dictionary, 'w', encoding='utf-8') as fp:
        for word, vowel in corpus.word2vowel.items():
            fp.write(word + SPACE + vowel)
            fp.write('\n')

def main():
    args = parser()
    dictionary = Dictionary.Dictionary()
    dictionary.load_sentences(args.wiki_corpus)
    dictionary.extract_words()
    dictionary.make_vowel_dict(args.vowel_dictionary)


if __name__ == '__main__':
    main()
