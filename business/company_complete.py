# coding=utf-8
"""
公司名补全，简称-全称
全称先切词，组装成 {公司名-地名 : 全名}。 停用词为公司、有限公司
简称也是先切词，再组装成公司名-地名，然后再去全称映射表中查找，若有，则映射为全名。

@requirement: 
@author keefe
@date 2022-4-18 
"""


class CompanyComplete(object):
    """ 公司名补全 """
    companys = ("天津市康普瑞森商贸有限公司", "易而观信息科技（上海）有限公司")

    def __init__(self, filename=None) -> None:
        pass

    def load_model():
        """ 加载模型 """

    def init_model(filename):
        """ 生成模型 """

    @classmethod
    def complete(self, text):
        pass


if __name__ == "__main__":

    texts = [""]
