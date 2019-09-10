import re
import argparse
import codecs
import pykakasi

import Corpus


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


def yomi2vowel(yomi):
    vowel = ''
    v_list = ['a', 'i', 'u', 'e', 'o', 'n']
    for w in yomi:
        if w in v_list:
            vowel = vowel + w
    return vowel


class Corpus():

    def __init__(self):
        self.corpus = []
        self.word2vowel = {}

    def load_corpus(self, fname):
        with codecs.open(fname, 'r', 'utf-8', 'ignore') as fp:
            for sentence in fp:
                sentence = sentence.rstrip('\n')
                sentence = sentence.split(' ')
                self.corpus.append(sentence)

    def convert_vowel(self, corpus):
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("J", "a")
        kakasi.setMode("r", "Hepburn")
        kakasi.setMode("s", True)
        kakasi.setMode("C", True)
        conv = kakasi.getConverter()
        for sentence in corpus.corpus:
            for word in sentence:
                yomi = conv.do(word)
                yomi = str(yomi)
                vowel = yomi2vowel(yomi)
                self.word2vowel[word] = vowel


def main():
    args = parser()
    corpus = Corpus()
    corpus.load_corpus(args.corpus)
    corpus.convert_vowel(corpus)


if __name__ == '__main__':
    main()
