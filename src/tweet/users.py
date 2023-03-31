from .util import get


def user_by_username(username: str):
    url_path = "/users/by/username/{0}".format(username)
    result = get(url_path)
    return result["data"]["data"]


def user_info(userId: str):
    url_path = "/users/{0}".format(userId)
    params = {
        "user.fields": "created_at,description,name,entities,profile_image_url,withheld,public_metrics"
    }
    result = get(url_path, params=params)
    return result["data"]["data"]


def followers(userId: str):
    url_path = "/users/{0}/followers".format(userId)
    params = {
        # "user.fields": "created_at,description,name,public_metrics"
    }
    result = get(url_path, params=params)
    return result["data"]["data"]


def following(userId: str):
    url_path = "/users/{0}/following".format(userId)
    params = {
        # "user.fields": "created_at,description,name,public_metrics"
    }
    result = get(url_path, params=params)
    return result["data"]["data"]


if __name__ == "__main__":
    user = user_by_username("Microsoft")
    userId = user['id']
    print("userId: {0}".format(userId))
    print("\n\n")
    userInfo = user_info(userId)
    print("created: {0}".format(userInfo["created_at"]))
    print("name: {0}".format(userInfo["name"]))
    print("description: {0}".format(userInfo["description"]))
    print("profile_image_url: {0}".format(userInfo["profile_image_url"]))

    print("followers_count: {0}".format(
        userInfo["public_metrics"]["followers_count"]))
    print("following_count: {0}".format(
        userInfo["public_metrics"]["following_count"]))
    print("tweet_count: {0}".format(userInfo["public_metrics"]["tweet_count"]))
    print("listed_count: {0}".format(
        userInfo["public_metrics"]["listed_count"]))
    print("\n\n")
