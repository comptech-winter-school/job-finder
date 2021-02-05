from model.base_models import Embedder
from sklearn.feature_extraction.text import TfidfVectorizer
from abc import ABC, abstractmethod
from nltk.corpus import stopwords

stoplist = stopwords.words("russian")

def preproc(text: str):
    pattern_html = r'<.*?>' 
    pattern_smile = r':\w+?-?\w+:'
    pattern_contact = r'\S*@\S+'
    pattern_nt = r'[\n\t\r*]'
    pattern_phone = r'(?:\d{9,11})?(?:\d *\(*\d{3}\)* *\d{3} *\d{2} *\d{2})?(?:\d\-*\d{3}\-*\d{3}\-*\d{2}\-*\d{2})?'
    clean_text = unicodedata.normalize("NFKD", str(text))
    clean_text = re.sub(pattern_html, r'', clean_text)
    clean_text = re.sub(pattern_smile, r'', clean_text)
    clean_text = re.sub(pattern_contact, r'', clean_text)
    clean_text = re.sub(pattern_nt, r' ', clean_text)
    clean_text = re.sub(pattern_phone, r'', clean_text)
    punct = '[!"#$%&()*\+,\.:;<=>`{|}~„“«»†*‘’•·]'
    clean_text = re.sub(punct, r'', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text
    return clean_text if clean_text else text


class TfidfEmbedder(Embedder):
    def __init__(self, max_features: int = 10000):
        self.vectorizer = TfidfVectorizer(max_features=max_features,
                                    lowercase=True,
                                    stop_words=stoplist, ngram=(1, 2))

    def embedding(self, text: str):
        text = preproc(text)
        return self.vectorizer.transform([text])

    def fit(self, texts):
        self.vectorizer.fit([preproc(text) for text in texts])

    def transform(self, text: list):
        return self.vectorizer.transform([preproc(text) for text in texts])

    def save(self, output_path: str):
        pickle.dump(self.vectorizer , open(output_path + "/" + "vectorizer.pickle", "wb"))

    def load(self, input_path: str):
        self.vectorizer = pickle.load(open(input_path + "/" + "vectorizer.pickle", "rb"))
        
        
        
class SBERTembedder(Embedder):
    def __init__(self):
      self.sbert = SentenceTransformer('paraphrase-distilroberta-base-v1')

    def embedding(self, text: str):
      return self.sbert.encode([preproc(text) for text in texts])

    def transform(self, texts: list):
      return [self.embedding(x) for x in texts]

    def fit(self, texts):
      pass

    def save(self, output_path: str):
      torch.save(self.sbert.state_dict(), output_path)

    def load(self, input_path: str):
      self.sbert= sbert.load_state_dict(torch.load(input_path))
      self.sbert.eval()
