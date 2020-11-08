# -*- coding: utf-8 -*-

import jieba
from plot_img import plot_wordcloud, read_file

 
def get_word_list(raw_file, encoding='gbk'):
    text = read_file(raw_file, encoding)
    cut = jieba.cut(text)  # 分词
    word_lst = ' '.join(cut)
    return word_lst


if __name__ == "__main__":
    # word_list = get_word_list('tlbb.txt')  # religion
    word_list = get_word_list(r'E:\project\project-tools\blind_date\tmp.txt')  # religion
    print(len(word_list))
    # print(word_list)
    plot_wordcloud(word_list)
