# System integration

<!-- Coverage manifest (plan §7.2). Every addition to this file must update it.
model: SL-P 8 / SL-P 12 / SL-P 15 / SL-P 25 (Modell 2008; document states validity "ab Baujahr 2006")
firmware: Pell 080325.1 (as printed in page footers; see verification.md for the version discrepancy)
source document: "Betriebsanleitung Pelletsanlage SL-P 8/12/15/25, Modell 2008", SL-Technik GmbH / Lindner & Sommerauer, dated 18.04.2008 and 29.04.2008. Short name for anchors: SL-P BA 2008.
source document 2: "Putz- und Reinigungsanleitung", Lindner & Sommerauer Heizanlagenbau, one page, undated, no model designation printed (supplied as the Anhang the BA 2008 contents page lists). Short name for anchors: L&S Putzanleitung.
source document 3: "pr TRVB H 118 – Ausgabe 2003", Anhang 2 (Kontrollbuch), pages 26–29 of that directive, supplied as the "Wartungsbuch" Anhang of BA 2008. Not manufacturer content; generic to automatic wood-firing systems. Short name for anchors: TRVB H 118 (2003).
source document 4: "Montageanleitung SL-P", Lindner & Sommerauer, Stand 05-2009, 12 unpaginated pages; technical-data table lists SL-P 8 / 12 / 15 / 25; no firmware stated. Short name for anchors: SL-P MA 2009. Page numbers in anchors are scan pages because none are printed.
source document 5: "Inbetriebnahme – Protokoll", Lindner & Sommerauer Biomasse-Heizanlagen / SL-Technik GmbH, one-page form, form no. 9.90.420, undated as a form, covers Brennschüsselanlage / Drehrostanlage / Pelletsanlage. Short name for anchors: L&S IB-Protokoll.
source document 6: "Prüfbescheinigung / Test Certificate / Prøvningsattest" no. 2209092-2-DK, TÜV SÜD Landesgesellschaft Österreich, 21 September 2009, type SL-P 12 only. Short name for anchors: TÜV 2209092-2-DK.
source document 7: "Raumfernfühler mit Sollwertkorrektur und Betriebswahlschalter RTFH4", EAP electric GmbH, one-page datasheet, undated. Third-party component; no boiler model printed. Short name for anchors: EAP RTFH4.
sections covered:
  Kap. 1 — Sicherheit/Allgemeines, Gefahrenhinweise, Sicherheitshinweise im Normalbetrieb, Sicherheitshinweise Instandhaltung, Gefahr durch Hitze, Personalauswahl (S. 1–3)
  Kap. 1 — Heizmaterialqualität, Pellets-Lagerraum, Kamin, Anschluss an den Kamin, Kesseltemperatur, Rücklaufanhebung, Bestimmungsgemäße Verwendung, Anwendungsbereich
  Kap. 2 — Bauteile der Anlage (Pos. 1–17 and parts without figure), including the per-component hazard notes as printed
  Kap. 3 — Beschreibung der Heizanlage, Technische Daten
  Kap. 4 — Erstinbetriebnahme, Einstellungen (general notes)
  Kap. 7 — Puffer-Betrieb (buffer as boiler, two-sensor operation, mixer assignment)
  Kap. 9 — Anschluss des Raumtemperaturfühlers, Das Raumgerät
  Kap. 13 — Zusatzparameter Service, hydraulic-relevant notes only (Boiler START vs Pumpe START, Ext.Stop d. Fremdofen, Sensor 70° Zwischenbehälter)
  Kap. 15 — Rücklaufanhebung description (mixer-controlled RLAH on M1)
  Kap. 16 — Abhilfe bei Leistungsproblemen
  Anhang — Putz- und Reinigungsanleitung (cleaning intervals per component, cleaning method)
  Anhang — TRVB H 118 Anhang 2/2: Regelmäßige Kontrolle (weekly, monthly, maintenance intervals)
  SL-P MA 2009 — all 12 pages: Allgemeine Hinweise, Lieferumfang, Zubehör, Der Pelletsraum, Heizraum/Lagerraum/Kamin, Einbau von Einblasrohren und Prallmatte, Befüllrohre durch andere Räume, Montage der Ansaugdüsen, Wanddurchbruch, Saug-Misch-Verteiler, Kessel (Anlieferung, dismantling, Aufstellen), Technische Daten, Anschluss an den Kamin, Elektrischer Anschluss, Hauptsteuerung terminal list, Verbindung zum Saug-Misch-Verteiler
  L&S IB-Protokoll — the blank form's sections and check items
  TÜV 2209092-2-DK — test basis and results for SL-P 12
  EAP RTFH4 — Anwendung, Technische Daten, Grundeinstellung resistance table, connection captions
sections not covered:
  Kap. 1 — Einleitung (greeting and blank technician phone field), Personalauswahl und Qualifikation beyond the one sentence quoted: not ingested
  Anhang — Service und Sicherheitstechnik Überprüfung (blank checklist form): not ingested
  Anhang — TRVB H 118 Anhang 2/1, 2/3, 2/4 (Kontrollbuch cover form, filled sample form marked MUSTER, blank monthly form): forms, not transcribed; only their field names are listed
  SL-P MA 2009 — drawings and photos (store layouts, wall-opening drawing, distributor drawing, dismantling photos, board layout): only printed captions, labels and dimensions transcribed; wire colours on the board drawing transcribed after a full-resolution re-read
  L&S IB-Protokoll — the filled-in entries of the scanned copy (operator, address, installer, serial number, output, which boxes were ticked, date, signatures): installation-specific, omitted
  TÜV 2209092-2-DK — signatory and company-register block: omitted
  EAP RTFH4 — "Öffnen des Deckels" photo and the two circuit sketches: captions only; manufacturer contact block omitted
  Figures — Kap. 2 cutaway drawing, Kap. 3 system drawing, Kap. 9 room-sensor drawing: not transcribed; only the printed text and captions are
