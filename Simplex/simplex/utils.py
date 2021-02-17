def first_positive_index(c: list, N: list):
    for idx, val in enumerate(c):
        if val > 0 and idx in N:
            return idx


def find_delta_min(delta: list, B: list):
    min = delta[B[0]]

    if delta.count("inf") == len(delta):
        return "inf"

    if min == "inf":
        return "inf"

    for idx, val in enumerate(delta):
        if val != "inf" and val < min and idx in B:
            min = val
    return min


def minimizing_index(delta: list, B: list):
    for idx in B:
        if delta[idx] == find_delta_min(delta, B):
            return idx