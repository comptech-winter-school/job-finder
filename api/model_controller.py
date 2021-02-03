import pandas as pd
from job_finder.models.Indexer import BaselineIndexer
from job_finder.models.Embedder import RandomEmbedder

df = pd.read_csv('ods_jobs.csv').text
indexer = BaselineIndexer(RandomEmbedder())
indexer.build(df.values.tolist())


def get_answer(text: str, k: int = 3):
    indexes = indexer.get_nearest_k(text, k)
    return df.loc[indexes].values.tolist()
