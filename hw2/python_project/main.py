def easy_task(matrix):
    result = "\documentclass{article}\n\\begin{document}\n\\begin{tabular}{"
    maxrange = -1
    for i in matrix:
        maxrange = max(maxrange, len(i))
    for i in range(maxrange):
        result += " c"
    result += " }\n"
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if j != 0:
                result += "& "
            result += str(matrix[i][j]) + ' '
            if j == maxrange - 1:
                result += "\\\\\n"
            j += 1
        while j < maxrange:
            if j != 0:
                result += "& "
            if j == maxrange - 1:
                result += "\\\\\n"
            j += 1
    result += "\\end{tabular}\n\\end{document}"
    fout = open("matrix.tex", 'w')
    print(result, file=fout)


if __name__ == '__main__':
    easy_task([[1, 2, 3], [1], [1,2,3]])
