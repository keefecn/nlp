# -*- coding: utf-8 -*-
'''
@summary: AFINN sentiment analysis in Python: Wordlist-based approach for sentiment analysis. 
@since: 2018-10-22
@author: Keefe Wu
@see: 
'''  

from afinn import Afinn

def afinn_score(text, language='en', emoticons=True):
    afinn = Afinn(language=language, emoticons=True)
    score = afinn.score(text)
    print(score)
    return score

afinn_score('This is utterly excellent!')
afinn_score('This is utterly excellent!', 'da')   # Danish
afinn_score('Hvis ikke det er det mest afskyelige flueknepperi...', 'da') 
afinn_score('I saw that yesterday :)')

afinn_de = Afinn(language='da')
score_de = afinn_de.score('Hvis ikke det er det mest afskyelige flueknepperi...')
print(score_de)