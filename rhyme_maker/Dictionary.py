# -*- coding: utf-8 -*-
import sys
import re
import codecs
import argparse
import pykakasi

import Corpus


SPACE = ' '
WORD = 0
VOWEL = 1


class Dictionary(Corpus.Corpus):

    def __init__(self):
        Corpus.Corpus.__init__(self)
        self.words2vowels = {}

    def load_vowel_dictionary(self, fname):
        with codecs.open(fname, 'r', 'utf-8', 'ignore') as fp:
            for word_and_vowel in fp:
                word_and_vowel = word_and_vowel.rstrip('\n')
                word_and_vowel = word_and_vowel.split(' ')
                word = word_and_vowel[WORD]
                vowel = word_and_vowel[VOWEL]
                self.words2vowels[word] = vowel

    def make_vowel_dict(self, fname):

        def yomi2vowel(yomi):
            vowel = ''
            v_list = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O', 'n']
            for w in yomi:
                if w in v_list:
                    vowel = vowel + w
            return vowel

        def convert_vowel():
            kakasi = pykakasi.kakasi()
            kakasi.setMode("H", "a")
            kakasi.setMode("K", "a")
            kakasi.setMode("J", "a")
            kakasi.setMode("r", "Hepburn")
            kakasi.setMode("s", True)
            kakasi.setMode("C", True)
            conv = kakasi.getConverter()
            for word in self.words:
                yomi = conv.do(word)
                yomi = str(yomi)
                vowel = yomi2vowel(yomi)
                self.words2vowels[word] = vowel

        convert_vowel()
        with open(fname, 'w', encoding='utf-8') as fp:
            for word, vowel in self.words2vowels.items():
                fp.write(word + SPACE + vowel)
                fp.write('\n')


def main():
    corpus_fname = sys.argv[1]
    output_vowel_dict_fname = sys.argv[2]
    input_vowel_dict_fname = sys.argv[3]
    dictionary = Dictionary()
    dictionary.load_sentences(corpus_fname)
    dictionary.extract_words()
    dictionary.make_vowel_dict(output_vowel_dict_fname)
    dictionary.load_vowel_dictionary(input_vowel_dict_fname)


if __name__ == '__main__':
    main()
