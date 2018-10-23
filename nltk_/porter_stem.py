# -*- coding: utf-8 -*-

import nltk
from nltk.stem import PorterStemmer

# porter stremmer 词干提取 
sStemmer = PorterStemmer()
print(sStemmer.stem('working'))
