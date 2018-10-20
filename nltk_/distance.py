# -*- coding: utf-8 -*-

import nltk
from nltk.metrics import *
# from nltk.metrics.distance import edit_distance
'''
edit_distance, binary_distance,
jaccard_distance, masi_distance,
interval_distance, custom_distance,
presence, fractional_presence
'''
                                          
# 编辑距离：用以判断短文本相似度
print(edit_distance('replace', 'relation'))

# jaccard距离：两个集合交集的相似度  (X交Y)/(X并Y)
X = set([10, 20, 30, 40])
Y = set([20, 30, 60])
print('jaccard_distance=%.4f' % jaccard_distance(X, Y))

# binary_distance
print('binary_distance=%.4f' % binary_distance(X, Y))
