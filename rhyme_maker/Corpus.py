import re
import argparse
import codecs
import pykakasi


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


class Corpus():

    def __init__(self):
        self.sentences = []
        self.word2vowel = {}
        self.words = []

    def load_sentences(self, fname):
        with codecs.open(fname, 'r', 'utf-8', 'ignore') as fp:
            for sentence in fp:
                sentence = sentence.rstrip('\n')
                sentence = sentence.split(' ')
                self.sentences.append(sentence)

    def extract_words(self):
        for sentence in self.sentences:
            for word in sentence:
                self.words.append(word)


def main():
    args = parser()
    corpus = Corpus()
    corpus.load_sentences(args.corpus)
    corpus.extract_words()


if __name__ == '__main__':
    main()
