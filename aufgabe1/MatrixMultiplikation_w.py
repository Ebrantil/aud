# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrixmultiplikation
# Abgabedatum: 21.5.2017
#
# Gruppennummer: <Bitte eintragen>
# Gruppenmitglieder: 
# - <Bitte eintragen>
# - <Bitte eintragen>
# - <Bitte eintragen>

# Diese Funktion können Sie verwenden, um Matrizen auszugeben.
def printMatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if (i > 0):
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")

# Implementieren Sie ab hier Ihre Lösungen:
def matMultDef(a, b):
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)
    # hier soll Ihre Implementierung der Matrixmultiplikation laut Definition stehen.
    # number of columns in a has to match number of rows in b
    if len(b) != len(a[0]):
        print('Matrix dimensions don\'t match')
        return
    # numbers of columns and rows for the result matrix
    numColumns = len(b[0])
    numRows = len(a)
    # initialize result matrix with zeros
    result = [[0 for x in range(0, numColumns)] for y in range(0, numRows)]
    # multiply rows of a with columns of b
    for rowidx in range(0, numRows):
        for colidx in range(0, numColumns):
            for i in range(0, len(b)):
                result[rowidx][colidx] = result[rowidx][colidx] + a[rowidx][i]*b[i][colidx]
    # result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

def matMultDC(a, b):
    """
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)
    """
    # hier soll Ihre Implementierung der Matrixmultiplikation nach dem Paradigma "Teile und Herrsche"
    # number of columns in a has to match number of rows in b
    if len(b) != len(a[0]):
        print('Matrix dimensions don\'t match')
        return
        
    # divide a and b only horizontally or vertically, respectively. If one can't be divided further, only divide the other.
    # If none can be divided further, calculate the product iteratively
    
    # numbers of columns and rows for the result matrix
    numColumns = len(b[0])
    numRows = len(a)
    # initialize result matrix with zeros
    result = [[0 for x in range(0, numColumns)] for y in range(0, numRows)]
    if len(b[0]) == 1 and len(a) == 1:
        result[0][0] = 0
        for i in range(0, len(b)):
            result[0][0] = result[0][0] + a[0][i]*b[i][0]
    elif len(b[0]) == 1 and len(a) > 1:
        divA = len(a) // 2
        # only divide a
        A1 = a[:divA]
        A2 = a[divA:]
        print('Divided a in two:')
        print('A1')
        printMatrix(A1)
        print('A2')
        printMatrix(A2)
        M11 = matMultDC(A1, b)
        M21 = matMultDC(A2, b)
        print('Partial results:')
        print('M11')
        printMatrix(M11)
        print('M12')
        printMatrix(M21)
        result[:divA] = M11[:]
        result[divA:] = M21[:]
    elif len(b[0]) > 1 and len(a) == 1:
        divB = len(b[0]) // 2
        B1 = [x[:divB] for x in b]
        B2 = [x[divB:] for x in b]
        # only divide b
        B1 = [x[:divB] for x in b]
        B2 = [x[divB:] for x in b]
        print('Divided b in two:')
        print('B1')
        printMatrix(B1)
        print('B2')
        printMatrix(B2)
        M11 = matMultDC(a, B1)
        M12 = matMultDC(a, B2)
        print('Partial results:')
        print('M11')
        printMatrix(M11)
        print('M12')
        printMatrix(M12)
        result[0][:divB] = M11[0][:]
        result[0][divB:] = M12[0][:]
    elif len(b[0]) > 1 and len(a) > 1:
        divA = len(a) // 2
        divB = len(b[0]) // 2
        # divide a in two, horizontally
        A1 = a[:divA]
        A2 = a[divA:]
        print('Divided a in two:')
        print('A1')
        printMatrix(A1)
        print('A2')
        printMatrix(A2)
        # divide b in two, vertically
        B1 = [x[:divB] for x in b]
        B2 = [x[divB:] for x in b]
        print('Divided b in two:')
        print('B1')
        printMatrix(B1)
        print('B2')
        printMatrix(B2)
        M11 = matMultDC(A1, B1)
        M12 = matMultDC(A1, B2)
        M21 = matMultDC(A2, B1)
        M22 = matMultDC(A2, B2)
        print('Partial results:')
        print('M11')
        printMatrix(M11)
        print('M12')
        printMatrix(M12)
        print('M21')
        printMatrix(M21)
        print('M22')
        printMatrix(M22)
        # copy M11 into result
        for r in range(0, divA):
            for c in range(0, divB):
                result[r][c] = M11[r][c]
        # copy M12 into result
        for r in range(0, divA):
            for c in range(divB, len(b[0])):
                result[r][c] = M12[r][c-divB]
        # copy M21 into result
        for r in range(divA, len(a)):
            for c in range(0, divB):
                result[r][c] = M21[r-divA][c]
        # copy M22 into result
        for r in range(divA, len(a)):
            for c in range(divB, len(b[0])):
                result[r][c] = M22[r-divA][c-divB]
    # result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

# Hier ist ein Testfall:
# result = matMultDef(
result = matMultDC(
[ # a
[3, 2, 1],
[1, 0, 2]
],
[ # b
[1, 2],
[0, 1],
[4, 0]]
)

print('berechnet:')
printMatrix(result)

# Das Ergebnis sollte folgende Matrix sein:
# [
# [7, 8],
# [9, 2]
# ]