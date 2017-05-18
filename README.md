# aud
Algorithmen und Datenstrukturen SoSe2017

1. Hausaufgabe : Matrizen-Multiplikation
Modalitäten
Abgabedatum: 21.5.2017 23:59 Uhr
Die Aufgabe ist in Gruppen von zwei bis maximal drei Studierenden zu erledigen. Einzelabgaben sind
nicht möglich.
Aufgabenstellung
Implementieren Sie die aus der Vorlesung bekannten Verfahren zur Matrixmultiplikation
-
-
nach Definition
nach dem Paradigma „Teile und Herrsche“ (intuitiv, nicht nach „Strassen“)
in Python 3.
Dazu laden Sie die Datei MatrixMultiplikation.py aus Moodle herunter, und implementieren die
beiden Funktionen matMultDef und matMultDC.
Stellen Sie sicher, dass Sie in Moodle in einer Abgabengruppe sind. Diese Gruppe gilt für das gesamte
Semester für alle Hausaufgaben.
Benennen Sie die Datei in <Gruppennummer>_<Nachname1>_<Nachname2>_<Nachname3>.py um,
und laden Sie diese in Moodle bei der Abgabe zu Hausaufgabe 1 hoch. (Wenn Sie nur zwei
Gruppenmitglieder sind, passen Sie den Dateinamen entsprechend an.)
Vergessen Sie nicht, Gruppennummer und Ihre Namen in der Datei in den vorgesehenen
Kommentaren einzutragen.
Die beiden Funktionen erhalten jeweils zwei Parameter: die m × n -Matrix a und die n × m-Matrix b,
die multipliziert werden sollen. Das Ergebnis der Funktion ist das Ergebnis der Matrix-Multiplikation
von a und b.
Sie sollen Ihre Berechnungen mithilfe von print – Ausgaben dokumentieren, um so die Rechenwege
und ggf. Zwischenergebnisse nachzuvollziehen. Zu diesem Zweck stellen wir Ihnen zusätzlich die
Funktion showMatrix(m) zur Verfügung, die eine gegebene Matrix ausgibt. Diese können Sie
verwenden.
Wir repräsentieren Matrizen für diese Aufgabe als geschachtelte Python-Listen, das heißt, die Matrix
a b
[ c d ] wird repräsentiert als [[a, b], [c, d], [e, f]].
