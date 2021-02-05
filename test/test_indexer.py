from models.Indexer import BaselineIndexer, FaissIndexer
from models.Embedder import RandomEmbedder
import numpy as np
import unittest

class testIndexer(unittest.TestCase):
    def setUp(self):
        self.embedder = RandomEmbedder()

    def test_indexer(self):
        for metric in ['cosine', 'l2']:
            self.indexerFaiss = FaissIndexer(self.embedder, metric=metric)
            self.indexerBase = BaselineIndexer(self.embedder, metric=metric)
            self.indexerFaiss.build(['pass'])
            self.indexerBase.build(['pass'])
            for strategy in ['a', 'b', 'c']:
                top_faiss = self.indexerFaiss.get_nearest_k(strategy)
                top_true = self.indexerBase.get_nearest_k(strategy)              
                self.assertEqual(top_faiss, top_true)