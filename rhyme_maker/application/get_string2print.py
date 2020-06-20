import os

def load_datas(data):
    data = str(data)
    with open('/home/mibayashi/programs/Tefu2/tefutefu/rhyme_maker/a', 'a') as fp:
        fp.write(data)
