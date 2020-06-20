import sys
import pykakasi

class Vowel():

    def __init__(self):
        self.vowel = ''
        self.yomi = ''

    def word2yomi(self, word):
        yomis = pykakasi.kakasi().convert(word)
        yomi = ''
        # TODO  正式に決まり次第音韻表記へ変更する
        for y in yomis:
            yomi += y['hepburn']
        return yomi

    def word2vowel(self, word):
        yomi = Vowel().word2yomi(word)
        vowel = ''
        # TODO 正規表現 使いましょう
        v_list = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O', 'n']
        for w in yomi:
            if w in v_list:
                vowel = vowel + w
        return vowel


def main():
    kakasi = pykakasi.kakasi()

main()
