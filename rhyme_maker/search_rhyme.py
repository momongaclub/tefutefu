import sys
import codecs


def load_word2vowel(fname):
    word2vowel = {}
    with codecs.open(fname, 'r', 'utf-8', 'ignore') as fp:
        for line in fp:
            line = line.rstrip('\n')
            line = line.split(' ')
            word = line[0]
            vowel = line[1]
            word2vowel[word] = vowel
    return word2vowel

def search_similar_vowels(target_word, word2vowel):
        for word, vowel in word2vowel.items():
            if vowel == word2vowel[target_word]:
                line = word + ':' + vowel
                print(line)

def yomi2vowel(yomi):
    vowel = ''
    v_list = ['a', 'i', 'u', 'e', 'o', 'n']
    for w in yomi:
        if w in v_list:
            vowel = vowel + w
    return vowel


def main():
    target_word = sys.argv[1]
    vowel_dictionary = sys.argv[2]
    word2vowel = load_word2vowel(vowel_dictionary)
    search_similar_vowels(target_word, word2vowel)

if __name__ == '__main__':
    main()
