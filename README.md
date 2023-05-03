# docsx-py

- loader.py - Collection of python code to calculate vector embeddings for given data and upsert them into pinecone.
- analysis.py - Another function to build a question-answer system based on pinecone vectors.

## Setup

- `python3 -m venv .venv` create virutal env with python3
- `source .venv/bin/activate` activate virtual env
- `pip install -r requirements.txt` install required dependencies

### Environment Variables

- PINECONE_API_KEY - pinecone api key to access embeddings index
