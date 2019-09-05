# -*- coding: utf-8 -*-
import sys
import codecs
import argparse


def load_dictionary(fname):
    # csv形式,表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    # 読みの部分を取得する. 読みの部分はカタカナで表記されて言え
    # ひとまず表層形で一致するかで計算量がまに合うか考える
    with codecs.open(fname, 'r', 'euc_jp', 'ignore') as fp:
        dictionary = {}
        for line in fp:
            line = line.rstrip('\n')
            line = line.split(',')
            word = str(line[0])
            info = line[1:]
            dictionary[word] = info
    return dictionary


def search_word(dictionary, word):
    print(dictionary[word])
    return 0


def main():
    fname = sys.argv[1]
    word = str(sys.argv[2])
    dictionary = load_dictionary(fname)
    search_word(dictionary, word)
    return 0


if __name__ == '__main__':
    main()
