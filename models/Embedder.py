from models.base_models import Embedder
import numpy as np


class RandomEmbedder(Embedder):
    def __init__(self):
        self.embs = None
        self.query = None

    def embedding(self, text: str = 'pass'):
        print(text)
        if text == 'a':
            query = self.embs[0].reshape((1, -1))
        elif text == 'b':
            query = 10 * self.embs[-1].reshape((1, -1))
        else:
            query = 0.5 * (self.embs[0] + self.embs[-1]).reshape((1, -1))
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

    def load(self):
        pass

    def save(self):
        pass

    def fit(self):
        pass
