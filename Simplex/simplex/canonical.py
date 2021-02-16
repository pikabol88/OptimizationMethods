def append_member(matrix: list, sign_pos: int, value: int):
    for i in range(len(matrix)):
        if i == sign_pos:
            matrix[i].append(value)
        else:
            matrix[i].append(0)


def to_canon(matrix: list, matrix_signs: list, members_signs: list, target: list):
    for i in range(len(matrix_signs)):
        if matrix_signs.count("<=") != 0:
            append_member(matrix, i,  1)
        if matrix_signs.count(">=") != 0:
            append_member(matrix, i, -1)

    for i in range(len(matrix_signs)):
        matrix_signs[i] = "="

    for pos in range(len(members_signs)):
        if members_signs[pos] == "<=":
            for i in range(len(matrix)):
                matrix[i][pos] = -matrix[i][pos]
            target[pos] = -target[pos]

        if members_signs[pos] == "":
            for i in range(len(matrix)):
                matrix[i].append(matrix[i][pos])
                matrix[i].append(-matrix[i][pos])
            target.append(target[pos])
            target.append(-target[pos])

            for i in range(len(matrix)):
                matrix[i].pop(pos)
            target.pop(pos)
            for i in range(len(target)):
                members_signs[i] = ">="
