def insert_member(matrix, sign_pos, member_pos, value):
    for i in range(len(matrix)):
        if i == sign_pos:
            matrix[i].insert(member_pos, value)
        matrix[i].insert(member_pos, 0)
    return member_pos + 1


def to_canon(matrix, signs, target, members):

    for i in range(len(matrix)):
        if matrix[i].count("<=") != 0:
            members = insert_member(matrix, i, members, 1)
        if matrix[i].count(">=") != 0:
            members = insert_member(matrix, i, members, -1)

    for i in range(len(matrix)):
        matrix[i][members] = "="

    for pos in range(len(signs)):
        if signs[pos] == "<=":
            for i in range(len(matrix)):
                matrix[i][pos] = -matrix[i][pos]
            target[pos] = -target[pos]

        if signs[pos] == "":
            for i in range(len(matrix)):
                matrix[i].insert(members, matrix[i][pos])
                matrix[i].insert(members + 1, -matrix[i][pos])
            members = + 2
            target.insert(len(target) - 2, target[pos])
            target.insert(len(target) - 2, -target[pos])

            for i in range(len(matrix)):
                matrix[i].pop(pos)
            target.pop(pos)