-->

<!-- Gap-marking convention: a blockquote that starts with "GAP:" marks a place
     where the source is silent, cut off, illegible, contradictory, or was
     skipped under the ingest-document first rule. Form:
     > GAP: [what is missing or uncertain] — [why]. See verification.md line N.
     A GAP is never filled from another page, another document or general
     knowledge. It is closed only by a new ingest with its own anchor, and the
     closing edit says so in place of the marker. -->

<!-- Anchor format: [SL-P BA 2008, Kap. N, S. M] = chapter N, page M
     as printed in the page footer. The manual's own wording is kept in German;
     English headings in parentheses are glosses only. Printed example values on
     display boxes are the manual's examples, not any installation's values
     (Kap. 4, S. 3: "Angaben sind typische Werte und können von Ihrem Display
     abweichen!"). Handwritten annotations in the scanned copy are not
     transcribed. The "Anlagenwert" column of every parameter list is omitted
     for the same reason. -->

---

## Kap. 1 — Sicherheit (safety notes) [SL-P BA 2008, Kap. 1, S. 1–3]

**Allgemeines:** Die vollautomatische Pelletsheizung entspricht dem Stand der Technik und den einschlägigen Sicherheitsvorschriften, sowie der TRVB H118. Den geltenden örtlichen Vorschriften ist bauseits Rechnung zu tragen. [S. 1]

**Gefahrenhinweise:** Die Anlage wird mit 230V Wechselstrom betrieben. Reparaturen dürfen nur von SL-Servicetechnikern, SL-Vertriebspartnern und autorisierten Fachleuten (z.B.: Elektriker,..) durchgeführt werden. Bei Schäden durch unsachgemäße Reparatur erlischt der Garantieanspruch. [S. 2]

Hinweiszeichen used in the manual: "Gefahr" — Nichtbeachten kann zu Schäden an Leib und Leben oder Sachwerten führen; lightning symbol — Gefahr für Personen durch Stromschlag; ">100°" symbol — Gefahr f. Personen durch Verbrennung. [S. 2]

**Personalauswahl und Qualifikation:** Die Heizanlage soll von einer Person beaufsichtigt werden. Diese wird von unserem Techniker bei der Inbetriebnahme auf die Funktionen der Anlage eingeschult. Weiters ist keine zusätzliche Qualifikation notwendig. [S. 2]

**Sicherheitshinweise im Normalbetrieb:** Heiße Verbrennungsgase werden über das Rauchrohr abgeführt. Das Rauchrohr kann so heiß werden, dass Verbrennungen auftreten können. [S. 3]

**Sicherheitshinweise Instandhaltung:** Die Anlage wird mit elektrischem Strom (230 VAC) betrieben. Bei allen Instandhaltungsarbeiten Netzstecker ziehen! Instandhaltungsarbeiten bei eingeschalteter Anlage sind nicht erlaubt. Durch automatisch ablaufende Prozesse (z.B.: Reinigen,..) kann Gefahr durch Quetschen entstehen. [S. 3]

**Gefahr durch Hitze:** Der Pelletskessel ist ökonomisch gestaltet und isoliert. Trotzdem entsteht an einigen Bauteilen (z.B.: Rauchrohr, ...) Strahlungswärme. Mindestabstände zu anderen Bauteilen sind lt. örtlichen Baubestimmungen einzuhalten. [S. 3]

> GAP: The manual contains no instructions for emergencies: smoke or flue gas in the room, suspected carbon monoxide, fire, burn-back into the hopper, or what to do in the pellet store. It names no emergency procedure beyond the STB and the over-temperature behaviour in Kap. 1, S. 5.

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

An "Inbetriebnahme – Protokoll" form was ingested separately; see the L&S IB-Protokoll section below. (An earlier GAP marker here is closed. Whether that form is the "Inbetriebnahme-Checkliste (Dreifache Ausfertigung)" meant here is not stated on either document; see verification.md line 33.)

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

The "Putz und Service-Anleitung" referred to in row 2 was ingested separately; see the Anhang section below. (An earlier GAP marker here is closed.)

---

## Anhang — Putz- und Reinigungsanleitung (cleaning guide) [L&S Putzanleitung, S. 1]

One page, Lindner & Sommerauer Heizanlagenbau letterhead, undated. A cutaway drawing of the boiler (not transcribed) carries the following labels:

**ACHTUNG: Nach jeder Rauchrohrreinigung Saugzugventilator kontrollieren!**

| Bauteil | Intervall (as printed) |
|---|---|
| Rauchrohr | regelmäßig kontrollieren |
| Saugzug | mind. 1x jährlich reinigen und kontrollieren |
| Putzmechanik | mind. 1x jährlich reinigen und kontrollieren |
| Wärmetauscher | 1x Jährlich reinigen und kontrolliere (as printed) |
| Brennraum | mind. 1x jährlich reinigen und kontrollieren |
| Aschenlade | nach Bedarf entleeren |
| Zahnräder | 1x jährlich kontrollieren und nach Bedarf schmieren |

Die Reinigung des Kessels bzw. der Entfernung der Flugasche erfolgt am besten mit einem Industriestaubsauger. Die Gesamtreinigung der Anlage wird zweckmäßigerweise von oben nach unten durchgeführt, wobei der Brenner geöffnet sein sollte.

Die Reinigungsintervalle sind abhängig von der Pelletsqualität (Normpellets verwenden) und reichen von 1x monatlich bis 1x jährlich.

> GAP: No model designation, date or version is printed on this page. It is treated as belonging to SL-P BA 2008 only because that manual's contents page lists a "Putz- und Reinigungsanleitung" as Anhang. See verification.md line 22.

> GAP: Related intervals printed elsewhere: Kap. 3, S. 2 says the Aschenlade is "im Winter monatlich zu entleeren"; Kap. 5 uses an Aschenlade counter (Standard 200, message at 150 Std.). This page says only "nach Bedarf". Not reconciled.

---

## Anhang — Wartungsbuch: TRVB H 118 (2003), Anhang 2 Kontrollbuch [TRVB H 118 (2003), Anhang 2/1–2/4, S. 26–29]

Not manufacturer content. Four pages from the Austrian fire-prevention directive "pr TRVB H 118 – Ausgabe 2003", supplied as the "Wartungsbuch lt. prTRVB H 118" Anhang listed in the BA 2008 contents. The scanned copy has the pages in the order 2/1, 2/3, 2/2, 2/4.

### Anhang 2/1 — Kontrollbuch (cover form) [S. 26]

Anhang 2 - Kontrollbuch: Sämtliche Überprüfungen, Reinigungen, Verrichtungen und Vorkommnisse sind in diesem Kontrollbuch laut nachfolgendem Muster einzutragen. Form fields: Anlagenbetreiber, Anlagenerrichter, Feuerungsanlage (Fabrikat, Type, Baujahr, Heizleistung, Sonstiges). Not transcribed further.

### Anhang 2/2 — Regelmäßige Kontrolle der automatischen Holzfeuerungsanlage (während der Heizperiode/Betriebszeit) [S. 27]

**1) Wöchentliche Sichtkontrolle:** Einmal wöchentlich ist die gesamte Feuerungsanlage einschließlich der Brennstofflagerung einer Sichtkontrolle zu unterziehen. Festgestellte Mängel sind unverzüglich zu beheben.

