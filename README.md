# job-finder
Project `Job Finder` at Winter Shool CompTech 2021 - service for a searching related vacations by text queries or a resume document.

Components
- `Embedder`- compute input texts embeddings, supports [TFIDF](https://ru.wikipedia.org/wiki/TF-IDF), [SBERT](https://github.com/UKPLab/sentence-transformers).
- `Indexer` - index for efficient searchin, based on [FAISS](https://github.com/facebookresearch/faiss)
- `api` - telegram bot backend, based on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

![img](https://github.com/comptech-winter-school/job-finder/blob/main/jobfinder%20struct.png)
