from sklearn.feature_extraction.text import CountVectorizer

from job_finder.models.base_models import Embedder


class CountVectModel(Embedder):
    def __init__(self, max_features: int = 10000):
        self.vect = CountVectorizer(ngram_range=(1, 2),
                                    max_features=max_features,
                                    lowercase=True,
                                    stop_words='english')

    def embedding(self, text: str):
        return self.vect.transform([text])

    def fit(self, texts):
        self.vect.fit(texts)

    def transform(self, text: str):
        return self.vect.transform([text])

    def save(self, output_path: str):
        pass

    def load(self, input_path: str):
        pass
