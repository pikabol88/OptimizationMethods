def pivot(N: list, B: list, A: list, b: list, c: list, v: list, l: int, e: int):
    N_new = list()
    B_new = list()
    A_new = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    b_new = [0 for i in range(len(b))]
    c_new = [0 for i in range(len(c))]
    v_new = [0 for i in range(len(v))]

    b_new[e] = b[l] / A[e][l]

    for j in N:
        if j != e:
            A_new[j][e] = A[j][l] / A[e][l]
    A_new[l][e] = 1 / A[e][l]

    for i in B:
        if i != l:
            b_new[i] = b[i] - A[e][i] * b_new[e]

            for j in N:
                if j != e:
                    A_new[j][i] = A[j][i] - A[e][i] * A_new[j][e]
            
            A_new[l][i] = -A[e][i] / A_new[l][e]
    
    for i in range(len(v)):
        v_new[i] = v[i] + c[e] * b_new[e]

    for j in N:
        if j != e:
            c_new[j] = c[j] - c[e] * A_new[j][e]
    c_new[l] = -c[e] * A_new[l][e]

    for i in N:
        if i != e and i != l:
            N_new.append(i)

    for i in B:
        if i != e and i != l:
            B_new.append(i)

    return N_new, B_new, A_new, b_new, c_new, v_new


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


def simplex(N: list, B: list, A: list, b: list, c: list, v: list):
    delta = [0 for m in range(len(A[0]))]
    x = list()

    for j in N:
        if c[j] > 0:
            e = first_positive_index(c, N)
            
            for i in B:
                if A[e][i] > 0:
                    delta[i] = b[i] / A[e][i]
                else:
                    delta[i] = "inf"
            
            l = minimizing_index(delta, B)
            if delta[l] == "inf":
                raise Exception("Задача не ограничена")
            else:
                N, B, A, b, c, v = pivot(N, B, A, b, c, v, l, e)
    
    for i in range(len(A)):
        if i in B:
            x.append(b[i])
        else:
            x.append(0)
    
    return x
