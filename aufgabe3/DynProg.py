#!/usr/bin/python3
## Algorithmen und Datenstrukturen
## Hausaufgabe 3 - Dynamische Programmierung
## Abgabedatum: 12.7.2017
##
## Gruppennummer: 63
## Gruppenmitglieder:
## - Maximilian Budwill
## - Wolfgang Ost
## - Simon Christ

## ACHTUNG: Verwenden Sie für Ihre Kommentare nur ein einzelnes #-Zeichen:
# so sollte Ihr Kommentar markiert werden
## so sind die Kommentare aus der Aufgabenstellung markiert.

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

## Implementieren Sie ab hier Ihre Lösungen:
def dynCompNChooseK(n, k):
    print('Parameter n:') ## Als Ausgabe genügt es nicht, nur die Parameter und das Ergebnis auszugeben.
    print(n)
    print('Parameter k:')
    print(k)
    ## hier soll Ihre Implementierung stehen.
    result = dynCompNChooseKTable(n,k)[0][k]
    return result

def dynCompNChooseKTable(n, k):
    ## hier soll Ihre Implementierung stehen.
    # initialize with 0
    result = [[0 for i in range(0,k+1)] for j in range(0,n+1)]
    # x over 0 always 1
    for i in range(0,n+1):
        result[i][0] = 1

    # fill the table columnwise bottom-up starting at the diagonal
    for i in range(1,k+1):
        for j in range(n-i,-1,-1):
            result[j][i] = result[j + 1][i] + result[j + 1][i - 1]

    return result

## Hier ist ein Testfall:
n = 3
k = 4
result = dynCompNChooseK(n, k)
resultTable = dynCompNChooseKTable(n, k)

print('berechnet:')
print(result) ## 10

print('mit der Tabelle:')
printMatrix(resultTable)
##  #k
##[ #0  1  2  3  4  5
##  [1, 0, 0, 0, 0, 0], #n=0
##  [1, 1, 0, 0, 0, 0], #n=1
##  [1, 2, 1, 0, 0, 0], #n=2
##  [1, 3, 3, 1, 0, 0], #n=3
##  [1, 4, 6, 4, 1, 0], #n=4
##  [1, 5, 10,10,5, 1]  #n=5
##[
