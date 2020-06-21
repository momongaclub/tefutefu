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

    def load_corpus(self, fname, f_type='pkl'):
        if f_type == 'pkl':
            self.word2vec = KeyedVectors.load(fname)
        elif f_type == 'binary':
            self.word2vec = KeyedVectors.load_word2vec_format(fname, binary=True)
        else:
            print('error')

    def save_pkl(self, fname):
        corpus.word2vec.save(fname+'pkl', pickle_protocol=1)


def main():
    args = parser()
    corpus = Corpus()
    corpus.load_corpus(args.corpus)


if __name__ == '__main__':
    main()
