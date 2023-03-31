import os

import pinecone

index_name = "profile-analysis"
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV") or "eu-west1-gcp"

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
index = pinecone.Index(index_name=index_name)


def analyze(usernameOne: str, usernameTwo: str):
    return {}


def find_vector(id: str, namespace: str = 'content'):
    return index.fetch([id], namespace=namespace)


def query_vector(data, namespace: str = 'content', top_k: int = 5):
    result = index.query([data], namespace=namespace,
                         top_k=top_k)
    return result


def upsert_data(data, namespace: str = 'content'):
    """
    data should be an array of tuples, ex:
    [
        ("username1", [0.1, 0.1, 0.1], metadata),
        ("username2", [0.2, 0.2, 0.2], metadata),
    ]
    metadata is optional
    """
    index.upsert(vectors=data, namespace=namespace)
    return True
