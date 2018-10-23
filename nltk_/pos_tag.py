# -*- coding: utf-8 -*-

import nltk

# pos tag~词性标注：需要先下载语料库  punkt、averaged_perceptron_tagger

# word tokensize
text1 = nltk.word_tokenize('It is a pleasure day today')
# pos tag
tagged = nltk.pos_tag(text1)
# ner
entities = nltk.chunk.ne_chunk(tagged)

print(text1)
print(tagged)
print(entities)