from Class import Corpus
from Class import Vowel
from pykakasi import kakasi
import argparse
import sys


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args

def search_rhyme(quey_word, corpus, vowel):
    query_vowel = vowel.word2vowel(quey_word)
    print(query_vowel)
    # TODO word が [word]形式とword形式になっているので変換処理を書く
    for word in corpus.word2vec.vocab:
        word_vowel = vowel.word2vowel(word)
        if query_vowel == word_vowel:
            print(word)

def main():
    query_word = '働き蟻'
    args = parser()
    vowel = Vowel.Vowel()
    corpus = Corpus.Corpus()
    corpus.load_corpus(args.corpus)
    #print(vars(corpus.word2vec))
    search_rhyme(query_word, corpus, vowel)



if __name__ == '__main__':
    main()
