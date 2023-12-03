#!/usr/bin/python3

# import argparse
import opencc
import os
import math
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
# templates_dir = os.path.join(current_dir, "templates")
# tmp_dir = os.path.join(current_dir, "tmp")

# 繁转简
converter = opencc.OpenCC('t2s')


# 获取gb2312
gb2312 = []
with open(os.path.join(current_dir, 'gb2312.txt'), "r", encoding='utf-8') as f:
    for line in f.readlines():
        gb2312.append(line.strip())


# 读入字的对数频率，例如：
# 的 -1.4254
char_freq = {}
with open(os.path.join(current_dir, 'char_freq.txt'), encoding='utf-8') as f:
    for line in f.readlines():
        char, freq = line.split()
        if char in gb2312:
            char_freq[char] = float(freq)



# 读入字的发音和多音字的对数频率，例如：
# 的	di	-3.4828
char_pinyin = []
with open(os.path.join(current_dir, 'char_pinyin.txt'), encoding='utf-8') as f:
    for line in f.readlines():
        char, pinyin, freq = line.split()
        if char in char_freq:
            char_pinyin += [(char, pinyin, float(freq) + char_freq[char])]

# 以字加读音的对数频率排序
char_pinyin.sort(key=lambda item: item[2], reverse=True)

# 读入字的笔画，例如：
# 的	pszhhpzn
# char_strokes = {}
# with open(os.path.join(current_dir, 'char_strokes.txt'),
#           encoding='utf-8') as f:
#     for line in f.readlines():
#         if len(line) > 1 and line[0] != '#':
#             char, strokes = line.split()
#             char_strokes[char] = strokes[:5]

# # 输出关于字的信息
# with open('char_info.js', 'w', encoding='utf-8') as f:
#     f.write('var char_info = [\n')
#     for char, pinyin, freq in char_pinyin[:args.count]:
#         f.write('["%c","%s","%s",%.4f],\n' % (char, pinyin, char_strokes[char][:5], freq))
#     f.write('];\n')

aaa = {}
for char, pinyin, freq in char_pinyin:
    if not aaa.get(pinyin):
        aaa[pinyin] = []
    aaa[pinyin].append((char, freq))

# print(aaa)
bbb = {}
for k, v in aaa.items():
    result = 0
    for item in v:
        result += math.exp(item[1])
    bbb[k] = math.log(result)

bbb2 = sorted(bbb.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
with open("test.txt", "w") as f:
    f.write(str(bbb2))
print([x[0] for x in bbb2])

yuns = {}
for item in bbb2:
    item_py = item[0]
    if len(item_py) > 2:
        if item_py[0:2] in ["zh", "ch", "sh"]:
            if not yuns.get(item_py[2:]):
                yuns[item_py[2:]] = []
            yuns[item_py[2:]].append(item_py[0:2])
        elif item_py[0:1] in ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's', 'y', 'w']:
            if not yuns.get(item_py[1:]):
                yuns[item_py[1:]] = []
            yuns[item_py[1:]].append(item_py[0:1])
        else:
            if not yuns.get(item_py):
                yuns[item_py] = []
            yuns[item_py].append("0")
    elif item_py[0:1] in ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's', 'y', 'w']:
        if not yuns.get(item_py[1:]):
            yuns[item_py[1:]] = []
        yuns[item_py[1:]].append(item_py[0:1])
    else:
        if not yuns.get(item_py):
            yuns[item_py] = []
        yuns[item_py].append("0")

yuns = list(set(yuns))
print(yuns)


yun0s = ["a", "o", "e", ]

shengs = [
    'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh',
    'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w'
]
yuns = {
    "a": [
        '0', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 's',
        'sh', 't', 'w', 'y', 'z', 'zh'
    ],
    "ai": [
        '0', 'b', 'c', 'ch', 'd', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 's', 'sh',
        't', 'w', 'z', 'zh'
    ],
    "an": [
        '0', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r',
        's', 'sh', 't', 'w', 'y', 'z', 'zh'
    ],
    "ang": [
        '0', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r',
        's', 'sh', 't', 'w', 'y', 'z', 'zh'
    ],
    "ao": [
        '0', 'b', 'c', 'ch', 'd', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's',
        'sh', 't', 'y', 'z', 'zh'
    ],
    "o": ['0', 'b', 'f', 'l', 'm', 'p', 'w', 'y'],
    "ong":
    ['c', 'ch', 'd', 'g', 'h', 'k', 'l', 'n', 'r', 's', 't', 'y', 'z', 'zh'],
    "ou": [
        '0', 'c', 'ch', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's',
        'sh', 't', 'y', 'z', 'zh'
    ],
    "e": [
        '0', 'c', 'ch', 'd', 'g', 'h', 'k', 'l', 'm', 'n', 'r', 's', 'sh', 't',
        'y', 'z', 'zh'
    ],
    "ei":
    ['0', 'b', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'sh', 'w', 'z', 'zh'],
    "en": [
        '0', 'b', 'c', 'ch', 'f', 'g', 'h', 'k', 'm', 'n', 'p', 'r', 's', 'sh',
        'w', 'z', 'zh'
    ],
    "eng": [
        '0', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r',
        's', 'sh', 't', 'w', 'z', 'zh'
    ],
    "er": ['0'],
    "i": [
        'b', 'c', 'ch', 'd', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'sh', 't',
        'x', 'y', 'z', 'zh'
    ],
    "ia": ['d', 'j', 'l', 'q', 'x'],
    "ian": ['b', 'd', 'j', 'l', 'm', 'n', 'p', 'q', 't', 'x'],
    "iang": ['j', 'l', 'n', 'q', 'x'],
    "iao": ['b', 'd', 'j', 'l', 'm', 'n', 'p', 'q', 't', 'x'],
    "ie": ['b', 'd', 'j', 'l', 'm', 'n', 'p', 'q', 't', 'x'],
    "in": ['b', 'j', 'l', 'm', 'n', 'p', 'q', 'x', 'y'],
    "ing": ['b', 'd', 'j', 'l', 'm', 'n', 'p', 'q', 't', 'x', 'y'],
    "iong": ['j', 'q', 'x'],
    "iu": ['d', 'j', 'l', 'm', 'n', 'q', 'x'],
    "u": [
        'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
        'r', 's', 'sh', 't', 'w', 'x', 'y', 'z', 'zh'
    ],
    "ua": ['g', 'h', 'k', 'sh', 'zh'],
    "uai": ['ch', 'g', 'h', 'k', 'sh', 'zh'],
    "uan": [
        'c', 'ch', 'd', 'g', 'h', 'j', 'k', 'l', 'n', 'q', 'r', 's', 'sh', 't',
        'x', 'y', 'z', 'zh'
    ],
    "uang": ['ch', 'g', 'h', 'k', 'sh', 'zh'],
    "ue": ['j', 'q', 'x', 'y'],
    "ui": ['c', 'ch', 'd', 'g', 'h', 'k', 'r', 's', 'sh', 't', 'z', 'zh'],
    "un": [
        'c', 'ch', 'd', 'g', 'h', 'j', 'k', 'l', 'q', 'r', 's', 'sh', 't', 'x',
        'y', 'z', 'zh'
    ],
    "uo":
    ['c', 'ch', 'd', 'g', 'h', 'k', 'l', 'n', 'r', 's', 'sh', 't', 'z', 'zh'],
    "v": ['l', 'n'],
    "ve": ['l', 'n'],
}
pinyins = aaa.keys()
# print(len(yuns.keys()))

# print(len(aaa.keys()))
