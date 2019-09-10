import argparse
import pykakasi

import Dictionary
import Corpus

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
    wiki_corpus = Corpus.Corpus()
    wiki_corpus.load_corpus(args.wiki_corpus)
    wiki_corpus.convert_vowel(wiki_corpus)
    make_vowel_dictionary(args.vowel_dictionary, wiki_corpus)



if __name__ == '__main__':
    main()