**2) Monatliche Kontrollen:** Monatlich sind folgende Kontrollen durchzuführen:
- Funktionstüchtigkeit der Rückbrand-Schutzeinrichtung RSE, insbesondere der zuverlässige Schließvorgang
- Betriebsbereitschaft der Löscheinrichtungen einschließlich Wasserzufuhr
- Sauberkeit der Rauchgaswege (Rauchgaszüge im Heizkessel, Verbindungsstück und Rauchfang)
- Ordnungsgemäßer Betrieb der Steuerung
- Funktionstüchtigkeit der Störungsmeldung/Warneinrichtung(en)
- Ordnungsgemäßer Betrieb der Verbrennungsluft- und Saugzugventilatoren
- Ordnungsgemäßer Zustand des Feuerungsraumes/der Ausmauerung
- Einsatzbereitschaft der/des tragbaren Feuerlöscher(s)
- Ordnungsgemäße Aschelagerung
- Heizraum frei von brennbaren Lagerungen
- Dach frei von brennbaren Ablagerungen
- Brandschutzabschlüsse (Brandschutztüren - selbstschließend)

**3) Wartung:** Je nach Heizleistung ist die Feuerungsanlage regelmäßig in nachstehenden Zeitintervallen einer Wartung durch den Anlagenerrichter unterziehen zu lassen.

| Heizleistung | Wartungsintervalle |
|---|---|
| ≤ 150 KW | alle 3 Jahre |
| ≤ 400 KW | alle 2 Jahre |
| > 400 KW | 1 x jährlich |

### Anhang 2/3 and 2/4 — Kontrollen der automatischen Holzfeuerungsanlage durch den Anlagenbetreiber [S. 28–29]

Monthly log form (2/3 is a filled sample watermarked MUSTER, 2/4 is blank). Header fields: Jahr, Anlagenbetreiber, verantwortlicher Anlagenbetreuer. Rows (Monatliche Kontrolle, one column per month Jän–Dez plus Bemerkungen): Rückbrand-Schutzeinrichtung; Löscheinrichtung(en); Rauchgaswege; Steuerung; Warneinrichtung(en); Ventilatoren; Feuerungsraum/Ausmauerung; Tragbare Feuerlöscher; Aschelagerung; Lagerungen im Heizraum; Ablagerungen am Dach; Brandschutzabschlüsse; Rauchfang-Überpr./Reinig.; Unterschrift/Kurzzeichen. Footer box: Wartung durch fachkundige Person, durchgeführt am, Unterschrift, Bemerkungen. The sample entries on 2/3 are the directive's printed example and are not transcribed.

> GAP: The TRVB pages are a generic directive excerpt. Whether the ≤ 150 KW "alle 3 Jahre" maintenance interval is what the manufacturer or the installer actually requires for an SL-P is not stated in either document (Kap. 1, S. 2 only "empfiehlt" a Wartungsvertrag). See verification.md line 23.

---

# Montageanleitung SL-P, Stand 05-2009 [SL-P MA 2009]

