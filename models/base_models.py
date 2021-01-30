from abc import ABC, abstractmethod


class Embedder(ABC):
    @abstractmethod
    def embedding(text: str):
        pass


class Index(ABC):
    @abstractmethod
    def build(texts: str):
        pass

    @abstractmethod
    def save(file_path: str):
        pass

    @abstractmethod
    def load(file_path: str):
        pass


class Validator(ABC):
    @abstractmethod
    def get_score(true_values, pred_values):
        pass

