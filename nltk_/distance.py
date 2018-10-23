# -*- coding: utf-8 -*-

import nltk
from nltk.metrics import *

'''
from nltk.metrics.distance  import (edit_distance, binary_distance,
                                  jaccard_distance, masi_distance,
                                  interval_distance, custom_distance,
                                  presence, fractional_presence)
'''
                                          
# 编辑距离：用以判断短文本相似度
print(edit_distance('replace', 'relation'))

# jaccard距离：两个集合交集的相似度  (X交Y)/(X并Y)
X = set([10, 20, 30, 40])
Y = set([20, 30, 60])
print('jaccard_distance=%.4f' % jaccard_distance(X, Y))

# binary_distance
print('binary_distance=%.4f' % binary_distance(X, Y))


def absolute_distance():
    # 欧氏距离~绝对距离
    import numpy as np
     
    x = np.random.random(10)
    y = np.random.random(10)
    
    # solution1
    dist1 = np.linalg.norm(x - y)
     
    # solution2
    dist2 = np.sqrt(np.sum(np.square(x - y)))  
     
    print('x', x)
    print('y', y)
    print('dist1', dist1)
    print('dist2', dist2)    
