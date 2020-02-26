# -*- coding: utf-8 -*-
"""
@summary: english cutword
@since: 2020-2-25
@author: Keefe Wu
@see: https://blog.csdn.net/codejas/article/details/80356544
""" 


def get_txt(filename, encoding='utf-8', is_replace_space=False):
    text = ''
    try:
        with open(filename, 'r', encoding=encoding) as f:
            text = f.read()  
    except UnicodeDecodeError as e:
        with open(filename, 'r', encoding='gbk') as f:
            text = f.read()     
    if is_replace_space:
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            text = text.replace(ch, " ")  # 将文本中特殊字符替换为空格
    print("{} len={}".format(filename, len(text)))
    return text




def calc_wordfreq(words, top_nums=20):
    def _change_word_sg(word):  # 三国
        rword = word
        excludes = {"将军","却说","二人","不可","荆州","不能","如此","商议","如何"}
        if word in excludes:
            return ''
        if word == "诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word == "关公" or word == "云长":
            rword = "关羽"
        elif word == "玄德" or word == "玄德曰":
            rword = "刘备"
        elif word == "孟德" or word == "丞相":
            rword = "曹操"
        return rword        
        
    counts = {}  # 通过键值对的形式存储词语及其出现的次数    
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        word = _change_word_sg(word)
        if word:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
    
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    print("words={}".format(len(items)))
    
    for i in range(top_nums):
        word, count = items[i]
        print("{0:<2} {1:<3} {2:>3}".format(i, word, count))


def do_stat_wordfreq(txt, is_zh=True, top_nums=20):
    """
          从文本文件中，统计词频
    """    
    words = []
    if is_zh:
        import jieba
        words = jieba.lcut(txt)  # 使用精确模式对文本进行分词
    else:
        words = txt.split()  # 对字符串进行分割，获得单词列表
    calc_wordfreq(words, top_nums=top_nums)

    
if __name__ == "__main__":
    filename = r"F:\ebook2\社科类电子书\My\国学典籍\其它\古典文学\四大名著TXT\1sg.txt"
    txt = get_txt(filename, is_replace_space=True)
    do_stat_wordfreq(txt)
