import os

import pinecone
from sentence_transformers import SentenceTransformer

index_name = os.getenv("PINECODE_INDEX") or "docsx-content"
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV") or "eu-west1-gcp"

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
index = pinecone.Index(index_name=index_name)

model = SentenceTransformer('average_word_embeddings_komninos')


def calc_embeddings(data: list):
    encoded = model.encode(data)
    return encoded


def find_vector(id: str, namespace: str = 'content'):
    return index.fetch([id], namespace=namespace)


def query_vector(query, top_k: int = 5, namespace: str = 'content'):
    # generate embeddings for the query
    xq = model.encode([query]).tolist()
    # search pinecone index for context passage with the answer
    xc = index.query(xq, top_k=top_k, include_metadata=True,
                     namespace=namespace)
    return xc


def query_given_vector(data, namespace: str = 'content', top_k: int = 5):
    result = index.query([data], namespace=namespace,
                         top_k=top_k)
    return result


def format_query(query, context):
    # extract content from Pinecone search result and add the  tag
    context = [f" {m['metadata']['content']}" for m in context]
    # concatenate all context
    context = " ".join(context)

    # concatenate the query and context
    query = f"Using this context as a reference: {context}\n\n please answer this question: {query}"
    return query


def upsert_data(data, namespace: str = 'content'):
    """
    data should be an array of tuples, ex:
    [
        ("id-1", [0.1, 0.1, 0.1], metadata),
        ("id-2", [0.2, 0.2, 0.2], metadata),
    ]
    metadata is optional
    """
    index.upsert(vectors=data, namespace=namespace)
    return True
