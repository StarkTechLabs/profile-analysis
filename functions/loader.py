import sys

from shared.analysis import find_vector, upsert_data
from shared.embed import calc_embeddings
from shared.tweet import (followers, following, tweets_by_user,
                          user_by_username, user_info)


def gather_data(username: str):
    tweets = tweets_by_user(username)
    user = user_by_username(username)
    info = user_info(user["id"])
    frs = followers(user["id"])
    fing = following(user["id"])

    data = [
        f"Username: {username}",
        f"Name: {info['name']}",
        f"Description: {info['description']}",
        f"Followers Count: {info['public_metrics']['followers_count']}",
        f"Following Count: {info['public_metrics']['following_count']}",
        f"Listed Count: {info['public_metrics']['listed_count']}",
        f"Tweet Count: {info['public_metrics']['tweet_count']}",
    ]
    for t in tweets:
        data.append(t["text"])
    for f in frs:
        data.append("Follower: " + f["username"])
    for f in fing:
        data.append("Follows: " + f["username"])

    return data


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("Please provide a username")
        sys.exit(1)
    username = argv[0]
    result = find_vector(username)

    if result['vectors'] == {} or (len(argv) > 1 and argv[1] == '-f'):
        print("gathering data")
        data = gather_data(username)
        print("calculating embeddings")
        embeddings = calc_embeddings("\n".join(data)).tolist()
        print("upsert data")
        upsert_data([(username, embeddings)])
        print("Finished")
        sys.exit(0)

    print("Already exist")
    sys.exit(0)
