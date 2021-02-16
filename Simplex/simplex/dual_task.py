def to_dual_task(matrix: list, matrix_signs: list, free_members: list, members_signs: list, target: list):
    dual_matrix = [list(i) for i in zip(*matrix)]
    dual_free_members = []
    dual_free_members.extend(target)
    dual_free_members.pop()
    dual_target = []
    dual_target.extend(free_members)
    dual_target.append("max")

    dual_matrix_signs = []
    for i in range(len(members_signs)):
        if members_signs[i] == ">=":
            dual_matrix_signs.append(">=")
        elif members_signs[i] == "":
            dual_matrix_signs.append("=")
        else:
            dual_matrix_signs.append("<=")

    dual_members_signs = []
    for i in range(len(matrix_signs)):
        if matrix_signs[i] == ">=":
            dual_members_signs.append(">=")
        elif matrix_signs[i] == "=":
            dual_members_signs.append("")
        else:
            dual_members_signs.append("<=")

    return dual_matrix, dual_matrix_signs, dual_free_members, dual_members_signs, dual_target
