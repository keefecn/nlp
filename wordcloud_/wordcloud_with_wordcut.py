# -*- coding: utf-8 -*-

import jieba
from plot_img import plot_wordcloud 

 
def get_word_list(raw_file):
    text = (open(raw_file, 'r', encoding='utf-8')).read()
    cut = jieba.cut(text)  # 分词
    word_lst = ' '.join(cut)
    return word_lst


if __name__ == "__main__":
    word_list = get_word_list('religion.txt')
    plot_wordcloud(word_list)
