import os
import my_lib as drawer
from pdflatex import PDFLaTeX


def draw_matrix(matrix, result):
    result += "\\begin{tabular}{"
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
    result += "\\end{tabular}"


def easy_task(matrix):
    result = "\documentclass{article}\n\\begin{document}\n"
    draw_matrix(matrix, result)
    result += "\n\\end{document}"
    fout = open("matrix.tex", 'w')
    print(result, file=fout)


def medium_task(matrix):
    result = "\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n"
    draw_matrix(matrix, result)
    drawer.pic_write("fib_func.py")
    result += "\\includegraphics[scale=0.25]{graph.png}"
    fout = open("second_task.tex", 'w')
    print(result, file=fout)
    fout = open("second_task.pdf", 'wb')
    print(PDFLaTeX.from_texfile("second_task.tex").create_pdf()[0], fout)


if __name__ == '__main__':
    # easy_task([[1, 2, 3], [1], [1,2,3]])
    medium_task([[1, 2, 3], [1], [1, 2, 3]])
