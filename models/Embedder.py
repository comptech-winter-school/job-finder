from models.base_models import Embedder
from sklearn.feature_extraction.text import TfidfVectorizer
from abc import ABC, abstractmethod
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
import pickle
stoplist = stopwords.words("russian")


class TfidfEmbedder(Embedder):
    def __init__(self, max_features: int = 10000):
        self.vectorizer = TfidfVectorizer(max_features=max_features,
                                    lowercase=True,
                                    stop_words=stoplist, ngram_range=(1, 2))

    def embedding(self, text: str):
        return self.vectorizer.transform([text])

    def fit(self, texts):
        self.vectorizer.fit(texts)

    def transform(self, texts: list):
        return self.vectorizer.transform(texts)

    def save(self, output_path: str):
        pickle.dump(self.vectorizer , open(output_path + "/" + "vectorizer.pickle", "wb"))

    def load(self, input_path: str):
        self.vectorizer = pickle.load(open(input_path + "/" + "vectorizer.pickle", "rb"))
