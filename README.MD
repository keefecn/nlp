
## Brief
* nltk：natural language toolkit
* wordcloud: 词云
* wordcut: 分词
* gensim: get text simialry，文本相似度
* business: 常用业务

## nltk
* Install: pip install nltk
* corpus download
```
import nltk
nltk.download()
```

* Usage: 包括词干提取、词性标注、距离计算、语法/语义/情感分析

## wordcloud
* Install: pip install wordcloud,matplotlib
* Usage:


## gensim
* Install: pip install gensim
* Usage:


## business

* company_complete 公司名补全，场景是公司名简称转全称。实现技术是分词+全名映射。示例：山东移动 ->  中国山东移动有限公司
* company_correct  公司名纠错，场景是OCR纠错。实现技术是计算字符串距离。示例：山东移动有力公司 -> 山东移动有限公司
* address_parse    中国地址解析，场景智能快递地址。实现技术。
* pinyin  中文转拼音