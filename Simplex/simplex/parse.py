from pathlib import Path


def parse(filename: Path):
    signs = [">=", "=", "<="]
    variables = ["x1", "x2", "x3", "x4", "x5"]

    matrix = list()
    line_signs = list()
    free_vec = list()

    var_signs = list()
    for var in variables:
        var_signs.append("")
    target = list()
    
    with filename.open("r") as file:
        for lidx, line in enumerate(file):
            line = line.split()
            matrix_line = list()

            # Parse line with null inequalities
            if lidx == 5:
                for tidx, token in enumerate(line):
                    if token in signs:
                        var_signs[int(line[tidx - 1][1]) - 1] = token
                continue
            
            # Parse any other line
            for tidx, token in enumerate(line):
                if token.isdigit():
                    if line[tidx - 1] == "+":
                        matrix_line.append(float(token))
                    else:
                        matrix_line.append(-float(token))

                if token in signs:
                    # If line contains target function
                    if lidx == 6:
                        target += matrix_line
                        target.append(line[tidx + 1])
                    else:
                        line_signs.append(token)
                        free_vec.append(float(line[tidx + 1]))
                    break

            matrix.append(matrix_line)

    return matrix, line_signs, free_vec, var_signs, target
