from models.base_models import Embedder
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk
import re
import unicodedata


nltk.download("stopwords")
from nltk.corpus import stopwords
stoplist = stopwords.words("russian")

def preproc(text: str):
    """
        Удаление юникодов типа \xa0 - неразрывный пробел
        Удаление ссылок на сайты, на почту, на телеграм, удаление смайликов вида :smile:, удаление \n, \t, \r
        Удаление пунктуации
        Схлопывание двойных пробелов
    """
    pattern_html = r'<.*?>' 
    pattern_smile = r':\w+?-?\w+:'
    pattern_contact = r'\S*@\S+'
    pattern_nt = r'[\n\t\r*]'
    pattern_phone = r'(?:\d{9,11})?(?:\d *\(*\d{3}\)* *\d{3} *\d{2} *\d{2})?(?:\d\-*\d{3}\-*\d{3}\-*\d{2}\-*\d{2})?'
    clean_text = unicodedata.normalize("NFKD", str(text))
    clean_text = re.sub(pattern_html, r'', clean_text)
    clean_text = re.sub(pattern_smile, r'', clean_text)
    clean_text = re.sub(pattern_contact, r'', clean_text)
    clean_text = re.sub(pattern_nt, r' ', clean_text)
    clean_text = re.sub(pattern_phone, r'', clean_text)
    punct = '[!"#$%&()*\+,\.:;<=>`{|}~„“«»†*‘’•·]'
    clean_text = re.sub(punct, r'', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text


class RandomEmbedder(Embedder):
    def __init__(self):
        self.embs = None
        self.query = None  

    def embedding(self, text: str = 'pass'):
        print(text)
        if text == 'a':
            query = self.embs[0].reshape((1,-1))
        elif text == 'b':
            query = 10 * self.embs[-1].reshape((1,-1))
        else:
            query = 0.5*(self.embs[0] + self.embs[-1]).reshape((1,-1))
        self.query = query
        return self.query

    def transform(self, texts: list = 'pass'):
        self.embs = np.array([[0.21931236, 0.19499308],
                              [0.67775472, 0.70789698],
                              [0.15899879, 0.29340316],
                              [0.15655223, 0.04617645],
                              [0.91230769, 0.29454197],
                              [0.53035581, 0.23188229],
                              [0.15494525, 0.22613995],
                              [0.22196722, 0.88154772],
                              [0.07235152, 0.24377389]]).astype('float32')
        return self.embs
    
    def fit(self, texts):
        pass

    def save(self, output_path: str):
        pass

    def load(self, input_path: str):
        pass


class TfidfEmbedder(Embedder):
    def __init__(self, max_features: int = 100):
        self.vectorizer = TfidfVectorizer(max_features=max_features,
                                    lowercase=True,
                                    stop_words=stoplist)

    def embedding(self, text):
        return self.vectorizer.transform([text])

    def fit(self, texts):
        self.vectorizer.fit(texts)

    def transform(self, text: list):
        return self.vectorizer.transform([text])

    def save(self, output_path: str):
        if output_path[-9:] != '.embedder':
            output_path += '.embedder'
        try:
            pickle.dump(self.vectorizer , open(output_path, "wb"))
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except: 
            print("Unexpected error")

    def load(self, input_path: str):
        if output_path[-9:] != '.embedder':
            output_path += '.embedder'
        try:
            self.vectorizer = pickle.load(open(input_path, "rb"))
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except: 
            print("Unexpected error")
            