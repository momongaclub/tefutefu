from .Class import Corpus
from .Class import Vowel
from pykakasi import kakasi
import argparse
import sys
import gensim


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


def search_rhyme(query_word, corpus, vowel):
    rhymes = ''
    query_vowel = vowel.word2vowel(query_word)
    # TODO word が [word]形式とword形式になっているので変換処理を書く
    results = []
    cnt = 0
    for word in corpus.word2vec.vocab:
        word_vowel = vowel.word2vowel(word)
        if query_vowel == word_vowel:
            # if query_wordがcorpus内にあれば
            result = cosine_similarity(corpus, query_word, word)
            result.append(word_vowel)
            results.append(result)
            rhymes = rhymes + word + '(' + word_vowel + ')' + ','
        cnt += 1
        if cnt == 60000:
            break
    results = sorted(results, key=lambda x:x[1], reverse=True)
    print(results)
    return results
    # return rhymes

def cosine_similarity(corpus, query_word, target_word):
    # model.most_similar(positive=['姪', '男性'], negative=['女性'])
    cos_sim = corpus.word2vec.similarity(query_word, target_word)
    result = [target_word, cos_sim]
    return result

def get_query_word(query_word):
    return query_word


def main(request):
    args = parser()
    query_word = request.POST['input_text']
    vowel = Vowel.Vowel()
    corpus = Corpus.Corpus()
    # corpus.load_corpus('/home/mibayashi/programs/tefutefu/rhyme_maker/application/data/tohoku_wiki_embeddings/entity_vector.model.sample', f_type='txt')
    corpus.load_corpus('/home/mibayashi/programs/tefutefu/rhyme_maker/application/data/tohoku_wiki_embeddings/entity_vector.model.pkl', f_type='pkl')
    rhymes = search_rhyme(query_word, corpus, vowel)
    return rhymes


if __name__ == '__main__':
    main()
