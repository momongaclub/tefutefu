import Dictionary
import sys


def make_vowel_dictionary(vowel_dictionary, dictionary):
    with open(vowel_dictionary, 'w', encoding = 'euc_jp') as fp:
        for word, info in dictionary.dictionary.items():
            dictionary.vowel = ''
            dictionary.word = word
            dictionary.search_word_yomi()
            dictionary.word2vowel()
            info.insert(0, dictionary.word)
            info.append(dictionary.vowel)
            line = ""
            for index in info:
                line += index + ','
            line = line.rstrip(',')
            fp.write(line)
            fp.write('\n')
        # 新たなcsvファイルをfnameで読み込み
        # 辞書の単語と母音を回す
        # キーと値を同時に出して,リストで連結する. 連結したリストの最後尾に母音を追加する
        # 既存の辞書に追加する


def main():
    ipa_dicitionary = sys.argv[1]
    vowel_dictionary = sys.argv[2]
    dictionary = Dictionary.Dictionary()
    dictionary.load_dictionary(ipa_dicitionary)
    make_vowel_dictionary(vowel_dictionary, dictionary)

if __name__ == '__main__':
    main()
