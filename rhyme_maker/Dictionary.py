# -*- coding: utf-8 -*-
import sys
import re
import codecs
import argparse

YOMI = 10


class Dictionary():

    def __init__(self):
        self.dictionary = {}
        self.word = ''
        self.yomi = ''
        self.vowel = ''

    def load_dictionary(self, fname):
        # csv形式,表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        with codecs.open(fname, 'r', 'euc_jp', 'ignore') as fp:
            for line in fp:
                line = line.rstrip('\n')
                line = line.split(',')
                word = str(line[0])
                info = line[1:]
                self.dictionary[word] = info

    def search_word_yomi(self):
        info = self.dictionary[self.word]
        self.yomi = info[YOMI]

    def word2vowel(self):
        vowel = ''
        patterns = []
        # ッ,ィ
        a_pattern = re.compile("[アカサタナハマヤラワガザダバパャ]")
        i_pattern = re.compile("[イキシチニヒミリギジヅビピ]")
        u_pattern = re.compile("[ウクスツヌフムユルグズヅブプュ]")
        e_pattern = re.compile("[エケセテネヘメレゲゼデベペ]")
        o_pattern = re.compile("[オコソトノホモヨロヲゴゾドボポョ]")
        n_pattern = re.compile("[ン]")
        patterns.append(a_pattern)
        patterns.append(i_pattern)
        patterns.append(u_pattern)
        patterns.append(e_pattern)
        patterns.append(o_pattern)
        patterns.append(n_pattern)
        v_list = ['a', 'i', 'u', 'e', 'o', 'n']

        for w in self.yomi:
            cnt = 0
            for pattern in patterns:
                if pattern.match(w):
                    self.vowel = self.vowel + v_list[cnt]
                cnt += 1

    def search_similar_vowels(self):
        for word, info in self.dictionary.items():
            vowel = info[-1]
            if vowel == self.vowel:
                print(word, vowel)


def main():
    dictionary = Dictionary()
    fname = sys.argv[1]
    word = sys.argv[2]
    dictionary.load_dictionary(fname)
    dictionary.word = word
    dictionary.search_word_yomi()
    dictionary.word2vowel()
    dictionary.search_similar_vowels()


if __name__ == '__main__':
    main()
