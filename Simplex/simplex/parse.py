from pathlib import Path


def parse(filename: Path):
    signs = [">=", "=", "<="]
    variables = ["x1", "x2", "x3", "x4", "x5"]

    coeffs_matrix = list()
    null_eq = list()
    for var in variables:
        null_eq.append("")
    func = list()
    
    with filename.open("r") as file:
        for lidx, line in enumerate(file):
            # Parse line with null inequalities
            if lidx == 5:
                line = line.split()
                for tidx, token in enumerate(line):
                    if token in signs:
                        null_eq[int(line[tidx - 1][1]) - 1] = token
                continue

            # Parse line with target function
            if lidx == 6:
                func = line.split()
                continue
            
            # Parse first 5 lines
            line = line.split()
            matrix_line = list()

            for tidx, token in enumerate(line):
                if token.isdigit():
                    if line[tidx - 1] == "+":
                        matrix_line.append(float(token))
                    else:
                        matrix_line.append(-float(token))

                if token in signs:
                    matrix_line += [token, float(line[tidx + 1])]
                    coeffs_matrix.append(matrix_line)
                    break

    return coeffs_matrix, null_eq, func
