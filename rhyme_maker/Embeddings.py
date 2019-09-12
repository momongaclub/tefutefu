# -*- coding: utf-8 -*-
import sys
import codecs

WORD = 0


class Embeddings():

    def __init__(self):
        self.embeddings = {}

    def load_embeddings(self, fname):
        with codecs.open(fname, 'r') as fp:
            info = fp.readline()
            for line in fp:
                line = line.rstrip('\n')
                line = line.rstrip(' ')
                line = line.split(' ')
                word = line.pop(WORD)
                embedding = line
                self.embeddings[word] = embedding


def main():
    fname = sys.argv[1]
    embeddings = Embeddings()
    embeddings.load_embeddings(fname)


if __name__ == '__main__':
    main()
