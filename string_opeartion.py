# -*- coding: utf-8 -*-
'''
@summary: string operation
@since: 2020-3-14
@author: Keefe Wu
@see: 
'''  

import time


def get_costtime(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func_return = func(*args, **kwargs)
        
        end = time.time() + 0.1
        print(f'{func.__name__}() execute time: {end - start}s')

        return func_return

    return wrapper


@get_costtime
def get_uniq_cut(raw_txt, cut_set=[], prior=1):
    """ 
     原始文本raw_txt 从目标匹配词列表(match_words) 获取 命中词。多个命中情况下，取共同字串的最长匹配 match_set。
  如果传参cut_set不为空，则合并cut_set和match_set，
  :params: raw_txt
  :params: cut_set  
  :params: prior 合并策略：
       1~cutset优先, 则取处理1或处理3;  other 取最长子串：则取处理2
  :return:  list[]   
    """

    def _is_part_match(word, word_list):
        # 判断 word 是否 部分匹配 word_list中的词
        for w in word_list:
            if word in w:
                return True
        return False    
        
    def _get_long_match(match_set):   
        # 取最长字串
        match_set = sorted(match_set, key=lambda d: len(d), reverse=True)  # 按长度降序
        print(1, match_set)
        match_long_set = []  # 最长匹配
        for word in match_set:
            if not _is_part_match(word, match_long_set):
                match_long_set.append(word)
        print(2, match_long_set)                
        return match_long_set
                     
    match_words = ['中国', '中国电信', '电信', '湖南移动电信', '湖南电信']
    res_list = []  # 最终返回
    match_set = []  # 初始匹配
    match_set = [word for word in match_words if word in raw_txt]  # if word not in cut_set      
    if prior != 1:  
        match_set.extend(cut_set)  # cut_set处理2：统一取最长匹配
    match_set = _get_long_match(match_set)  # match_set取 最长匹配
    
    if prior == 1 and cut_set:  # cut_set处理3：cut_set优先   
        res_list.extend(cut_set)
        for word in match_set:
            if word not in cut_set: 
                res_list.append(word)
    else:
        res_list = match_set           
    print(res_list)
    return res_list


def judge_interval(list1, list2):
    """
            判断 list1 是否在 list2 区间内，list1/list2数值升序排列 
    :exaple1: 
    True:  list1=[2,4,5], list2=[1,4,6]
    Flase: list1=[2,4,5], list2=[3,4,6]  
    """
    len1 = len(list1)
    len2 = len(list2)
    spos_1 = list1[0]
    epos_1 = list1[len1-1]
    if spos_1 < list2[0] or epos_1 > list2[len2-1]:
        print('list1 not in list2')
        return False
    print('list1 in list2')
    return True

if __name__ == "__main__":
    cut_set = ['主席', '电信']  # 初始命中词
    raw_txt = '中国主席江泽民去伊朗看来自中国的湖南电信CEO。' 
    get_uniq_cut(raw_txt, cut_set, prior=1)   
    judge_interval([2,3,15], [1,4,5])