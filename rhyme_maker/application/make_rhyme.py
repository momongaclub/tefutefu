from .Class import Corpus
from .Class import Vowel
from pykakasi import kakasi
import argparse
import sys


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


def search_rhyme(query_word, corpus, vowel):
    rhymes = ''
    query_vowel = vowel.word2vowel(query_word)
    print('query_word:', query_word, 'query_vowel:', query_vowel)
    # TODO word が [word]形式とword形式になっているので変換処理を書く
    for word in corpus.word2vec.vocab:
        word_vowel = vowel.word2vowel(word)
        if query_vowel == word_vowel:
            print('word:', word, 'vowel:', word_vowel)
            rhymes = rhymes + word + '(' + word_vowel + ')' + ','
    return rhymes


def get_query_word(query_word):
    return query_word


def main(request):
    args = parser()
    query_word = request.POST['input_text']
    vowel = Vowel.Vowel()
    corpus = Corpus.Corpus()
    corpus.load_corpus('/home/mibayashi/programs/tefutefu/rhyme_maker/application/data/tohoku_wiki_embeddings/entity_vector.model.sample',
                       f_type='txt')
    rhymes = search_rhyme(query_word, corpus, vowel)
    return rhymes


if __name__ == '__main__':
    main()
