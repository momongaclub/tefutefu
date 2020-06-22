import sys
import pykakasi


class Vowel():

    def __init__(self):
        self.vowel = ''
        self.yomi = ''

    def word2yomi(self, word):
        # TODO  正式に決まり次第音韻表記へ変更する
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
        kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
        kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
        kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
        # kakasi.setMode("s", True) # add space, default: no separator
        # kakasi.setMode("C", True) # capitalize, default: no capitalize
        converter = kakasi.getConverter()
        yomi = converter.do(word)
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
    word = 'プール学校'
    vowel = Vowel()
    yomi = vowel.word2yomi(word)
    print(yomi)




if __name__ == '__main__':
    main()
