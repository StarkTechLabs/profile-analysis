from flask import Flask, jsonify

from .analysis import find_vector, query_vector, upsert_data
from .embed import calc_embeddings
from .tweet import (followers, following, tweet_by_id, tweets_by_user,
                    user_by_username, user_info)

app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({
        'message': 'Welcome'
    })


@app.route('/twttr/tweets/<id>', methods=['GET'])
def get_tweet_by_id(id: str):
    res = tweet_by_id(id)
    return jsonify(res)


@app.route('/twttr/users/<id>', methods=['GET'])
def get_user_info(id: str):
    info = user_info(id)
    return jsonify(info)


@app.route('/twttr/users/username/<username>', methods=['GET'])
def get_user_info_username(username: str):
    user = user_by_username(username)
    # info = user_info(user["id"])
    return jsonify(user)


@app.route('/twttr/users/<username>/tweets', methods=['GET'])
def get_user_tweets(username: str):
    print(username)
    tweets = tweets_by_user(username)
    return jsonify(tweets)


def gather_data(username: str):
    tweets = tweets_by_user(username)
    user = user_by_username(username)
    info = user_info(user["id"])
    frs = followers(user["id"])
    fing = following(user["id"])
    # build embeddings

    data = [
        "Username: " + username,
        "Name: " + info["name"],
        "Description: " + info["description"],
    ]
    for t in tweets:
        data.append(t["text"])
    for f in frs:
        data.append("Follower: " + f["username"])
    for f in fing:
        data.append("Follows: " + f["username"])

    return data


@app.route('/twttr/users/<username>/load', methods=['GET'])
def load_user_profile(username: str):
    """ Load user profile and tweets for vector analysis """
    print(username)

    data = gather_data(username)
    embeddings = calc_embeddings("\n".join(data)).tolist()
    upsert_data([(username, embeddings)])
    return jsonify({"message": "ok"})


@app.route('/twttr/users/<username>/all', methods=['GET'])
def find_user_profile(username: str):
    """ Load user profile and tweets for to display """
    print(username)

    data = gather_data(username)
    return jsonify(data)


@app.route('/query/<username>', methods=['GET'])
def query_index(username: str):
    print("query: " + username)
    data = gather_data(username)
    embeddings = calc_embeddings("\n".join(data)).tolist()
    result = query_vector(embeddings)
    # print(result)

    res = []
    for m in result['matches']:
        res.append({'id': m['id'], 'score': m['score'],
                   'metadata': m['metadata'] if 'metadata' in m else {}})
    # print(res)
    return jsonify(res)


@app.route('/vector/<username>', methods=['GET'])
def fetch_vector(username: str):
    result = find_vector(username)
    print(result)

    return jsonify(result)


#
# Error Handling
#


@app.errorhandler(Exception)
def handle_error(error):
    """ Default error handler """
    print(error)
    error = error or {}
    if type(error) is object:
        response = jsonify(error)
    else:
        response = str(error)

    return jsonify({'error': response, 'message': 'An error occurred.'}), 500


def run(port=5000, debug=False):
    """ """
    print('Running server on port ' + str(port))
    app.run(port=port, debug=debug)
