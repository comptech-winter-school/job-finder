import pandas as pd
from models.Indexer import BaselineIndexer
from models.Embedder import TfidfEmbedder


df = pd.read_csv('ods_jobs.csv').text.fillna('')
indexer = BaselineIndexer(TfidfEmbedder())
indexer.build(df.values.tolist())


def get_answer(text: str, k: int = 3):
    indexes = indexer.get_nearest_k(text, k)
    return df.loc[indexes].values.tolist()