Twelve unpaginated pages. Anchors give the scan page. Cover drawing is the same Heizraum / Brennstofflagerraum system drawing as BA 2008 Kap. 3, S. 1 (Förderschlauch 2" antistatisch, Saug-Misch-Verteiler, Ansaugdüsen, VL/RL).

## Allgemeine Hinweise [SL-P MA 2009, scan S. 2]

**Sicherheitshinweis:** Diese Vollautomatische Pelletsheizung entspricht dem Stand der Technik und den einschlägigen Sicherheitsvorschriften sowie der TRVB.

**Gefahrenhinweis:** Der Pelletskessel wird mit elektrischem Strom (230V) betrieben. Durch unsachgemäße Installation od. Reparatur kann Lebensgefahr durch Stromschlag entstehen. Alle Arbeiten am Kessel sind von qualifiziertem Personal durchzuführen.

**Garantie:** Eine fachgerechte Installation und Inbetriebnahme des Pelletskessels sind Voraussetzung für die Garantieleistungen durch den Hersteller.

**Lieferumfang:** Pelletskessel. Zwischenbehälter mit vollautomatischer Saugeinrichtung.

**Zubehör:** Saug-Misch-Verteiler für 2,3 od. 4 Ansaugdüsen. Spiralschlauch mit Erdungslitze als Saug- und Rückluftschlauch (25m). Ansaugdüse. Befüllrohre. Prallmatte. Z-Profile für Lagerraumtür. Storz-Kupplungen und Blinddeckel f. Befüllrohre.

## Der Pelletsraum — Ausführung [SL-P MA 2009, scan S. 2]

- Die Richtlinien der TRVB H118 und der örtlichen Bauvorschriften sind einzuhalten.
- Der Pellets - Lagerraum muss trocken sein.
- Der Pellets - Lagerraum muss dicht und massiv ausgeführt sein.
- Die Umfassungswände und Geschoßdecke müssen der Brandwiderstandsklasse F90 entsprechen.
- Die Einstiegsöffnung in den Pelletsraum muss nach außen aufgehen. Sie ist als Brandschutztür T30 auszuführen.

## Heizraum, Lagerraum und Kamin [SL-P MA 2009, scan S. 3]

Die Anlage kann auf drei Seiten bis auf wenige Zentimeter zur Wand gestellt werden. Es sollte jedoch bereits bei der Planung auf ausreichenden Platz für Servicearbeiten geachtet werden.

Um einen Störungsfreien Betrieb zu gewährleisten sind folgende Punkte zu beachten:

- **Zuluftöffnung im Heizraum** (keine Inbetriebnahme der Anlage ohne Zuluftöffnung)!
- **Im unteren Leistungsbereich können Abgastemperaturen unter 90°C entstehen.** Pelletsheizanlagen sind deshalb an einen feuchtigkeitsunempfindlichen Kamin anzuschließen.
- **Vor Errichtung einer automatischen Holzfeuerung ist das Einvernehmen mit dem zuständigen Rauchfangkehrer herzustellen.**
- **Das Abgasrohr muss zum Kamin ansteigend** (ideal sind 45°) **installiert werden.** Lange Abgasstrecken zum Kamin sind zu vermeiden.
- **Im Abgasrohr oder im Kamin ist ein Energiesparzugregler mit Explosionsklappe einzubauen.** Die Kaminzugregler sind einzustellen (Betriebsanleitung Seite 4 u. Technische Daten für Kaminberechnung)
- **Prallplatte im Lagerraum montieren.** Bei der Einbringung der Pellets ist darauf zu achten, dass diese gegen eine Prallwand geblasen werden und das Heizmaterial ohne Beschädigung in den Lagerraum rieselt.
- **Befüllrohre sollten nach Möglichkeit gerade ausgeführt werden. 90° Bögen sind zu vermeiden.**
- **Lagerraum: trocken** (Feuchtigkeit lässt Pellets aufquellen), **dicht und massiv** (Brandwiderstandsklasse), **keine E-Installationen und Wasserführenden Leitungen** (Kondenswasser).
- **Bei der Schlauchverlegung ist besonders darauf zu achten, dass es zu keinen Pelletsablagerungen kommen kann (keinen „Siphon" einbauen)!** (Two sketches: a single rising bend marked correct, an S-shaped sag marked wrong.)

## Einbau von Einblasrohren und Prallmatte [SL-P MA 2009, scan S. 4]

Two plan drawings (not transcribed) labelled: Einblasöffnung, Prallmatte, Z-Profil mit Brettern, Lucke T30, Einblasrohre, Blindboden 45°; dimensions printed 15, 20, 80/80.

> GAP: The drawing dimensions 15, 20 and 80 carry no unit. See verification.md line 28.

- Es ist immer ein Befüll- und ein Entlüftungsstutzen notwendig. Diese müssen aus Metall sein und sind zu erden. An der Außenseite muss eine Kupplung vom System Storz Typ A ∅ 100mm angebracht sein!
- Führen Leitungen durch brandschutztechnische Bauteile, so sind sie im Bereich der Durchdringung entsprechend der geforderten Brandwiderstandsklasse abzuschotten!
- Im Pellets - Lagerraum dürfen keine E-Installationen sein (Explosionsgefahr). Ist dies nicht vermeidbar ist Sie entsprechen der geltenden Vorschriften (z.B.: ÖVE, DVE, ..) explosionsgeschützt auszuführen!
- Die Befüllstutzen sind mit Blindkupplungen zu verschließen!

Es empfiehlt sich, einen Blindboden (z.B. 45° Neigung) einzubauen, um eine bessere Entleerung zu gewährleisten, und eine übermäßige Staubansammlung zu vermeiden.

### Befüllrohre die durch andere Räume geführt werden [SL-P MA 2009, scan S. 4]

Befüllrohre, die durch andere Räume geführt werden, sind entsprechend Zeichnung mit Steinwolle zu isolieren. Die Isolierung ist durch die Öffnung zu führen, der verbleibende Restspalt zu verputzen. Die Isolierungen sind an beiden Seiten der Wand mit Bindedraht zu sichern. Die Befülleitungen sind in geeigneter Weise zu fixieren (Deckenabhängung). (Drawing: Quelle TRVB H118.)

| | 1.) Wände die F30 standhalten müssen | 2.) Wände die F90 standhalten müssen |
|---|---|---|
| Mindestlänge der Isolierung | l= 500mm | l= 500mm |
| Mindestdicke der Isolierung | d= 40mm | d= 50mm |

