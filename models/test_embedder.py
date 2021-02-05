from unittest import TestCase

from models.Embedder import TfidfEmbedder, SBERTembedder


class TestTfidfEmbedder(TestCase):
    def setUp(self):
        self.texts = ['Hi', 'hello!', 'how are you?', 'Привет как дела?']
        self.tfidf_vectors = [...]

    def test_fit(self):
        tfidf = TfidfEmbedder()
        tfidf.fit(self.texts)
        vectors = tfidf.transform(self.texts)
        print(tfidf)
        print(vectors)


class TestSBERTembedder(TestCase):
    def setUp(self):
        self.texts = ['Hi', 'hello!', 'how are you?', 'Привет как дела?']
        self.sbert_vectors = [...]

    def test_sbert_transform(self):
        sbert = SBERTembedder()
        vectors = sbert.transform(self.texts)
        print(vectors)
        # self.assertEquals(self.sbert_vectors, vectors)
