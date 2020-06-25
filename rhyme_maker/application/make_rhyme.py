from .Class import Corpus
from .Class import Vowel
from pykakasi import kakasi
import argparse
import sys
import gensim
import Levenshtein


def parser():
    parser = argparse.ArgumentParser(description='Process corpus.')
    parser.add_argument('corpus', help='corpus_data')
    args = parser.parse_args()
    return args


def search_rhyme(query_word, corpus, vowel):
    rhymes = ''
    query_vowel = vowel.word2vowel(query_word)
    query_yomi = vowel.word2yomi(query_word)
    # TODO word が [word]形式とword形式になっているので変換処理を書く
    results = []
    cnt = 0
    match_n = 2
    match_weight = 0.3
    cosine_weight = 1 - match_weight

    print(query_vowel)
    for word in corpus.word2vec.vocab:
        word_vowel = vowel.word2vowel(word)
        word_yomi = vowel.word2yomi(word)
        if query_vowel[-match_n:] == word_vowel[-match_n:]:
            word_match_score, scores = word_match_scorer(vowel, query_yomi, word_yomi)
            cosine_score = cosine_similarity(corpus, query_word, word)
            score = match_weight*word_match_score + cosine_weight*cosine_score
            # result = [word, word_vowel, score, scores]
            result = [word, word_vowel, score]
            # if query_wordがcorpus内にあれば
            # result = cosine_similarity(corpus, query_word, word)
            # result.append(word_vowel)
            results.append(result)
            rhymes = rhymes + word + '(' + word_vowel + ')' + ','
        cnt += 1
        if cnt == 10000:
            break
    results = sorted(results, key=lambda x:x[2], reverse=True) # scoreでソート
    print(results)
    return results

def word_match_scorer(vowel, query_yomi, word_yomi, vowel_weight=0.2, cons_weight=0.2, word_len_weight=0.1):
    # TODO とりあえず編集距離
    word_vowel = vowel.word2vowel(word_yomi)
    query_vowel = vowel.word2vowel(query_yomi)
    word_cons = vowel.yomi2cons(word_yomi)
    query_cons = vowel.yomi2cons(query_yomi)
    vowel_score = Levenshtein.distance(word_vowel, query_vowel)
    cons_score = Levenshtein.distance(word_cons, query_cons)
    word_len = len(word_yomi)
    word_match_score = word_len_weight*word_len - (vowel_weight*vowel_score + cons_weight*cons_score)
    scores = [vowel_score, cons_score, word_len, word_match_score]
    return word_match_score, scores
    # return vowel_score, scores

def cosine_similarity(corpus, query_word, target_word):
    # model.most_similar(positive=['姪', '男性'], negative=['女性'])
    cos_sim = corpus.word2vec.similarity(query_word, target_word)
    return cos_sim

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
