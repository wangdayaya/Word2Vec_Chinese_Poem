# -*- coding: utf-8 -*-
import os
import jieba
from flask import json


def main():

   # 将 json 目录中的每首诗词分别进行单字和单词的切分
    output = open('poem.txt', 'w', encoding='utf-8')
    for root, dirs, files in os.walk('json'):
        for i,file in enumerate(files):
            print('{}/{}'.format(i,len(files)))
            filename = os.path.join(root, file)
            print(filename)
            with open(filename, 'r', encoding='utf8') as fp:
                lines = json.load(fp)
                for i,line in enumerate(lines):
                    s = ''.join(line['paragraphs'])
                    for word in jieba.cut(s):
                        if word and word!=':' and word!='，' and word!='。'and word!='？':
                            output.write(word + ' ')
                    output.write('\n')
                    for word in list(s):
                        if word and word!=':' and word!='，' and word!='。'and word!='？':
                            output.write(word + ' ')
                    output.write('\n')
    output.close()



if __name__ == '__main__':
    main()
