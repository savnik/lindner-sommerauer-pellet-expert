# System integration

<!-- Coverage manifest (plan §7.2). Every addition to this file must update it.
model: SL-P 8 / SL-P 12 / SL-P 15 / SL-P 25 (Modell 2008; document states validity "ab Baujahr 2006")
firmware: Pell 080325.1 (as printed in page footers; see verification.md for the version discrepancy)
source document: "Betriebsanleitung Pelletsanlage SL-P 8/12/15/25, Modell 2008", SL-Technik GmbH / Lindner & Sommerauer, dated 18.04.2008 and 29.04.2008. Short name for anchors: SL-P BA 2008.
sections covered:
  Kap. 1 — Heizmaterialqualität, Pellets-Lagerraum, Kamin, Anschluss an den Kamin, Kesseltemperatur, Rücklaufanhebung, Bestimmungsgemäße Verwendung, Anwendungsbereich
  Kap. 2 — Bauteile der Anlage (Pos. 1–17 and parts without figure), including the per-component hazard notes as printed
  Kap. 3 — Beschreibung der Heizanlage, Technische Daten
  Kap. 4 — Erstinbetriebnahme, Einstellungen (general notes)
  Kap. 7 — Puffer-Betrieb (buffer as boiler, two-sensor operation, mixer assignment)
  Kap. 9 — Anschluss des Raumtemperaturfühlers, Das Raumgerät
  Kap. 13 — Zusatzparameter Service, hydraulic-relevant notes only (Boiler START vs Pumpe START, Ext.Stop d. Fremdofen, Sensor 70° Zwischenbehälter)
  Kap. 15 — Rücklaufanhebung description (mixer-controlled RLAH on M1)
  Kap. 16 — Abhilfe bei Leistungsproblemen
sections not covered:
  Kap. 1 — Einleitung, Sicherheit/Allgemeines, Gefahrenhinweise (symbols), Personalauswahl, Sicherheitshinweise im Normalbetrieb, Sicherheitshinweise Instandhaltung, Gefahr durch Hitze, Haftungsausschluss: general safety text, no target file per ingest-document step 2 — flagged for a plan decision
  Anhang — Service und Sicherheitstechnik Überprüfung (blank checklist form): not ingested
  Anhang — Putz- und Reinigungsanleitung, Wartungsbuch lt. prTRVB H 118: listed in the contents, not present in the scan
  Figures — Kap. 2 cutaway drawing, Kap. 3 system drawing, Kap. 9 room-sensor drawing: not transcribed; only the printed text and captions are
-->

