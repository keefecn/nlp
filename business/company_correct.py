# coding=utf-8
"""
公司名纠错
字符串相似串比较 
@requirement: python-Levenshtein  difflib
@author keefe
@date 2022-4-18 
"""


import Levenshtein


class CompanyCorrect(object):
    """ 公司名纠错 """
    companys = ("天津市康普瑞森商贸有限公司", "知观信息科技（香港）有限公司")

    def __init__(self, filename=None) -> None:
        pass

    @classmethod
    def correct(self, text):
        if text in self.companys:
            return text

        min, txt = self.calc_similay(text)
        print(f"{text} corrent: {txt}, min={min}");
        return txt

    @classmethod
    def calc_similay(self, text, res_num=1):
        """
        返回一个最相似结果, 距离最小
        @return int, str
        """
        min, res_txt = 100, ""
        for company in self.companys:
            diff = Levenshtein.distance(text, company)                    
            if diff < min:
                min, res_txt  = diff, company
            if min < 3:
                return min, res_txt   

        return min, res_txt


if __name__ == "__main__":
    texts = [""]

    CompanyCorrect().correct("司津市康普瑞森商贸有限公")
