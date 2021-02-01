from sklearn.feature_extraction.text import TfidfVectorizer
from abc import ABC, abstractmethod
from nltk.corpus import stopwords

stoplist = stopwords.words("russian")


class Embedder(ABC):
    @abstractmethod
    def embedding(self, text: str):
        pass

    @abstractmethod
    def transform(self, texts: list):
        pass

    @abstractmethod
    def fit(self, texts):
        pass

    @abstractmethod
    def save(self, output_path: str):
        pass

    @abstractmethod
    def load(self, input_path: str):
        pass


class TfidfEmbedder(Embedder):
    def __init__(self, max_features: int = 10000):
        self.vectorizer = TfidfVectorizer(max_features=max_features,
                                    lowercase=True,
                                    stop_words=stoplist)

    def embedding(self, text: str):
        return self.vectorizer.transform([text])

    def fit(self, texts):
        self.vectorizer.fit(texts)

    def transform(self, text: str):
        return self.vectorizer.transform([text])

    def save(self, output_path: str):
        pickle.dump(self.vectorizer , open(output_path + "vectorizer.pickle", "wb"))

    def load(self, input_path: str):
        self.vectorizer = pickle.load(open(input_path + "vectorizer.pickle", "rb"))
        
        
       