<!-- Gap-marking convention (PROVISIONAL — plan §7.1 was not available when this
     file was first filled; replace with the plan's convention when supplied):
     a blockquote starting with "GAP:" marks a place where the source is silent,
     cut off, illegible, or skipped per the ingest-document first rule, e.g.
     > GAP: [what is missing] — [why]. See verification.md line N.
-->

<!-- Anchor format (provisional): [SL-P BA 2008, Kap. N, S. M] = chapter N, page M
     as printed in the page footer. The manual's own wording is kept in German;
     English headings in parentheses are glosses only. Printed example values on
     display boxes are the manual's examples, not any installation's values
     (Kap. 4, S. 3: "Angaben sind typische Werte und können von Ihrem Display
     abweichen!"). Handwritten annotations in the scanned copy are not
     transcribed. The "Anlagenwert" column of every parameter list is omitted
     for the same reason. -->

---

## Kap. 1 — Allgemeine Hinweise (general notes relevant to installation)

### Bestimmungsgemäße Verwendung (intended use) [SL-P BA 2008, Kap. 1, S. 2]

Der Pelletskessel dient zum Beheizen von Wohnräumen. Als Brennmaterial sind nur Pellets erlaubt, die der ÖN M7135 oder einer vergleichbaren nationalen Norm (DIN) entsprechen. **Für den Betrieb dürfen nur Pellets mit 6mm Durchmesser verwendet werden.** Für Schäden durch unsachgemäße Nutzung und Aufstellung wird keine Haftung übernommen. Für einen umweltschonenden und sicheren Betrieb wird der Abschluss eines Wartungsvertrages empfohlen.

### Anwendungsbereich (scope) [SL-P BA 2008, Kap. 1, S. 3]

Die nachfolgende Betriebsanleitung gilt für den Pelletskessel SL-P ab Baujahr 2006.

Die Heizanlage ist entsprechend EN 303-5 „Heizkessel für feste Brennstoffe, automatisch beschickte Feuerungen, Nennwärmeleistung bis 300 kW" geprüft. (Haftungsausschluss, same page.)

### Heizmaterialqualität (fuel quality) [SL-P BA 2008, Kap. 1, S. 4]

Ihre Pellets-Heizanlage ist für die Verfeuerung von Pellets **Durchmesser 6mm** entsprechend ÖNORM M 7135-Teil 1, DIN 51731, DIN Plus sowie PVA-Pellets (Gütezeichen des Österr. Pelletsverbandes) geeignet. Garantieansprüche gelten nur bei Verwendung des angegebenen Heizmaterials.

### Pellets-Lagerraum (pellet store) [SL-P BA 2008, Kap. 1, S. 4]

Der Lagerraum soll eine längliche Form haben um eine größtmögliche Austragung des Materials aus dem Lagerraum zu erreichen.

Bei der Einbringung der Pellets ist darauf zu achten, dass diese gegen eine Prallwand geblasen werden und das Heizmaterial ohne Beschädigung in den Lagerraum rieselt. Als Prallwandschutz hat sich eine harte Gummimatte bewährt. Beim Befüllen des Lagerraumes ist darauf zu achten, dass sämtliche Öffnungen des Bunkers dicht geschlossen sind (Gummidichtungen) und die Wartungstüre von innen mit einer Bretterwand geschützt ist.

### Kamin (chimney) [SL-P BA 2008, Kap. 1, S. 4]

Ein vorschriftsmäßiger, vom Kaminkehrer überprüfter und der Kesselleistung angepasster Kamin ist Voraussetzung für einen einwandfreien Betrieb der Anlage. Bitte berücksichtigen Sie, dass im unteren Leistungsbereich Abgastemperaturen unter 90°C entstehen können. Die Anlage ist deshalb an einem feuchtigkeitsunempfindlichen Kamin anzuschließen. Das Verbindungsrohr muss unbedingt dicht ausgeführt und stabil befestigt sein.

### Anschluss an den Kamin (chimney connection, draught regulator) [SL-P BA 2008, Kap. 1, S. 4–5]

Da die Anlage mit einem drehzahl-geregelten Saugzuggebläse betrieben wird, ist für den Abtransport des Rauchgases nur mehr ein Kaminzug von 7 bis 10 Pascal notwendig. Laut TRVB-H118 ist in der Einbindung vom Kessel zum Kamin eine Verpuffungsklappe (Explosionsklappe) vorzusehen. Bei einem Kaminzug über 10 Pascal Unterdruck ist diese als Kombi – Energiesparzugregler mit Explosionsklappe auszuführen. Das Einstellen des Energiesparzugreglers ist nur sinnvoll bei Außentemperaturen unter +5°C, dabei sollte die Anlage schon mindestens 1 Stunde in Betrieb sein. Vor der Messung unbedingt darauf achten, dass die Anlage im Nennlastbereich läuft. Förderdruck zwischen Kessel und Energiesparzugregler messen (Abstand der Messöffnung zum Kessel möglichst 3 x Rauchrohrdurchmesser). Danach muss der Energiesparzugregler auf den jeweiligen Wert eingestellt werden. (Hinweis: Kaminzug verändert sich mit veränderter Leistung). Ein zu hoher Förderdruck beschleunigt die Verbrennung. Die Abgastemperatur wird künstlich erhöht. Schlechte Leistungsanpassung und vermehrter Auswurf von Staub ist die Folge. Ein zu niedriger Förderdruck führt zu Leistungsproblemen und unvollständigem Verbrennungsverhalten!

### Kesseltemperatur (boiler temperature) [SL-P BA 2008, Kap. 1, S. 5]

Der Kessel sollte mindestens eine Temperatur von 70°C erreichen. Übersteigt die Kesseltemperatur 90°C, so schalten sich alle Pumpen ein, außerdem regelt der Mischer auf maximale Vorlauf-Temperatur. Dies bewirkt, dass die im Brenner noch vorhandene Restenergie ohne Übertemperaturmeldung abgeführt wird. Der Übertemperaturschutz (STB) tritt ab 100°C in Kraft.

### Rücklaufanhebung (return temperature raising) [SL-P BA 2008, Kap. 1, S. 5]

Der Heizkessel sollte im Betrieb eine Temperatur von mind. 50° erreichen. Durch eine integrierte Rücklaufanhebung wird der Kessel gleichmäßig durchspült und dadurch eine Korrosion der Kesselinnenwände verhindert. Nur bei Systemen mit Puffer/Boiler über 1000L ist eine Rücklaufanhebung in der Hydraulik einzuplanen. Diese ist auf 55° einzustellen.

> GAP: The 55° figure here differs from the 63°C "Standard" for "Rücklauf SOLL" in the Kap. 15 parameter list — source inconsistency, not resolved here. See verification.md.

---

## Kap. 2 — Bauteile der Anlage und Gefahrenhinweise (components) [SL-P BA 2008, Kap. 2, S. 1–4]

Nachstehend finden Sie die wichtigsten Bauteile der Anlage und einen entsprechenden Gefahrenhinweis. Position numbers refer to the cutaway drawing on Kap. 2, S. 1 (drawing not transcribed).

**Rauchrohr (Pos.1)** — Das Rauchrohr leitet die Abgase zum Kamin. Es ist mit einem Energiespar-Zugregler bauseits auszustatten. Das Rauchrohr erwärmt sich im Normalbetrieb weit über 100°C. Es besteht daher akute Verbrennungsgefahr. Es empfiehlt sich, das Rauchrohr mit einer hitzebeständigen Isolierung zu versehen. [S. 1]

**Display (Pos.2)** — Bedieneinheit für die gesamte Anlage. [S. 1]

**AUS-Schalter (Pos.3)** — Beim Ausschalten mit diesem Schalter wird die ganze Anlage abgeschaltet. Auch die Pumpen und die Heizkreisregelung! ACHTUNG: Die Module (Mischer, Pumpen) sind separat angeschlossen und stehen daher noch unter Strom!! [S. 1]

**Saugzugventilator (Pos.4)** — Der Saugzugventilator ist in den Wärmetauscher-Deckel integriert. Der Ventilator wird mit 230 V betrieben. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! [S. 2]

**Reinigungsmechanik (Pos.5)** — Die Putzfedern reinigen den Wärmetauscher bei jedem Reinigungsvorgang vollautomatisch. Bauteile: Reinigungsmotor, Reinigungswelle, Aufhängung für Reinigungsfedern, Reinigungsfedern mit Innenrohr. Der Reinigungsmotor wird mit 230 V betrieben. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! Der Reinigungsvorgang läuft automatisch ab, daher nicht in die Mechanik greifen! [S. 2]

**Wärmetauscher (Pos.6)** — Der Wärmetauscher dient zur Aufnahme der Wärme und Umsetzung in den Heizkreis. Besondere Gefahren: Der Wärmetauscher ist mit einer Sicherheitsgruppe auszustatten. Um Schäden zu vermeiden, ist im Heizsystem ein Ausdehnungsgefäß einzubauen. [S. 2]

**Pelletsrutsche (Pos.7)** — Über die Pelletsrutsche gelangen die Pellets in die Brennkammer. Wenn die Pelletsrutsche ausgebaut ist, nicht in den Stockerkanal greifen. Es besteht Quetschgefahr! [S. 2]

**Brennertopf unten (Pos.8)** — Hier werden die Pellets verbrannt. Der Brennertopf ist während des Betriebes sehr heiß. Vor Wartungsarbeiten unbedingt abkühlen lassen. [S. 2]

**Anzünder (Pos.9)** — Der Anzünder dient zum Entzünden der Pellets. Der Anzünder wird mit 230 V betrieben. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! Achtung: Der Anzünder erreicht über 1000°C. Verbrennungsgefahr beim Ausbau! [S. 3]

**Drehrost (Pos.10)** — Öffnet die Brennkammer nach unten zur Aschenlade während des Reinigungsvorganges. Wenn die Brennkammer nach unten zur Aschenlade während des Reinigungsvorganges geöffnet wird und die Aschenanlage herausgezogen ist, besteht die Möglichkeit, in die Öffnung zu greifen. Es besteht daher Quetschgefahr! [S. 3]

**Aschelade (Pos.11)** — Nimmt die Verbrennungsasche auf. Heiße Asche kann zu Verbrennungen führen. [S. 3]

**Stockerschnecke (Pos. 12)** — Die Stockerschnecke fördert die Pellets in die Brennkammer. [S. 3]

**Putzmotor (Pos. 13)** — Betätigt die Putzschwinge. Bestandteile: Putzmotor, Putzgestänge. Der Putzmotor wird mit 230V betrieben. Reparaturen dürfen nur vom Fachmann durchgeführt werden. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! [S. 3]

**Stockermotor (Pos. 14)** — Der Stockermotor treibt die Stockerschnecke an. Über Zahnräder wird auch die Zellradschleuse mitbetrieben. Bauteile: Stockermotor, Motorhalterung, Zahnräder. Der Stockermotor wird mit 230V betrieben. Reparaturen dürfen nur vom Fachmann durchgeführt werden. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! Achtung: Quetschgefahr bei den Zahnrädern! [S. 3]

**Zellradschleuse (Pos.15)** — Die Zellradschleuse ist eine Brandschutzeinrichtung. Sie trennt den Stockerkanal vom Vorratsbehälter. Stecken Sie keine Gegenstände von oben durch den Behälter in die Zellradschleuse, da sie dadurch beschädigt werden kann. [S. 4]

**Zwischenbehälter (Pos. 16)** — In den Zwischenbehälter werden die Pellets gesaugt. [S. 4]

**Saugturbine (Pos. 17)** — Sie dient zum Erzeugen des Unterdruckes im Saugbehälter. Die Saugturbine wird mit 230V betrieben. Reparaturen dürfen nur vom Fachmann durchgeführt werden. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! [S. 4]

**Saugschlauch (ohne Abb.)** — Der Saugschlauch leitet die Pellets über den Saug-Misch-Verteiler zum Zwischenbehälter. Es darf nur ein mit einer Erdungslitze ausgestatteter, von SL-Technik mitgelieferter Saugschlauch verwendet werden. Es dürfen keine Stoffe eingesaugt werden, die den Saug-Misch-Verteiler oder den Kessel Schaden zufügen könnten. [S. 4]

**Saug-Misch-Verteiler (ohne Abb.)** — Dient zum Wechseln zwischen den einzelnen Absaugpunkten. Bauteile: Umschaltklappen, Stellmotore. Die Stellmotoren werden mit 230V betrieben. Reparaturen dürfen nur vom Fachmann durchgeführt werden. Vor Beginn der Wartungsarbeiten muss die Anlage vom Stromnetz getrennt werden! [S. 4]

**Ansaugdüsen (ohne Abb.)** — Die Ansaugdüsen dienen zur Aufnahme der Pellets im Lagerraum. Es können bis zu 4 Düsen in den Lagerraum eingebaut sein. Die Düsen sind am Lagerraumboden anzuschrauben. [S. 4]

---

## Kap. 3 — Beschreibung der Heizanlage (system description) [SL-P BA 2008, Kap. 3, S. 1–2]

Drawing on S. 1 (not transcribed) shows: Heizraum with the boiler, VL/RL connections, Förderschlauch 2" antistatisch, Saug-Misch-Verteiler, and the Brennstofflagerraum with Ansaugdüse. Numbered items in the text refer to that drawing.

Der Brennstoff wird über Ansaugdüsen (1) aus dem Lagerraum gesaugt. Über einen Saug-Misch-Verteiler (2) werden mehrere Saugeinheiten zu einem Förderschlauch (3) und einem Rückluftschlauch (4) zusammengefasst.

Am anderen Ende befinden sich das Saugaggregat und ein Tagesbehälter (5). Über die rückbrandsichere Zellradschleuse (RSE) (6) gelangen die Pellets zur Stockerschnecke (7), die sie in den Brennraum fördert. Die Stockerschnecke ist mit der Zellenradschleuse über Zahnräder verbunden. Das gesamte Fördersystem besteht aus einem Getriebemotor (8) und einem Saugaggregat.

Die Pellets gelangen über die Pelletsrutsche (9) in den unteren Brennertopf (10) und werden dort verbrannt.

Die Konstruktion erlaubt in Verbindung mit den im Röhrenwärmetauscher befindlichen und über ein Hebelsystem bewegten Reinigungsfedern (11) eine vollautomatische Reinigung des Wärmetauschers und des Brenners.

Die bei der Verbrennung und Reinigung anfallende Asche fällt in die unterhalb des Brenners liegende Aschenlade (12), welche im Winter monatlich zu entleeren ist.

Die Zündung des Brenners erfolgt mittels Glühstab (13).

Die Verbrennungsluft wird durch den Außenbereich des Kessels angesaugt und verteilt als Primär- und Sekundärluft der Verbrennung zugeführt. Dies geschieht mittels eines Drehzahl-geregelten Saugzuggebläses (14).

Die Verbrennungsüberwachung erfolgt durch die Lambdasonde, die auf die Brennstoffzufuhr und auf das Saugzuggebläse eingreift. Die Leistungsregelung arbeitet gleitend, wobei die Kesselwassertemperatur als Maßstab dient.

Der Kessel ist mit einer integrierten Rücklauftemperaturanhebung ausgestattet.

Die Steuerung der Anlage übernimmt eine Steuerung neuester Bauart (Programm tauschbar über Schnittstelle RS232 oder CAN-BUS).

Als Betriebsarten stehen Dauerbetrieb, Uhrzeitbetrieb (z.B. zweimal täglich starten), Boilerbetrieb (startet Anlage bei Absinken der Boilertemperatur automatisch), Uhr – Boilerbetrieb (in Verbindung mit Solaranlage) zur Verfügung. [S. 2]

### Technische Daten (technical data) [SL-P BA 2008, Kap. 3, S. 3]

| | SL-P 8 | SL-P 12 | SL-P 15 | SL-P 25 |
|---|---|---|---|---|
| Nennleistung (kW) | 7,9 | 12 | 14,9 | 23,5 |
| Leistungsbereich | 2,4-7,9 | 2,5-12 | 3,9-14,9 | 3,9-23,5 |
| Wirkungsgrad (Nennleistung) | 95 | 95,2 | 94,6 | 93,2 |
| Wirkungsgrad (kleinste Leistung) | 91,6 | 91,6 | 93,8 | 93,8 |
| Breite | 1080 | 1080 | 1080 | 1080 |
| Tiefe | 730 | 730 | 730 | 730 |
| Höhe | 1500 | 1500 | 1500 | 1500 |
| Gewicht mit eingeb. Brenner | 350 | 350 | 350 | 350 |
| Wasserinhalt (Liter) | 43,6 | 43,6 | 43,6 | 43,6 |
| Wasserseitiger Widerstand (k10/k20) (mbar) | 13,5/3,4 | 13,5/3,4 | 13,5/3,4 | 13,5/3,4 |
| Rauchrohranschluss (mm) | 130 | 130 | 130 | 130 |
| Rauchrohr | nach oben | nach oben | nach oben | nach oben |
| Dm Vor/Rücklauf (Zoll) | 1" | 1" | 1" | 1" |
| Vorlauf | nach oben | nach oben | nach oben | nach oben |
| Rücklauf | nach oben | nach oben | nach oben | nach oben |
| Einstellung Temperaturregler (STB) | 100° | 100° | 100° | 100° |
| Abgasmassenstrom Nennl./Teill. (g/s) | 5/3 | 7/3 | 8/4 | 13/6 |
| notw. Förderdruck 160°C (mbar) | 0,07/0,1 | 0,1/0,1 | 0,1/0,07 | 0,1/0,07 |
| Abgastemperatur Nenn / Teillast | 165/115 | 165/115 | 165/115 | 165/115 |
| Kohlendioxid Nenn/Teillast (%) | 13,1 / 10,8 | 14,2 / 10,8 | 14,5 / 10,5 | 14,2 / 10,5 |
| Aschenlade vorne (Liter) | 20 | 20 | 20 | 20 |
| Elektr. Anschluss | 230V ; 10A ; 50 Hz (all models) | | | |
| Anzünder (W) | 300 | 300 | 300 | 300 |
| Saugzug (W) | 32 | 32 | 32 | 32 |
| Stromaufnahme Wh / 360min | 130 | 220 | 220 | 390 |
| Strom in % zur NL / 360 min | 0,4 | 0,3 | 0,2 | 0,3 |

> GAP: Units for Breite/Tiefe/Höhe and Gewicht are not printed on the page (presumably mm and kg, but the manual does not say). See verification.md.

---

## Kap. 4 — Erstinbetriebnahme (first commissioning) [SL-P BA 2008, Kap. 4, S. 2]

Um Garantieansprüche auf die Anlage nicht zu verlieren, darf die Heizung ausschließlich von einer befugten Person, anhand der in der Betriebanleitung enthaltenen Inbetriebnahme-Checkliste (Dreifache Ausfertigung), das erste Mal in Betrieb genommen werden. Eine Checkliste ist vom Kunden mit Unterschrift zu bestätigen und innerhalb von acht Tagen an die Herstellerfirma zu senden!

> GAP: The Inbetriebnahme-Checkliste referred to here is not in the scan (only the Anhang "Service und Sicherheitstechnik Überprüfung" form is).

Bei der Erstinbetriebnahme muss manuell der Zwischenbehälter mit Pellets gefüllt werden. Dazu gehen Sie in das Menü Dauerbetrieb, blättern dort bis zum Parameter „Saugen/Putzen" und starten mit „+" den Saugvorgang. Ist der Zwischenbehälter gefüllt, wechseln Sie in den Handbetrieb und starten mit der „+" das Menü „Brenner füllen". Es werden Pellets aus dem Zwischenbehälter in den Brenner gefördert. Die Funktion „Brenner füllen" sollte 2 bis 3 mal gestartet werden, bis die ersten Pellets in den Brennraum fallen. Mit „-" stoppen Sie die Stockerschnecke wieder.

Anschließend drückt man die Taste DAUERBETRIEB und startet die Anlage durch drücken der Taste „Ein". Es beginnt nun der automatische Zündvorgang. Dies erkennt man durch das abwechselnde Blinken der roten und grünen Kontrollleuchte der Tasten „Ein" bzw. „Aus". Das Saugzuggebläse regelt ab jetzt in mehreren Schritten bis zur eingestellten Startdrehzahl. Danach beginnt die Stockerschnecke mit der eingestellten Startförderzeit Pellets in den Brenner zu fördern, zugleich läuft der Anzünder (Glühstab) und versucht das Heizmaterial zu zünden.

Sobald die Anlage in den Regelbetrieb wechselt leuchtet nur mehr die grüne Leuchte der „Ein" Taste.

### Einstellungen (general note on settings) [SL-P BA 2008, Kap. 4, S. 3]

Achtung: Einige Werte für die Grundeinstellung der Heizanlage können nur im **Dauerbetrieb** geändert werden. Sollte die Anlage z.B. im **Uhrzeitbetrieb** laufen, ist die Anlage auf **Dauerbetrieb** umzuschalten; die Werte können so verändert werden. Anschließend wechseln sie wieder in den **Uhrzeitbetrieb**.

Angaben sind typische Werte und können von Ihrem Display abweichen! Notieren Sie sich die für Sie passenden Werte in der Parameterliste. Bei einem Tausch der Software müssen diese Werte wieder von Hand eingegeben werden.

Die Heizanlage kann in einigen Punkten an das Heizsystem angeglichen werden, passen Sie die verschiedenen Werte Ihren Anforderungen an. Bei der Erstinbetriebnahme wird diese Arbeit von unserem Service-Techniker für Sie erledigt.

---

## Kap. 7 — Puffer-Betrieb (buffer tank as "Boiler") [SL-P BA 2008, Kap. 7, S. 1–3]

Es können je nach Anzahl der installierten Module serienmäßig bis zu 24 Boiler bedient werden. In den jeweiligen Boiler muss ein Temperaturfühler (PT 100) eingebaut werden. [S. 1]

ACHTUNG: Im „Boilerbetrieb" ist die Rücklaufanhebepumpe an die Boilerladepumpe gebunden und schaltet erst mit Erreichen der „Boilerfreigabe Temp." ein, bei Erreichen der „Boiler-Soll Temp." mit einer Verzögerung von 300 sec. wieder aus. Somit wird verhindert, dass die RLAH-Pumpe den Puffer wieder entleert. [S. 1]

Die Anlage unterscheidet nicht, ob es sich um einen Brauchwasserboiler oder einen Pufferspeicher handelt. Es kann jeder erste Boileranschluß im Modul (B1, B4, B7,…B22) als Pufferspeicher genutzt werden. In der Regel werden Pufferspeicher mit 2 Fühlern (oben Ein-, und unten Aus-Temperatur) ausgestattet. Dies ist der Anlage in den „Zusatzparametern Service" mitzuteilen (z.B.: „Boiler 1 mit 2 PT 100"). Somit ist im Modul am B1-Anschluß der „Fühler oben" anzuschließen und am B2-Anschluß der „Fühler unten". [S. 2]

Ist Boiler 1 auf 2 Fühler eingestellt (Zusatzparameter Service), so kann unter B1 nur mehr die „Start" Temperatur eingestellt werden. Die Boiler (Puffer) „Soll-Temperatur" ist unter B2 einzustellen. Am „B2" ist nur die „Boiler SOLL" Temperatur einzustellen. [S. 2]

Für den Betrieb als Pufferspeicher müssen jetzt nur noch die Mischkreise dem Pufferspeicher zugeordnet werden. Auch diese erfolgt in den Zuatzparametern Service: Durch das aktivieren der Funktion „Solar" sind die ausgewählten Mischkreise dem jeweiligen Pufferspeicher zugeordnet. [S. 3]

Für diese gilt somit nicht mehr die Kesseltemperatur als Indikator, sondern die Puffertemperatur, d.h. die Heizkreise entnehmen so lange dem Pufferspeicher die Energie, bis die „Boiler Start" Temperatur unterschritten wird. Erst dann startet der Kessel und lädt den Puffer wieder auf. [S. 3]

**Achtung:** Die Freigabetemperatur der Heizkreispumpe „Heizung Pumpe AUS bei __°" (Menü Außentemperaturregelung) muss niedriger sein als die „Boiler Start Temperatur". Die jeweilige „Start" - und „Soll" - Temperaturen sind dem Heizsystem und dem Puffertyp anzupassen. [S. 3]

Related rule from Kap. 13, S. 4: Die „Boiler START" Temperatur (Fühler oben) muss höher sein als die „Pumpe START" Temp. des entsprechenden Mischkreises. Sonst steht die Pumpe. Der Kessel heizt bei erreichter überschrittener „Boiler START" Temp. nicht!! [SL-P BA 2008, Kap. 13, S. 4]

The corresponding menu items and parameter ranges are in parameters.md (Kap. 7, Kap. 13).

---

## Kap. 9 — Raumgerät und Raumtemperaturfühler (room unit and sensor)

### Anschluss des Raumtemperaturfühlers (wiring) [SL-P BA 2008, Kap. 9, S. 4]

Der Fühler ist in den Modulen (GM+AT1, GM+AT2, EM2 od. EM4) dem jeweiligen Heizkreis zugeordnet anzuschließen. Es können einem Raumgerät mehrere Heizkreise zugeordnet werden. Es ist an den Kontakten 1 und 2 anzuschließen.

Drawing on the same page gives the room unit dimensions as 26 × 79 × 81 (and 26 depth) — no unit printed. > GAP: unit not printed on the drawing; presumed mm but not stated. See verification.md.

Wird eine mischergesteuerte Rücklaufanhebung montiert, so ist für diese immer Heizkreis 1 (M1) zu verwenden. [S. 4]

### Das Raumgerät (room unit) [SL-P BA 2008, Kap. 9, S. 2–3]

Mit dem Raumgerät können Sie einige Funktionen der Außentemperaturregelung direkt beeinflussen.

ACHTUNG: Ist ein Raumgerät an die Anlage angeschlossen, so haben Einstellungen an diesem Vorrang gegenüber Einstellungen, die direkt an der Anlage vorgenommen werden. Das heißt, wird das Raumgerät auf **Nachtabsenkung aktiviert** (C) geschaltet, so kann dieser Mischkreis direkt an der Anlage nicht auf **Normalbetrieb** umgeschaltet werden. Die Betriebsart „Uhrzeit Betrieb" ist gänzlich deaktiviert, verwenden Sie für Zeitschaltungen die Parameter „HZ-Nachtabschaltung" EIN bzw. AUS am Ende des Menüs Außentemperaturregelung. [S. 2]

Switch positions (drawing on S. 2): A: Pumpe Aus, B: Boilerbetrieb, C: Nachtabsenkung aktiviert, D: Normalbetrieb, E: Nachtabsenkung deaktiviert, F: Temperaturwahlschalter. [S. 2]

zu A: Pumpe Aus: Hier können Sie die Ihrem Heizkreis zugeordnete Pumpe ausschalten. Sind alle Heizkreispumpen auf AUS, so schaltet die Anlage ab. Achtung: Ist das Raumgerät auf AUS, kann die Pumpe direkt an der Anlage nicht eingeschaltet werden! [S. 3]

zu B: Boilerbetrieb: Mit dieser Funktion schalten Sie die Anlage auf Boilerbetrieb. Achtung: Die Heizkreise sind auf AUS geschaltet! [S. 3]

zu C: Nachtabsenkung aktiviert: Die Anlage senkt sofort die errechnete „Vorlauf SOLL" Temperatur um den unter „Vorlaufabsenkung" eingestellten Wert ab. Die in der Außentemperaturregelung eingestellten Absenkzeiten sind somit ungültig. Auch hier kann es nicht direkt an der Anlage deaktiviert werden. [S. 3]

zu D: Normalbetrieb: Mit dieser Funktion (wird am häufigsten einzusetzen sein) läuft die Anlage nach allen unter Außentemperaturregelung eingestellten Parametern. Alle direkt an der Anlage vorgenommenen Einstellungen haben volle Wirkung. [S. 3]

zu E: Nachtabsenkung deaktiviert: Die eingestellten Zeitfenster der Nachtabsenkung haben keine Wirkung. Die Anlage läuft nach der errechneten „Vorlauf SOLL" Temperatur. ACHTUNG: Bei den Schaltungen C, D und E schaltet die Anlage automatisch in den Dauerbetrieb!! [S. 3]

zu F: Temperaturwahlschalter: Mit diesem Drehschalter können Sie die gewünschte Raumtemperatur direkt beeinflussen, indem der gemessene Wert um ca. +/- 5°C verfälscht wird. Über die errechnete Vorlaufkurve und den gewählten Raumeinfluss senkt bzw. erhöht die Anlage die „Vorlauf SOLL" Temperatur. Achtung: Bei Raumeinfluss 0% hat dies keine Wirkung! Zum Erstellen der Heizkurven ist der Temperaturwahlschalter auf neutral zu stellen!! [S. 3]

---

## Kap. 13 — Service-level notes with hydraulic relevance [SL-P BA 2008, Kap. 13, S. 1, S. 4]

Der Ausgang 6 kann für einen externen Austragungsmotor (z.B.: Erdtankschnecken...) verwendet werden. Hier können lt. Zulieferer die max. Ströme eingestellt werden. Der Ausgang wird getaktet!! (125sec EIN, 10 sec. AUS). Der Ausgang wird sofort bei erreichen der „Vollmeldung" im Zwischenbehälter abgeschaltet. Die Saugturbine hat 10 sec. Nachlaufzeit. [S. 1]

Ext.Stop d. Fremdofen: Über einen Abgassensor im Rauchrohr eines "Zweitofens" kann die Heizkreisregelung auch bei kaltem Kessel betrieben werden (Heizkreispumpe EIN bei „Kesseltemperatur" wird umgangen). AUS= „Zweitofen" kalt – unser Kessel startet bei Anforderung. EIN = „Zweitofen" heiß – unser Kessel übernimmt Wärmeverteilung. [S. 4]

Sensor 70° Zwischenb: Am Ausgang 16 kann auch ein 70° Sensor installiert werden. (Schweiz). Nur wenn der „70° Sensor" am Zwischenbehälter anspricht wird der Alarmausgang in den Modulen beschaltet. Alle weiteren Fehler die normalerweise Alarm auslösen werden unterdrückt. [S. 4]

The Extern Start (Direkt / Impuls) behaviour is in parameters.md, Kap. 13.

---

## Kap. 15 — Rücklaufanhebung, mischergeregelt (mixer-controlled return raising) [SL-P BA 2008, Kap. 15, S. 1]

Wird die Rücklaufanhebung nicht thermisch, sondern mit einem Dreiwegemischer + Stellmotor geregelt, muss dafür der 1. Heizkreis verwendet werden. Man drückt dazu die Außentemperatur - Reg. Taste und definiert die mit der +/- Taste M1 als Rücklaufanhebung. Überprüfen kann man das im Zusatzparameterbereich „Hausanlage". Auf Drehrichtung des Mischers achten! AUF ➜ in den Heizkreis Offen ; ZU ➜ zum Heizkreis geschlossen = kleiner Kreislauf.

Rücklaufanhebung Pumpe EIN bei 40° (display example): Bei dieser Kesseltemperatur schaltet sich die Rücklaufanhebung ein. Rücklaufanhebung Pumpe AUS bei 110° (display example): Bei dieser Kesseltemperatur schaltet die Rücklaufpumpe aus. Um ein Überhitzen des Kessels zu vermeiden, diese Einstellung nicht verändern!!

Parameter ranges (Rücklauf SOLL, RL-Pumpe EIN/AUS bei) are in parameters.md, Kap. 15.

---

## Kap. 16 — Abhilfe bei Leistungsproblemen (remedies for output problems) [SL-P BA 2008, Kap. 16, S. 1]

| Ursache | Abhilfe |
|---|---|
| „Kessel Soll" und „Kessel MIN" Temp. zu niedrig eingestellt. | Im Dauerbetrieb „Kessel-Soll" und „Kessel MIN" Temperatur erhöhen. |
| Kessel und Rauchgaswege nicht gereinigt. | Hat der Kessel eine sehr niedrige Abgastemperatur, so ist anzunehmen, dass die Kesselreinigung nicht ausreichend ist (siehe Putz und Service-Anleitung sowie Kontrolle der Rauchgaswege nicht vergessen, siehe Anhang der Betriebsanleitung). |
| Kontrolle der Installation (Hydraulik). | Wenn die Beheizung unzureichend ist, zuerst kontrollieren, ob die Wärmeerzeugung (Kessel), oder die Wärmeverteilung (Pumpen – Mischer) schuld sind. Bei Unklarheiten, Kontakt mit Ihrem ausführenden Installateur aufnehmen. |
| Minderwertige Pelletsqualität (Staubanteil zu hoch, Pressdichte) | Um energiewirtschaftlich eine vernünftige Lösung zu erreichen, sollte man sich unbedingt an die vorgegebenen Normheizmaterialien halten. |

> GAP: The "Putz und Service-Anleitung" referred to in row 2 is listed in the contents as an Anhang but is not in the scan.