## Montage der Ansaugdüsen [SL-P MA 2009, scan S. 5]

Drawing labels: 4x Befestigungsschrauben, RL-Schlauch, Saugschlauch, Einblasöffnung, Prallmatte, Z-Profil und Bretter, T30, Saugschläuche, Rückluftschläuche; nozzle spacing printed as "100".

Die Ansaugdüsen sind am Boden zu befestigen. Abstand zw. den Düsen 800 – 1200 mm. Um größere Staubansammlungen zu vermeiden ist beidseitig ein schräger Boden einzubauen (ca. 45° Neigung). Von den Ansaugdüsen wird je ein Saugschlauch und Rückluftschlauch zum Saug-Misch-Verteiler geführt. Von dort werden nur ein Saugschlauch und ein Rückluftschlauch zum Kessel geführt.

Die Schläuche sind in der Wanddurchführung einzumauern und zu verputzen. Ein Mindestbiegeradius von 25 cm ist bei den Schläuchen einzuhalten

## Wanddurchbruch [SL-P MA 2009, scan S. 6]

Fixings listed on the drawing: 4 Stk. Gestellschrauben M10x80 DIN 571 verz., 4 Stk. Scheiben M10 DIN 125 A verz., 4 Stk. Dübel Nylon N12 (distributor); 6 Stk. Gestellschrauben M6x40 DIN 571 verz., 6 Stk. Scheiben M6 DIN 125 A verz., 6 Stk. Dübel Nylon N8 (wall plate). Die Schläuche sind in der Wanddurchführung einzumauern und zu verputzen.

| Mauerdurchbruch | Breite x Höhe |
|---|---|
| 1 Stk. Lagerraum-Ansaugdüse | 7 x 15cm |
| 2 Stk. Lagerraum-Ansaugdüse | 16 x 15cm |
| 3 Stk. Lagerraum-Ansaugdüse | 25 x 15cm |
| 4 Stk. Lagerraum-Ansaugdüse | 33 x 15cm |

**Achtung:** Wird auf Grund von behördlicher Anordnung oder den örtlichen Baubestimmungen eine Brandschutzmanschette vorgeschrieben, so sind die Nylon-Dübel durch Metalldübel zu ersetzen

> GAP: Further drawing dimensions (110, 15, 12, and the 7 / 16 / 25 / 33 scale under the wall plate) carry no unit on the drawing. See verification.md line 28.

## Saug-Misch-Verteiler (flap positions) [SL-P MA 2009, scan S. 6]

In der Steuerung wird die Klappenstellung Pos.1 als AUF (der linke Abgang der Einheit ist offen) bezeichnet. Dadurch ergeben sich folgende Kombinationen:

| | M1 | M2 | M3 |
|---|---|---|---|
| Saugpos.1 | AUF | AUF | AUF |
| Saugpos.2 | ZU | AUF | AUF |
| Saugpos.3 | ZU | ZU | AUF |
| Saugpos.4 | ZU | ZU | ZU |

Drawing: M2 is the upper unit, M1 lower left, M3 lower right; each unit has outlets Pos.2 and Pos.1; the four store-side outlets are Pos.1–Pos.4 left to right.

## Kessel — Anlieferung and dismantling for transport [SL-P MA 2009, scan S. 7–9]

Der Kessel wird auf einer Euro-Palette in einem Karton verpackt angeliefert. Um eine problemlose Aufstellung und Montage zu ermöglichen, ist die Verkleidung bereits auf der Palette zu entfernen. Dazu gehen sie folgendermaßen vor: [S. 7]

**Displayverkleidung entfernen:** Schrauben oben lösen; nach oben schieben, um die Displayverkleidung auszuhängen; Buskabel am Display ausstecken. [S. 7]

**Frontverkleidung freimachen:** In der Frontverkleidung ist der Hauptschalter integriert. Um die Verkleidung zu entfernen, muss das Netzkabel an der Platine ausgesteckt werden. **ACHTUNG** Bevor Sie die Abdeckung öffnen stellen sie sicher, das der Netzstecker nicht eingeseckt ist!! Stecken sie dazu den Stecker 1 (ganz links) aus und ziehen ihn durch die Kabeldurchführung. Sie können dann die Frontverkleidung inkl. Hauptschalter und Netzkabel entfernen. [S. 8]

**Deckel entfernen:** Entfernen Sie zuerst die 3 Einsätze aus dem Deckelrahmen. Der Deckelrahmen ist nur auf Führungsbolzen gesteckt und kann daher problemlos heruntergenommen werden. [S. 8]

**Verkleidung abnehmen:** Entfernen Sie zuerst beide Seitenverkleidungen. Diese sind in die Front- bzw. Rückwandverkleidungen eingehängt. Falls eine Seitenverkleidung leicht klemmt, drücken sie oben leicht gegen die Frontverkleidung. Dann sollte sich die Verkleidung lösen. [S. 8]

Die Front- und Rückwandverkleidung ist mit je 2 Schrauben an der Grundplatte befestigt. Zum Entfernen der Verkleidung diese Schrauben lösen. [S. 9]

Normalerweise muss der Vorratsbehälter zur Montage nicht abgenommen werden. Sollte jedoch ein besonders enges Hindernis die Einbringung unmöglich machen, so lösen sie am Behälter oben die Halteschraube und am Stockerkanal die Schrauben nach der Zellradsschleuse. Sie können den Behälter mit der Stockerschnecke herausziehen. Der Kessel kann so in den Heizraum transportiert werden. [S. 9]

## Aufstellen des Kessels [SL-P MA 2009, scan S. 10]

