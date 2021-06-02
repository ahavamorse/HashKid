def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dict = {}
    result = []

    for num in a:
        if abs(num) in dict:
            result.append(abs(num))
        else:
            dict[abs(num)] = 1
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
