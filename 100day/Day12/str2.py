# @author: huhao
# @file: str2.py
# @time: 2019/7/23 7:13
# @Document：https://www.python.org/doc/
# @desc:

'''拆分长字符串'''
import re


def main():
    poem = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
    sentence_list = re.split(r"[，。, .]", poem)

    '''
    ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
    '''
    while "" in sentence_list:
        sentence_list.remove("")
        print(sentence_list)

    '''
     ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
    '''


if __name__ == '__main__':
    main()
