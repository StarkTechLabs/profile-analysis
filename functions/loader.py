from util import calc_embeddings, upsert_data


def handler(request):
    '''
    request is a standard Flask Request
    '''

    data = request.get_json()

    print('calculating embeddings')
    embeddings = calc_embeddings('%s\n%s'.format(
        data['title'], data['data'])).tolist()
    print('upsert data')
    upsert_data([(data['id'], embeddings, {
        'title': data['title'],
        'content': data['data']
    })], namespace=data['namespace'])
    return 'Success'
