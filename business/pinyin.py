# coding=utf-8
"""
中文转拼音
@requirement: xpinyin
@author keefe
@date 2022-4-18 
@refer 每天分享一个好用的Python库-xpinyin  https://learnku.com/articles/58577
"""

from xpinyin import Pinyin

p = Pinyin()
# 默认分隔符 -
print(p.get_pinyin("上海"))

s1 = p.get_pinyin("上海", tone_marks='marks')

s2 = p.get_pinyin("上海", tone_marks='numbers')
print(s1, s2)
