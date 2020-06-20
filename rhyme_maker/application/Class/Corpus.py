import argparse
from gensim.models import KeyedVectors


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


class Corpus():

    def __init__(self):
        self.word2vec = []

    def load_corpus(self, fname):
        self.word2vec = KeyedVectors.load_word2vec_format(fname, binary=True)


def main():
    args = parser()
    corpus = Corpus()
    corpus.load_corpus(args.corpus)
    print(corpus.word2vec.most_similar('[森羅万象]'))


if __name__ == '__main__':
    main()