Der Kessel soll einen Wandabstand von ca. 10cm haben und ist waagrecht auszurichten. Nun kann der Kessel wieder in umgekehrter Reihenfolge zusammengebaut werden. Die Befestigungsschraube für die Rückwandverkleidung (mittig) kann weggelassen werden. An der Stirnseite sollten sie jedoch mit der Hand angeschraubt werden. Achten Sie darauf, das Sie keine Kabel vergessen an der Steuerung anzustecken

Plan drawing labels: VL and RL connection pairs at both rear corners, Sicherheitsgruppe; dimensions 100, 1080, 100, 700, 630.

> GAP: The plan-drawing dimensions carry no unit. See verification.md line 28.

Vor Inbetriebnahme des Kessels kontrollieren, ob die Pelletsrutsche und der Brennertopf richtig eingehängt ist.

### Technische Daten as printed in the Montageanleitung [SL-P MA 2009, scan S. 10]

| | SL-P 8 | SL-P 12 | SL-P 15 | SL-P 25 |
|---|---|---|---|---|
| Nennleistung(kW) | 7,9 | 12 | 14,9 | 23,0 |
| Leistungsbereich | 2,4-7,9 | 2,5-12 | 3,9-14,9 | 3,9-23,0 |
| Breite | 1080 | 1080 | 1080 | 1080 |
| Tiefe | 730 | 730 | 730 | 730 |
| Höhe | 1500 | 1500 | 1500 | 1500 |
| Gewicht mit eingeb. Brenner | 350 | 350 | 350 | 350 |
| Wasserinhalt(Liter) | 43,6 | 43,6 | 43,6 | 43,6 |
| Wasserseitiger Widerstand (k10/k20) (mbar) | 13,5/3,4 | 13,5/3,4 | 13,5/3,4 | 13,5/3,4 |
| Rauchrohranschluss (mm) | 130 | 130 | 130 | 130 |
| Rauchrohr | nach oben | nach oben | nach oben | nach oben |
| Dm Vor/Rücklauf (Zoll) | 1" | 1" | 1" | 1" |
| Vorlauf | nach oben | nach oben | nach oben | nach oben |
| Rücklauf | nach oben | nach oben | nach oben | nach oben |
| notw. Förderdruck bei 160°C (mbar) | 0,07/0,1 | 0,1/0,1 | 0,1/0,07 | 0,1/0,07 |
| Abgastemperatur Nenn / Kleinste L. | (blank) | (blank) | (blank) | (blank) |
| Aschenlade (Liter) | 20 | 20 | 20 | 20 |
| Elektr. Anschluss | 230V ; 10A ; 50 Hz (all models) | | | |
| Anzünder (W) | 300 | 300 | 300 | 300 |
| Saugzug (W) | 32 | 32 | 32 | 32 |

> GAP: This table differs from BA 2008 Kap. 3, S. 3 for SL-P 25 (Nennleistung 23,0 here, 23,5 there; Leistungsbereich 3,9-23,0 here, 3,9-23,5 there), leaves the Abgastemperatur row blank, and omits the efficiency, exhaust mass flow, CO2 and power-consumption rows. Both tables are kept with their own anchors; not merged. See verification.md line 29.

## Anschluss an den Kamin [SL-P MA 2009, scan S. 11]

**Kamin:** Ein, den örtlichen Bestimmungen und der Kesselleistung entsprechender Kamin ist Voraussetzung für den einwandfreien Betrieb der Anlage. Die Abgastemperatur kann im Teillastbereich unter 95°C sinken. Daher ist der Kamin feuchtigkeitsunempfindlich auszuführen. Wird die Anlage an einen bestehenden, feuchtigkeitsempfindlichen Kamin (z.B.: Ziegelmauerwerk) angeschlossen, so ist eine Kaminberechnung durchzuführen bzw. ein Kaminbefund einzuholen (Kaminkehrer).

**Das Abgasrohr:** Lt. TRVB ist im Verbindungsstück (Abgasrohr) oder im Kamin innerhalb des Heizraumes eine Verpuffungsklappe (Explosionsklappe) einzubauen. Es ist ein Kaminzugregler einzubauen, der den Kaminzug auf 20 mbar begrenzt.

> GAP: "auf 20 mbar" is transcribed as printed. BA 2008 Kap. 1, S. 4 gives the required draught as "7 bis 10 Pascal" and the technical data give a Förderdruck of 0,07–0,1 mbar. The printed 20 mbar is two orders of magnitude away from both and is not to be used as a setting without checking. Also "unter 95°C" here vs "unter 90°C" on scan S. 3 and in BA 2008. See verification.md lines 30 and 31.

## Elektrischer Anschluss [SL-P MA 2009, scan S. 11]

Der Heizkessel wird steckerfertig verdrahtet geliefert. Es müssen lediglich die Verbindungen zum Saug-Misch-Verteiler, zu den Modulen und zu den peripheren Geräten (Pumpen, Mischer, ..) Vorort hergestellt werden. Die Platine befindet sich unterhalb des Displays.

Front-view drawing labels: Hauptsteuerungsplatine (behind the panel below the display); STB mechanisch zu entriegeln (button below the board cover, above the firebox door).

## Hauptsteuerung — terminal assignment [SL-P MA 2009, scan S. 12]

Board drawing is marked "IPN 80". Fuse positions are printed with ratings 2A, 10A, 10A and 3A; a jumper position is marked "C STOCKER"; two BUS sockets are at the right-hand end. The terminal strip labels under the drawing read: 230V, SAUG, GLÜH, PUTZ, STOCKER, AUST, LUFT, M1, M2, M3, FÜLL, STB (<100°), LAMBDA, DREH, EXT (AUS), KESSEL (PT100), ABGAS (PT100). Pin markings: terminals 1–4, 6, 7 are L1 PE N; terminal 5 is L1 PE L2 L3; terminal 8 is N PE Y1 Y2; terminals 9 and 10 are Y1 Y2.

