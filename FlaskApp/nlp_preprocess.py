import pandas as pd
import string
import numpy as np

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import nltk
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')

class NLPprocess:
    def __init__(self, data):
        self.data = data
        self.lowers = self.normalize()
        self.tokens = self.tokenize()
        self.clean_tokens = self.stopwords_removal()
        self.lemmas = self.lemmatize()
    
    def normalize(self):
        lowers = self.data.lower()
        return lowers
        
    def tokenize(self):
        tokens = word_tokenize(self.lowers)
        return tokens
    
    def stopwords_removal(self):
        stopW = stopwords.words('english')
        stopW.extend(list(string.punctuation))
        tokens_without_stopW = [word for word in self.tokens if word not in stopW]
        return tokens_without_stopW
        
    def lemmatize(self, join=True):
        wnl = WordNetLemmatizer()
        tokens = [wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,'v'),'n'),'a') for w in self.clean_tokens]
        if join:
            return ' '.join(tokens)
        else:
            return tokens


