def append_member(matrix: list, sign_pos: int, value: int, target: list):
    for i in range(len(matrix)):
        if i == sign_pos:
            matrix[i].append(value)
        else:
            matrix[i].append(0)
    target.insert(len(target) - 1, 0)


def to_canon(matrix: list, matrix_signs: list, members_signs: list, target: list):
    num_members = len(target) - 1

    for i in range(len(matrix_signs)):
        if matrix_signs[i].count("<=") != 0:
            append_member(matrix, i,  1, target)
        if matrix_signs[i].count(">=") != 0:
            append_member(matrix, i, -1, target)

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
            target.insert(len(target) - 1, target[pos])
            target.insert(len(target) - 1, -target[pos])

            for i in range(len(matrix)):
                matrix[i].pop(pos)
            target.pop(pos)
            for i in range(num_members):
                if (len(target) - 1) > len(members_signs):
                    members_signs.append(">=")
                members_signs[i] = ">="
