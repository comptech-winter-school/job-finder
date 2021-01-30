from abc import ABC, abstractmethod


class Embedder(ABC):
    @abstractmethod
    def embedding(self, text: str):
        pass


class Index(ABC):
    @abstractmethod
    def build(self, texts: str):
        pass

    @abstractmethod
    def save(self, file_path: str):
        pass

    @abstractmethod
    def load(self, file_path: str):
        pass


class Validator(ABC):
    @abstractmethod
    def get_score(self, true_values, pred_values):
        pass

