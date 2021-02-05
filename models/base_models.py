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


class Index(ABC):
    @abstractmethod
    def build(self, texts: list):
        pass

    @abstractmethod
    def save(self, file_path: str):
        pass

    @abstractmethod
    def load(self, file_path: str):
        pass

    @abstractmethod
    def get_nearest_k(self, text: str, k):
        pass


class Validator(ABC):
    @abstractmethod
    def get_score(self, true_values, pred_values):
        pass


class TextDao(ABC):
    @abstractmethod
    def get_top_k(self, text: str, k):
        pass
