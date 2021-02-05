import faiss
import numpy as np
from sklearn.metrics import pairwise_distances

from models.base_models import Embedder, Index


class BaselineIndexer(Index):
    def __init__(self, embedder: Embedder, metric='cosine'):
        """
          metric: as in sklearn.metrics
        """
        self.embedder = embedder
        self.metric = metric
        self.indexer = None

    def build(self, texts: list):
        self.indexer = self.embedder.transform(texts)

    def get_nearest_k(self, text: str, k=3, isDistance=False):
        emb = self.embedder.embedding(text)
        distances = pairwise_distances(emb, self.indexer, metric=self.metric)
        top_k_arguments = np.argsort(np.array(distances))[0][:k]
        if isDistance:
            return distances[:, top_k_arguments], top_k_arguments
        else:
            return top_k_arguments

    def save(self, file_path: str):
        pass

    def load(self, file_path: str):
        pass


class FaissIndexer(Index):
    """
      Faiss uses only 32-bit floating point matrices (unsupport sparse)
      metric: cosine or L2
    """

    def __init__(self, embedder: Embedder, metric='cosine'):
        self.embedder = embedder
        self.metric = metric
        self.indexer = None

    def build(self, texts: list):
        """
            shoud normalize for cosine similarity
        """
        embs = self.embedder.transform(texts).astype('float32')
        features_dim = embs.shape[1]
        if self.metric == 'cosine':
            self.indexer = faiss.index_factory(features_dim, "Flat", faiss.METRIC_INNER_PRODUCT)
            faiss.normalize_L2(embs)
        elif self.metric == 'l2':
            self.indexer = faiss.IndexFlatL2(features_dim)
        else:
            print('Metric not found')
        self.indexer.add(embs)

    def get_nearest_k(self, text: str, k=3, isDistance=False):
        """
          return topk indices : list or turple (distances, indeces)
        """
        k = min(k, self.indexer.ntotal)
        emb = self.embedder.embedding(text).astype('float32')
        if self.metric == 'cosine':
            faiss.normalize_L2(emb)
        distances, indexs = self.indexer.search(emb, k)
        indexs = indexs
        if isDistance:
            return 1 - distances, indexs
        else:
            return indexs

    def save(self, file_path: str):
        if not file_path.endswith('.indexer'):
            file_path += '.indexer'
        try:
            faiss.write_index(self.indexer, file_path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error")

    def load(self, file_path: str):
        if not file_path.endswith('.indexer'):
            file_path += '.indexer'
        try:
            self.indexer = faiss.read_index(file_path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error")
