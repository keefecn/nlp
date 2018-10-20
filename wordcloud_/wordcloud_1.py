# -*- coding: utf-8 -*-

import os
import sys
from plot_img import plot_wordcloud 
 
cur_file_name = os.path.basename(sys.argv[0]).split(".")[0] 
sentences = '''Importance of relative word frequencies for font-size. 
With relative_scaling=0, only word-ranks are considered. 
With relative_scaling=1, a word that is twice as frequent will have twice the size. 
If you want to consider the word frequencies and not only their rank, relative_scaling around .5 often looks good.'''
plot_wordcloud(sentences, cur_file_name)