| Terminal | Label | Function as printed |
|---|---|---|
| 1 | NETZ | Netzanschluss (230V) |
| 2 | SAUG | Saugturbine (230V) |
| 3 | GLÜH | Zünderspirale (230V) |
| 4 | PUTZ | Putzmotor (230V) |
| 5 | STOCKER | Stockermotor (230V) |
| 6 | AUST | Ext. Antriebsmotor (230V) |
| 7 | LUFT | Saugzuggebläse V1 (230V) |
| 8 | M1 | Saug-Misch-Verteiler Motor 1 (230V) |
| 9 | M2 | Saug-Misch-Verteiler Motor 2 (230V) |
| 10 | M3 | Saug-Misch-Verteiler Motor 3 (230V) |
| 12 | FÜLL | Füllstandssensor — wire colours printed under the terminal: blau, weiß, braun |
| 13 | STB | Sicherheitstemperaturbegrenzer |
| 14 | LAMBDA | Lambdasonde — wire colours printed: weiß, weiß/grau, schwarz |
| 15 | DREH | Sensor Brenner zu — wire colours printed: blau, schwarz, braun |
| 16 | EXT | Externer Start |
| 18 | KESSEL | Kesselthermometer |
| 19 | ABGAS | Abgasfühler |

> GAP: Terminals 11 and 17 do not appear in the printed list or on the drawing. Which circuit each fuse protects is not printed. The order in which the three colours map to the three pins of each terminal is given only by their left-to-right position in the drawing. See verification.md lines 32 and 42.

Cross-reference, both as printed in BA 2008 Kap. 13: "Der Ausgang 6 kann für einen externen Austragungsmotor … verwendet werden" (S. 1) matches terminal 6 AUST here; "Am Ausgang 16 kann auch ein 70° Sensor installiert werden" (S. 4) refers to terminal 16 EXT here.

### Verbindung zum Saug-Misch-Verteiler [SL-P MA 2009, scan S. 12]

Die Stellmotoren des Saug-Misch-Verteilers werden direkt an der Hauptplatine angeschlossen. Bei 1 Saug-Misch-Verteiler (2 Ansaugdüsen) reicht ihnen die Verbindung von Anschluss 8 aus. Hierfür verwenden Sie ein 4-poliges Kabel (mind. 0,75mm²). Für die 2. und 3. Saug-Misch-Verteiler verwenden Sie je ein 2-poliges Kabel. Auch hier mind. 0,75mm².

Wiring sketch: Anschlußleiste Steuerung terminals 8 / 9 / 10 (N, PE, Y1, Y2 from 8; Y1, Y2 from 9 and from 10) to the Klemmblock Saug-Misch-Verteiler, then to Stellmotor M1, M2, M3.

---

# Inbetriebnahme – Protokoll (commissioning record form) [L&S IB-Protokoll, S. 1]

One-page form, no. 9.90.420, Lindner & Sommerauer Biomasse - Heizanlagen / SL-Technik GmbH. Only the blank form is transcribed. The entries, ticks, date and signatures of the scanned copy are installation-specific and omitted.

Header fields: Name des Anlagenbetreibers, Straße, Ort; Montagefirma, Adresse, Monteur. **Feuerungsanlage:** Heizkessel-Typ, Wärmeleistung, Baujahr, Fabrik.-Nr.

**Sicherheitstechnische Überprüfung:** Rückbrandschutzeinrichtung; Löscheinrichtung; Warneinrichtung; Zellenradschleuse; Rauchgaswege.

**Anlagenbauteile überprüft:** Kaminzugregler; Ventilatoren; Ascheladen; Steuerung; Rücklaufanhebung.

**Inbetriebnahme** (one of): 1 Brennschüsselanlage; 2 Drehrostanlage; 3 Pelletsanlage.

**a) KONTROLLE HANDBETRIEB**
1. Test Putzmotor
2. Test Rückbrandklappe
3. Zellenradschleuse (Achtung Drehrichtung!)
4. Test Raumaustragung (Achtung Drehrichtung / Federpakete!)
5. Test Stockermotor (Achtung Drehrichtung!)
6. Test Lüfter V1 Saugzuggebläse (Achtung Drehrichtung!)
7. Test Lüfter V2 Sekundärgebläse (Achtung Drehrichtung!)
8. Test Föhnlüfter + Föhnheizung
9. Test Boilerpumpe, Rücklaufpumpe, Heizkreispumpe
10. Test Mischer auf / zu (Achtung Drehrichtung!)
11. Test Sensoren: Füllstand, Drehrost, Lichtschranken
12. Einschulung Handbetrieb

**b) KONTROLLE DAUERBETRIEB**
1. Kontrolle Kesseltemperatur
2. Kontrolle Abgastemperatur
3. Kontrolle V1 min / V1 max
4. Kontrolle Pause min / Pause max
5. Kontrolle Förderzeit
6. Kontrolle Reinigungsautomatik
7. Einschulung Dauerbetrieb
8. Hinweis Wartung

**c) EINSCHULUNG UHRZEITBETRIEB** 1. Wochentag einstellen 2. Uhrzeit einstellen 3. Uhrzeit auf nächsten Tag übertragen

**d) EINSCHULUNG BOILERBETRIEB** 1. Boiler auswählen 2. Boiler Soll eingeben 3. Boiler Start eingeben 4. Boiler-Vorrang 5. Resttemperatur-Verwertung

**e) EINSCHULUNG UHR-BOILER** 1. Uhrzeit einstellen

