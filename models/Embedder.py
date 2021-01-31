from sklearn.feature_extraction.text import TfidfVectorizer
from abc import ABC, abstractmethod

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
                                    stop_words='english')

    def embedding(self, text: str) -> str:
        return self.vectorizer.transform([text])

    def fit(self, texts):
        self.vectorizer.fit(texts)

    def transform(self, text: str):
        return self.vectorizer.transform([text])

    def save(self, output_path: str):
        pickle.dump(self.transformed_data , open(output_path + "vectorizer.pickle", "wb"))

    def load(self, input_path: str):
        pickle.dump(self.transformed_data , open(output_path + "vectorizer.pickle", "wb"))
        
        
        
#SBERT_Embedder
from sentence_transformers import SentenceTransformer

class SBERTEmbedder(Embedder):
    def __init__(self):
        self.vectorizer = SentenceTransformer('paraphrase-distilroberta-base-v1')
        self.transformed_data = None

    def transform(self, text: str):
        self.transformed_data = self.vectorizer.encode([text])
        return self.vectorizer.encode([text])

    def save(self, output_path: str):
        pickle.dump(self.transformed_data, open(output_path + "vectorizer.pickle", "wb"))

    def load(self, input_path: str):
        pickle.dump(self.transformed_data, open(output_path + "vectorizer.pickle", "wb"))

        
