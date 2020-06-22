import sys
import argparse
from Class import Corpus


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    parser.add_argument('save_pkl', help='save_pkl_file')
    args = parser.parse_args()
    return args


def main():
    args = parser()
    corpus = Corpus.Corpus()
    corpus.load_corpus(args.corpus, f_type='binary')
    corpus.save_pkl(args.save_pkl)


if __name__ == '__main__':
    main()
