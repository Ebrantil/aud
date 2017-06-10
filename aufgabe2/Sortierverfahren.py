# Algorithmen und Datenstrukturen
# Hausaufgabe 2 - Sortierverfahren
# Abgabedatum: 11.6.2017
#
# Gruppennummer: 63
# Gruppenmitglieder:
# - Maximilian Budwill
# - Wolfgang Ost
# - Simon Christ

# Implementieren Sie ab hier Ihre Lösungen:

# Vertauschen der Werte an Positionen i und j in Liste L
# pre: 0 <= i, j <= len(L)-1
def chg(L,i,j):
    tmp= L[i]
    L[i] = L[j]
    L[j] = tmp

def merge( list1, list2 ):
    length1 = len(list1)
    length2 = len(list2)
    list = list1 + list2
    j = 0
    while j < length2:
        i = length1 + j
        while i > 0 and list[i-1] > list[i]:
            chg( list, i-1, i )
            i = i - 1
        if i == length1 + j: break
        j = j + 1
    return list

def combine(list):
    global result
    out = []
    length = len(list)
    if(length == 1):
        result = list[0]
        return
    if length % 2 == 1:
        for i in range( 0, length - 1, 2 ):
            out.append( merge( list[i], list[i+1] ) )
        out.append( list[length - 1] )
    else:
        for i in range( 0, length, 2 ):
            out.append( merge( list[i], list[i+1] ) )
    print( out )
    combine( out )

def divide( list ):
    global result
    length = len(list)
    if length == 1: result.append(list)
    else:
        newLength = len(list) // 2
        divide(list[:newLength])
        divide(list[newLength:])

result = []
def sortMerge(a):
    global result
    print('Parameter a:')
    print(a)
    # hier soll Ihre Implementierung des Mergesort - Verfahrens stehen.
    divide(a)  # durch das Ergebnis Ihrer Implementierung ersetzen
    print('Result after divide:')
    print(result)
    print('Combine:')
    combine( result )
    return result

def heapify(A,v,last):
    w = 2 * v + 1 # linkes Kind von v
    while(w <= last): # w ist Knoten des Baums
        if(w+1 <= last): # Gibt es ein rechtes Kind?
            if(A[w] > A[w+1]): w = w+1  # > statt < für min-heap
        # w ist Kind mit minimalem Element
        if(A[v] <= A[w]): return    # Heapeigenschaft o.k.; <= statt >= für min-heap
        # sonst:
        chg(A,v,w)
        v = w
        w = 2 * v + 1

def buildHeap(A):
    n = len(A) -1
    # fueralle inneren Knoten bottom-up
    for v in range( (n-1) // 2, -1, -1 ):
        # Heapeigenschaft wieder herstellen
        heapify(A,v,n)

def sortHeapDesc(a):
    print('Parameter a:')
    print(a)
    # hier soll Ihre Implementierung von absteigendem HeapSort stehen.
    buildHeap(a)
    last = len(a) -1
    while(last >= 1):
        # Wurzel mit letztem Blatt tauschen
        chg(a,last,0)
        # letzten Knoten aus Baum entfernen
        last = last -1
        # Heapeigenschaft wieder herstellen
        heapify(a,0,last)
    result = a  # durch das Ergebnis Ihrer Implementierung ersetzen
    return result

# Hier ist ein Testfall:
liste = [3, 2, 1, 9, 17, 4, -1, 0, 5]
mergeResult = sortMerge(liste)
heapResult = sortHeapDesc(liste)


print('berechnet:')
print(mergeResult)
print(heapResult)

# Das Ergebnis sollte folgende Liste sein:
# [-1, 0, 1, 2, 3, 4, 9, 17]
# [17, 9, 4, 3, 2, 1, 0, -1]
