# -*- coding: utf-8 -*-
"""
@summary: jieba cutword
@since: 2020-2-25
@author: Keefe Wu
@see: Python jieba分词知识整合  https://blog.csdn.net/qq_22022063/article/details/78987531
  https://blog.csdn.net/codejas/article/details/80356544
""" 

import jieba


def cutword_demo():
    """ 
         分词
          三种切割模式  (lcut返回列表，cut返回生成器）
    1. 精简模式(默认模式)，cut_all=False, 返回一个列表类型的结果，没有冗余  
    2. 全模式，使用 'cut_all=True' 指定.把文本中所有可能的词语都扫描出来，有冗余       
    3. 搜索引擎模式，在精确模式基础上，对长词再次切分 
    """
    seg_str = "好好学习，天天向上，吴启福好南。他来到了网易杭研大厦"
    print("raw string: {}".format(seg_str))
    print(jieba.lcut(seg_str))
    print(jieba.lcut(seg_str, cut_all=True))
    print(jieba.lcut_for_search(seg_str)) 
    print('---------') 
    jieba.add_word('好南')  # 向字典中添加新词
    print(jieba.cut(seg_str))
    print("/".join(jieba.cut(seg_str)))
    print("/".join(jieba.cut(seg_str, cut_all=True)))  
    print("/".join(jieba.cut_for_search(seg_str)))  
    

def self_dict():
    """ 自定义词典 """
    import jieba.posseg as pseg  # 
    jieba.load_userdict("userdict.txt")  # 加载用户词典     
    jieba.add_word('石墨烯')
    jieba.add_word('凱特琳')
    jieba.del_word('自定义词')
     
    test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
    )
    words = jieba.cut(test_sent)
    print('jieba.cut: {}'.format('/'.join(words)))
    print("="*40)

         
def posseg():
    """ 词性标注 """
    import jieba.posseg as pseg
    test_sent = ("李小福是创新办主任也是云计算方面的专家")
    result = pseg.cut(test_sent)    
    for w in result:
        print(w.word, "/", w.flag, ", ", end=' ')

        
def keyword_extract_by_wordfreq(content, topK=20):
    """ 基于 TF-IDF 算法的关键词抽取 """
    import jieba.analyse
    jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")  # 停用词
    jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");    
    tags = jieba.analyse.extract_tags(content, topK=topK)     
    print(",".join(tags))            


def keyword_extract_by_textrank(content, topK=20):
    """ 基于 TextRank 算法 的关键词抽取 
    基本思想:
    1. 将待抽取关键词的文本进行分词
    2. 以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
    3. 计算图中节点的PageRank，注意是无向带权图
    """
    import jieba.analyse.textrank

    tags = jieba.analyse.textrank(content, topK=topK)     
    print(",".join(tags))  


if __name__ == "__main__":
    from calc_wordfreq import get_txt
    filename = r"F:\ebook2\社科类电子书\My\国学典籍\其它\古典文学\四大名著TXT\1sg.txt"
    txt = get_txt(filename)
    cutword_demo()
    # self_dict()
    # posseg()
    # keyword_extract_by_wordfreq(txt)
    # keyword_extract_by_textrank(txt)    
