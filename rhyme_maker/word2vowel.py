import sys
import re

def word2vowel(word):
    vowel = ''
    patterns = []
    a_pattern = re.compile("[あかさたなはまやらわがざだば]")
    i_pattern = re.compile("[いきしちにひみりぎじづび]")
    u_pattern = re.compile("[うくすつぬふむゆるぐずづぶ]")
    e_pattern = re.compile("[えけせてねへめれげぜでべ]")
    o_pattern = re.compile("[おこそとのほもよろをごぞどぼ]")
    patterns.append(a_pattern)
    patterns.append(i_pattern)
    patterns.append(u_pattern)
    patterns.append(e_pattern)
    patterns.append(o_pattern)

    v_list = ['a','i','u','e','o']

    for w in word:
        cnt = 0
        for pattern in patterns:
            if pattern.match(w):
                vowel = vowel + v_list[cnt]
            cnt += 1
    return vowel

def main():
    word = str(sys.argv[1])
    vowel = word2vowel(word)
    print(vowel)

if __name__ == '__main__':
    main()
