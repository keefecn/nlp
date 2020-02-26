#coding: utf-8  
"""
@summary: plot utils
@since: 2018-10-22
@author: Keefe Wu
@see: 
""" 
from matplotlib import pyplot as plt
from wordcloud import WordCloud 

def read_file(filename, encoding='utf-8'):
    text = ''
    with open(filename, 'r', encoding=encoding) as f:
        text = f.read()  # readlines
    return text

def plot_wordcloud(word_list, save_img_name=None):
       
    font = r'C:\Windows\Fonts\FZSTK.TTF'
    # stopword = ['xa0']  # 设置停止词
    stopword = read_file('stopword.txt')
    wc = WordCloud(
                   background_color='white',
                   width=1800,
                   height=1200,
                   max_words=50,
                   # max_font_size=60,
                   # margin=5,
                   font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
                   stopwords=stopword,
                   )
    wc_result = wc.generate(word_list)               
    # wc_result = wc.fit_words(word_list)                   
    plt.imshow(wc_result)  # 用plt显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.show()
    if save_img_name:
        wc_result.to_file(save_img_name + '.png')  # 保存图片
    else:
        wc_result.to_file('new.png')

    
if __name__ == "__main__":
    pass    
