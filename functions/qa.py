from generator import generate_answer
from util import format_query, query_vector


def handler(request):
    '''
    request is a standard Flask Request
    '''

    data = request.get_json()
    query = data['query'] or 'what is abstractive question-answering?'
    vector_result = query_vector(query, top_k=1, namespace=data['namespace'])

    context = get_context(vector_result['matches'])
    query = format_query(query, vector_result['matches'])

    answer = generate_answer(query)
    return {'context': context, 'answer': answer}


def get_context(matches):
    # extract content from Pinecone search result and add the  tag
    context = [f" {m['metadata']['content']}" for m in matches]
    # concatenate all context
    context = " ".join(context)
    return context


if __name__ == '__main__':
    query = 'what is abstractive question-answering?' or 'what is pinecone?'
    vector_result = query_vector(
        query, top_k=1, namespace='9yzOWI3afyf4nyfnfHK80rdBfuD3')
    query = format_query(query, vector_result['matches'])

    answer = generate_answer(query)
    print(answer)
