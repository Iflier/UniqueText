# -*- coding:utf-8 -*-
"""
Dec: 比较json文件的这一行和下一行来去除重复的行，前提是被比较的文件已经排序了
Created on: 2018.01.25
Author: Iflier
"""
print(__doc__)

import difflib

with open('new.json', 'r', encoding='utf-8') as file, open('newest.json', 'a',
                                                           encoding='utf-8') as file2:
    while True:
        line = file.readline()
        if line:
            file2.write(line)
        else:
            break
        nextLine = file.readline()
        if nextLine:
            seq = difflib.SequenceMatcher(None, line, nextLine)
            if seq.ratio() < 0.8:
                # 相似度，数值越大，越相似
                file2.write(nextLine)
        else:
            break