**f) EINSCHULUNG AUSSENTEMPERATURREGELUNG** 1. Mischerkreis auswählen 2. Mischerkreis EIN/AUS 3. Nachtabsenkung EIN/AUS 4. Uhrzeit einstellen 5. Heizkurve einstellen Vorlauf max / min 6. Außentemperatur einstellen max / min 7. Raum einstellen max / min 8. Raumeinfluss einstellen

Closing statement: Der Anlagenbetreiber wurde mit der Bedienung der automatischen Holzfeuerungsanlage vertraut gemacht und über die Wirkungsweise und Eigenkontrolle der technischen Sicherheitseinrichtungen unterrichtet. Im Zuge der Unterweisung wurde dem Betreiber der Anlage eine Bedienungsanleitung übergeben. Fields: Datum; Unterschrift des Anlagenbetreibers.

> GAP: The form covers three plant types. It does not say which check items apply to a Pelletsanlage; several (Rückbrandklappe, Raumaustragung, Lüfter V2 Sekundärgebläse, Föhnlüfter, Lichtschranken) name components that do not appear in BA 2008 or MA 2009. See verification.md line 34.

---

# TÜV Prüfbescheinigung SL-P 12 [TÜV 2209092-2-DK, S. 1]

Trilingual certificate (German / English / Danish), TÜV SÜD Landesgesellschaft Österreich, issued Bruck/Mur, 21. September 2009. **Applies to type SL-P 12 only.**

| Field | As printed |
|---|---|
| Nummer | 2209092-2-DK |
| Antragsteller / Hersteller | Lindner & Sommerauer |
| Produkt | Heizkessel für Holzpellets / boiler for wood pellets / centralvarmekedel for træpiller |
| Typ | SL-P 12 |
| Prüfgrundlage | EN 303-5, Klasse 3 |
| Brennstoff | Holzpellets |
| Brennstoffzufuhr | automatisch |
| Grundlage: Prüfbericht | K 14991 / 2.1, 2006-05-10 |

**Prüfergebnis:**

| | Messwert | Anforderung EN 303-5 |
|---|---|---|
| **Volllast / nominal load** | 12,3 kW | |
| CO (10% O₂) | 35 | max. 3000 mg.m⁻³ |
| OGC (10% O₂) | 2 | max. 100 mg.m⁻³ |
| Staub / dust (10% O₂) | 16 | max. 150 mg.m⁻³ |
| Wirkungsgrad / efficiency | 95,0 | min. 73,5 % |
| **Teillast / part load** | 2,5 kW | |
| CO (10% O₂) | 45 | max. 3000 mg.m⁻³ |
| OGC (10% O₂) | 6 | max. 100 mg.m⁻³ |
| Staub / dust (10% O₂) | 12 | max. 150 mg.m⁻³ |
| Wirkungsgrad / efficiency | 91,8 | min. 73,5 % |

Die Übereinstimmung der genannten Werte mit den Ergebnissen gemäß dem Prüfbericht wird bestätigt.

> GAP: The Messwert column prints no unit; the unit is printed only in the Anforderung column. Nominal load here is 12,3 kW and efficiency 95,0 / 91,8, where BA 2008 Kap. 3, S. 3 gives Nennleistung 12 and Wirkungsgrad 95,2 / 91,6 for SL-P 12. Kept separately with their own anchors. See verification.md line 35.

---

# Raumfernfühler RTFH4 (EAP electric) [EAP RTFH4, S. 1]

Third-party datasheet: "Raumfernfühler mit Sollwertkorrektur und Betriebswahlschalter RTFH4".

**Anwendung:** Raumfühler für Raumtemperaturüberwachung einschließlich Potentiometer für Fernverstellung mit Mittelstellung zum Erhöhen und Absenken der Kessel- und Vorlauftemperatur.

**Technische Daten:**

| | |
|---|---|
| Gehäuse | Kunststoffgehäuse, Farbe weiß |
| Umgebungstemperatur | +21°C |
| Sollwertverstellung | +/-5°C |
| Betriebswahlschalter | Aus / Boiler / Nacht / Automatik / Tag |
| Störung | LED Rot |
| Sensor | KTY81-122 |
| Anschluß | 2-Leiter |
| Versorgungsspannung | 5V DC für LED |
| Montage | auf UP-Dose Ø55mm |
| Schutzart | IP20, Schutzklasse 3 |

**Grundeinstellung:**

| Raumtemp. | Aus | Boiler | Mond | Uhr | Sonne |
|---|---|---|---|---|---|
| 21°C | 2365Ω | 2035Ω | 1695Ω | 1035Ω | 1365Ω |

**Achtung:** Bei Sensor Betrieb beträgt die Abweichung des Widerstandswert pro Grad Celsius Raumtemperatur ca. 8Ω auf- bzw. abwärts.

Sketch captions: "Öffnen des Deckels" (photo); "Anschlussbild 0/1 Sensorkreis", 2-Leiter, terminals 1 and 0 across Rx; "Anschlussbild Duo-LED 5V", three terminals of which two are legibly marked G and rt.

> GAP: Nothing on this sheet names Lindner & Sommerauer or the SL-P, and nothing in BA 2008 names the RTFH4. The match with the "Raumgerät" of BA 2008 Kap. 9 (positions Pumpe Aus / Boilerbetrieb / Nachtabsenkung aktiviert / Normalbetrieb / Nachtabsenkung deaktiviert; symbols Mond, Uhr, Sonne; ±5°C selector; contacts 1 and 2) is an inference from similar wording and is not stated in print. Note also that BA 2008 says to connect at "Kontakten 1 und 2" while this sheet labels the sensor terminals 1 and 0. The resistance row is not monotonic (Uhr 1035Ω is below Sonne 1365Ω); transcribed as printed. The third LED terminal label is not legible. See verification.md lines 36 and 37.

