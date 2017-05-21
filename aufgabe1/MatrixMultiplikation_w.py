# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrixmultiplikation
# Abgabedatum: 21.5.2017
#
# Gruppennummer: 63
# Gruppenmitglieder:
# - Maximilian Budwill
# - Wolfgang Ost
# - Simon Christ

# Diese Funktion können Sie verwenden, um Matrizen auszugeben.
def printmatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if i > 0:
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")


# Implementieren Sie ab hier Ihre Lösungen:
def matMultDef(a, b):
    print(40 * "-")
    print('|Parameter a:')
    printmatrix(a)
    print(40 * "-")
    print('|Parameter b:')
    printmatrix(b)
    print(40 * "-")
    # hier soll Ihre Implementierung der Matrixmultiplikation laut Definition stehen.
    # number of columns in a has to match number of rows in b
    if len(b) != len(a[0]):
        print('Matrix dimensions don\'t match')
        return
    # numbers of columns and rows for the result matrix
    num_columns = len(b[0])
    num_rows = len(a)
    # initialize result matrix with zeros
    result_m = [[0 for x in range(0, num_columns)] for y in range(0, num_rows)]
    # multiply rows of a with columns of b
    for rowidx in range(0, num_rows):
        for colidx in range(0, num_columns):
            for i in range(0, len(b)):
                result_m[rowidx][colidx] = result_m[rowidx][colidx] + a[rowidx][i] * b[i][colidx]
    # result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result_m


def matMultDC(a: object, b: object) -> object:
    # hier soll Ihre Implementierung der Matrixmultiplikation nach dem Paradigma "Teile und Herrsche"
    # number of columns in a has to match number of rows in b
    if len(b) != len(a[0]):
        print('Matrix dimensions don\'t match')
        return

    # divide a and b only horizontally or vertically, respectively. If one can't be divided further, only divide the other.
    # If none can be divided further, calculate the product iteratively

    # numbers of columns and rows for the result matrix
    num_columns = len(b[0])
    num_rows = len(a)
    # initialize result matrix with zeros
    result = [[0 for x in range(0, num_columns)] for y in range(0, num_rows)]
    if len(b[0]) == 1 and len(a) == 1:
        result[0][0] = 0
        for i in range(0, len(b)):
            result[0][0] = result[0][0] + a[0][i] * b[i][0]
    elif len(b[0]) == 1 and len(a) > 1:
        divA = len(a) // 2
        # only divide a
        a1 = a[:divA]
        a2 = a[divA:]
        print('Divided a in two:')
        print('a1')
        printmatrix(a1)
        print('a2')
        printmatrix(a2)
        m11 = matMultDC(a1, b)
        m21 = matMultDC(a2, b)
        print('Partial results:')
        print('m11')
        printmatrix(m11)
        print('m12')
        printmatrix(m21)
        result[:divA] = m11[:]
        result[divA:] = m21[:]
    elif len(b[0]) > 1 and len(a) == 1:
        divB = len(b[0]) // 2
        b1 = [x[:divB] for x in b]
        b2 = [x[divB:] for x in b]
        # only divide b
        b1 = [x[:divB] for x in b]
        b2 = [x[divB:] for x in b]
        print('Divided b in two:')
        print('b1')
        printmatrix(b1)
        print('b2')
        printmatrix(b2)
        m11 = matMultDC(a, b1)
        m12 = matMultDC(a, b2)
        print('Partial results:')
        print('m11')
        printmatrix(m11)
        print('m12')
        printmatrix(m12)
        result[0][:divB] = m11[0][:]
        result[0][divB:] = m12[0][:]
    elif len(b[0]) > 1 and len(a) > 1:
        divA = len(a) // 2
        divB = len(b[0]) // 2
        # divide a in two, horizontally
        a1 = a[:divA]
        a2 = a[divA:]
        print('Divided a in two:')
        print('a1')
        printmatrix(a1)
        print('a2')
        printmatrix(a2)
        # divide b in two, vertically
        b1 = [x[:divB] for x in b]
        b2 = [x[divB:] for x in b]
        print('Divided b in two:')
        print('b1')
        printmatrix(b1)
        print('b2')
        printmatrix(b2)
        m11 = matMultDC(a1, b1)
        m12 = matMultDC(a1, b2)
        m21 = matMultDC(a2, b1)
        m22 = matMultDC(a2, b2)
        print('Partial results:')
        print('m11')
        printmatrix(m11)
        print('m12')
        printmatrix(m12)
        print('m21')
        printmatrix(m21)
        print('m22')
        printmatrix(m22)
        # copy m11 into result
        for r in range(0, divA):
            for c in range(0, divB):
                result[r][c] = m11[r][c]
        # copy m12 into result
        for r in range(0, divA):
            for c in range(divB, len(b[0])):
                result[r][c] = m12[r][c - divB]
        # copy m21 into result
        for r in range(divA, len(a)):
            for c in range(0, divB):
                result[r][c] = m21[r - divA][c]
        # copy m22 into result
        for r in range(divA, len(a)):
            for c in range(divB, len(b[0])):
                result[r][c] = m22[r - divA][c - divB]
    # result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result


# Hier ist ein Testfall:
print('|Berechnung Matrixmultiplikation:')
print(40 * "-")
# Aufruf nach Definition
print()
print('|Berechnung nach Definition')
result = matMultDef(
    [  # a
        [3, 2, 1], [1, 0, 2]], [  # b
        [1, 2], [0, 1], [4, 0]])

print()
print('Ergebnis nach Definition')
printmatrix(result)
print(40 * "-")

# Aufrufen Divide and Conquer 1
print()
print('|Berechnung nach Divide and Conquer ')
print('-> Zerlege in einzelne Zeilen und Spalten als Elementar')
result = matMultDC([[3, 2, 1], [1, 0, 2]], [[1, 2], [0, 1], [4, 0]])
print()
print ('Ergebnis nach Divide and Conquer ')
printmatrix(result)
print(40 * "-")
