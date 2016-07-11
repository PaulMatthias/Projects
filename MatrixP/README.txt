Dies ist eine Simulation fuer einen Matrix Produktionssystem


[1] Wie benutze ich diese Simulation?

0) Kontrolliere im "sys_param.dat" file, ob die gewuenschten Systemparameter gesetzt sind (sowie maximale Laufzeit oder aehnliches 
1) Kopiere das Input File aus dem "input_files" Ordner, welches verwendet werden soll, in den Hauptordner (in den selben in der auch diese README liegt)
2) dann starte das skript mit "bash run.sh" (start aus dem terminal fuer linux systeme), exe dateien fuer windows Systeme sollten folgen
3) Auswertung sollte dann im Ordner plot/ erfolgen, indem individuelle Visualierungen gemacht werden koennen
4) Rohdaten koennen sich im Ordner out/ angeschaut werden




[2] Aktueller Entwicklungsstand der Simulation

- Arbeitszellen werden mit einem Input File initialisiert (das Format wird in read_csv.cpp beschrieben)
- Arbeitszellen koennen aktuell bis zu 2 verschiedenen Arbeitspaketen beinhalten, welche individuelle Bearbeitungszeiten besitzen
- neue Produkte werden in jedem Zeitschritt von freien Arbeitszellen mit dem Arbeitspaket 1 angefangen
- nach jedem Bearbeitungszeitschritt wird die benoetigte Zeit fuer die aktuelle Bearbeitung um 1 reduziert
- wenn die Zeit einer Arbeitszelle auf 0 sinkt, wird die arbeitszelle wieder frei und das Produkt ist einen Fertigungsschritt weiter




[3]  Aktuelle bereits implementierte Diagnostik

- Echtzeit Ueberwachung der Zellen ,die anzeigt, ob sie frei oder beschaeftigt ist
- Zeitentwicklung der Fertigungszeit pro Produkt
- Integrale Unproduktive Zeit der Arbeitszellen
- Integrale Summe der fertigen Produkte




[4] Anmerkungen
- Zurzeit fertigen die Zellen mit 2 AP weniger Produkte als mit 1 AP 
-> das sollte auf jeden Fall anders laufen...
- Vermutung: koennte daran liegen, dass die Zellen mit AP1 statt ein neues Produkt anzufangen, eher den anderen Bearbeitungsschritt vorziehen
