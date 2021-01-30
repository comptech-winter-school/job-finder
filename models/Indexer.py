from models.base_models import Embedder, Index
import numpy as np
import faiss


class FaissIndexer(Index):
    """
      Косинусного расстояния нет, но можно через скалярное произведение.
      Для этого нужно нормировать эмбеддинги (сохраним в norm_embs)
    """
    def __init__(self, embedder: Embedder):
        self.embedder = embedder
        self.texts = None
        self.norm_embs = None
        self.indexer = None

    def build(self, texts: list):
        """
          Расчет индексов в self.indexer, сохранение нормир эмбеддингов
        """
        self.texts = texts
        embs = self.embedder.transform(texts)
        features_dim = embs.shape[1]
        self.indexer = faiss.index_factory(features_dim, "Flat", faiss.METRIC_INNER_PRODUCT)
        self.indexer.ntotal
        faiss.normalize_L2(embs)
        self.norm_embs = embs.copy()
        self.indexer.add(embs)

    def get_nearest_k(self, text: str, k):
        """
          k ближайших индексов
        """
        emb = self.embedder.embedding(text)
        faiss.normalize_L2(emb)
        distance, index = self.indexer.search(emb, k)
        index = index[index >= 0] # если не найдены, то -1
        #return self.texts[index]
        return index

    def save(self, file_path: str):
        try:
            faiss.write_index(self.indexer, file_path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except: 
            print("Unexpected error")

    def load(self, file_path: str):
        try:
            self.indexer = faiss.read_index(file_path)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except: 
            print("Unexpected error")
            