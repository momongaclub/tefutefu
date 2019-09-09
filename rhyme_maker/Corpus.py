import sys
import argparse


class Corpus():

    def __init__(self):
        self.corpus = []

    def load_corpus(self, fname):
        with open(fname, 'r') as fp:
            for sentence in fp:
                sentence = sentence.rstrip('\n')
                sentence = sentence.split(' ')
                self.corpus.append(sentence)

def main():
    corpus = Corpus()


if __name__ == '__main()__':
    main()
