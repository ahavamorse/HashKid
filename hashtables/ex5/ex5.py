

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    dict = {}
    result = []

    for path in files:
        split_path = path.split("/")
        file = split_path[-1]
        if file in dict:
            dict[file].append(path)
        else:
            dict[file] = [path]

    for file in queries:
        if file in dict:
            for path in dict[file]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
