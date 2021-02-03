from models.base_models import Embedder, Index, TextDao
from models.Embedder import preproc
import pandas as pd
import os


class DAO(TextDao):
    """
    Example:
        dao = DAO(MyEmbedder=TfidfEmbedder, MyIndexer=BaselineIndexer)
        dao.get_top_k("some_cv_text", number_of vacancies)
    """
    def  __init__(self, MyEmbedder: Embedder, 
                        MyIndexer: Index, 
                        path_jobs='../data/ods_jobs.csv', 
                        path_model=None):
        self.df = None
        self.embedder = MyEmbedder()
        self.indexer = MyIndexer(self.embedder)
        if os.path.exists(path_jobs) :
            self.df = pd.read_csv(path_jobs, usecols = ['text'])
            self.df = self.df[self.df['text'].notna()]
        else:
            print(f"Can't open {path_jobs}")
            
        if path_model is None:
            self.embedder.fit(self.df['text'])
            self.indexer.build(self.df['text'])
        else:
            self.embedder.load(path_model+'.embedder')
            self.indexer.load(path_model+'.indexer')
            
    def get_top_k(self, text: str, k=3):
        inds = self.indexer.get_nearest_k(text, k=3)
        return self.df.loc[inds, 'text']
