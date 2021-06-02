def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dict = {}

    for index in range(0, len(weights)):
        if weights[index] in dict:
            dict[weights[index]].append(index)
        else:
            dict[weights[index]] = [index]

    for weight in dict.keys():
        needed_weight = limit - weight
        if needed_weight in dict:
            index_1 = dict[weight][0]
            index_2 = dict[needed_weight][-1]
            print([index_1, index_2])
            if index_1 > index_2:
                return [index_1, index_2]
            else:
                return [index_2, index_1]

    return None
