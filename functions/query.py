import sys

from shared.analysis import find_vector, query_vector

if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) < 0:
        print("Please provide a username")
        sys.exit(1)
    username = argv[0]
    vec_result = find_vector(username)

    if vec_result['vectors'] == {}:
        print("Could not find username, please load into index first")
        sys.exit(1)

    # print(vec_result['vectors'][username]['values'])
    print("running query")

    query_result = query_vector(vec_result['vectors'][username]['values'])
    print(query_result)
    print("Finished")
    sys.exit(0)
