def minimizing_index(delta: list):
    for idx, val in enumerate(delta):
        min = val
        min_idx = idx
        if min != "inf":
            break

    if min == "inf":
        return min

    for idx, val in enumerate(delta):
        if val == "inf":
            continue
        
        if val < min:
            min = val
            min_idx = idx

    return min_idx