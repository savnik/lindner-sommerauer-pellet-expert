# Controller parameters

<!-- Coverage manifest (plan §7.2). Every addition to this file must update it.
model: SL-P 8 / SL-P 12 / SL-P 15 / SL-P 25 (Modell 2008; document states validity "ab Baujahr 2006")
firmware: Pell 080325.1 (as printed in page footers of Kap. 5–15; Kap. 1–4, 16, 17 footers carry only a date; see verification.md for the version discrepancy)
source document: "Betriebsanleitung Pelletsanlage SL-P 8/12/15/25, Modell 2008", SL-Technik GmbH / Lindner & Sommerauer, dated 18.04.2008 and 29.04.2008. Short name for anchors: SL-P BA 2008. Kap. 12 and 13 footers read "Serviceanleitung Pelletsanlage" rather than "Bedienungsanleitung".
sections covered:
  Kap. 4 — Erklärung des Bedienungsfeldes (Display), keys
  Kap. 5 — Dauerbetrieb (menu items, parameter list)
  Kap. 6 — Uhrzeitbetrieb (menu items, parameter list)
  Kap. 7 — Boilerbetrieb (menu items, parameter list)
  Kap. 8 — Uhr-Boilerbetrieb (menu items, parameter list)
  Kap. 9 — Außentemperaturregelung (heating curve, room curve, menu items, parameter list); room-unit switch functions are in system-integration.md
  Kap. 10 — Prüfbetrieb
  Kap. 11 — Handbetrieb
  Kap. 12 — Zusatzparameter Verbrennung (menu items, factory settings per model)
  Kap. 13 — Zusatzparameter Service (menu items)
  Kap. 14 — Zusatzparameter Fühlerabgleich
  Kap. 15 — Zusatzparameter Hausanlage (menu items, parameter list)
  Kap. 17 — Fehlermeldungen (F2–F167 as printed)
sections not covered:
  none of Kap. 4–15, 17 is omitted; figures (display panel photo Kap. 4 S. 1, heating-curve graphs Kap. 9 S. 1–2, Heizbild Kap. 9 S. 5) are described from their printed captions only
  "Anlagenwert" columns of all parameter lists: omitted (installation-specific, handwritten in the scanned copy)
-->

<!-- Gap-marking convention: a blockquote that starts with "GAP:" marks a place
     where the source is silent, cut off, illegible, contradictory, or was
     skipped under the ingest-document first rule. Form:
     > GAP: [what is missing or uncertain] — [why]. See verification.md line N.
     A GAP is never filled from another page, another document or general
     knowledge. It is closed only by a new ingest with its own anchor, and the
     closing edit says so in place of the marker. -->

<!-- Anchor format: [SL-P BA 2008, Kap. N, S. M] = chapter N, page M
     as printed in the page footer. Display boxes are transcribed as two-line
     code blocks exactly as printed; the numbers in them are the manual's
     example values, not defaults and not any installation's values (Kap. 4,
     S. 3: "Angaben sind typische Werte und können von Ihrem Display
     abweichen!"). Defaults are only the "Standard" columns of the printed
     Parameterlisten. Handwritten annotations in the scanned copy are not
     transcribed. -->

---

## Kap. 4 — Erklärung des Bedienungsfeldes (control panel) [SL-P BA 2008, Kap. 4, S. 1]

Panel layout (from the photo): a two-line display at the top (example shown: `Kesseltemp. 75°` / `Kessel SOLL 80°`); left key block `Z` (top), `–` `Quit` `+` (middle row), `V` (bottom); `Ein` and `Aus` keys with LEDs; right column of mode keys, each with a yellow LED: Dauerbetrieb, Uhrzeitbetrieb, Boilerbetrieb, Uhr+Boilerbetr., Außentemp. Reg., Prüfbetrieb, Handbetrieb.

**Taste Ein --- Aus:** Die Anlage kann damit gestartet bzw. gestoppt werden. Bei eingeschalteter Anlage leuchtet die grüne Leuchtdiode, bei ausgeschalteter Anlage leuchtet die rote Leuchtdiode. Während des Zündvorganges blinken die beiden Leuchtdioden abwechselnd. Im Boilerbetrieb schaltet die Anlage selbständig, die Tasten **Ein** und **Aus** haben nur eine bedingte Funktion.

**Rechte Tastenreihe:** Die gewünschte Betriebsart wird durch Drücken ausgewählt, dabei leuchtet die gelbe Leuchtdiode.

**Taste Quit (quittieren):** Taste drücken und damit angezeigte Störmeldungen entfernen.

**Taste - bzw. +:** Sollwerte in der zweiten Reihe des Anzeigefeldes können mit den Tasten - (minus) bzw. + (plus) in einem vorgegebenen Bereich verändert werden (z.B. Uhrzeit im Uhrzeitbetrieb etc.).

**Taste V bzw. Z:** Mit den Tasten V (vorwärts) bzw. Z (zurück) können die einzelnen Anzeigefelder, wie die Seiten eines Buches, vor- und zurückgeblättert werden.

Access to the Zusatzparameter menus (from Kap. 12, 13, 15, 14): einmaliges gleichzeitiges Drücken von V und Z → Zusatzparameter Verbrennung [Kap. 12, S. 1]; zweimaliges gleichzeitiges Drücken von V und Z → Zusatzparameter Service [Kap. 13, S. 1] and, as printed identically, Zusatzparameter Hausanlage [Kap. 15, S. 1]; gleichzeitiges Drücken von V und Z aus dem Hauptmenü → Zusatzparameter Fühlerabgleich [Kap. 14, S. 1]. Zurück kommen Sie durch Drücken einer beliebigen Betriebsarttaste. Den Wert ändern Sie mit der „+" oder „-" Taste.

> GAP: The manual gives the same key sequence ("zweimaliges gleichzeitiges Drücken") for both Zusatzparameter Service (Kap. 13) and Zusatzparameter Hausanlage (Kap. 15), and "gleichzeitiges Drücken … aus dem Hauptmenü" for Fühlerabgleich (Kap. 14) without a count. The exact navigation between these three levels is not stated in the document. See verification.md.

Field observation, not from a document [verification.md line 43, firmware 080325.4]: repeated presses of V and Z together step through the levels in the order Verbrennung (1), Service (2), Fühlerabgleich (3), Hausanlage (4), each opening with a title screen "ZUSATZPARAMETER / <name>". Quote as an observation on that firmware, not as the manual's instruction.

---

## Kap. 5 — Dauerbetrieb (continuous operation) [SL-P BA 2008, Kap. 5, S. 1–3]

Die Betriebsart „Dauerbetrieb" unterscheidet grundsätzlich 2 Varianten:

**a) Betrieb der Anlage ohne ein Raumgerät:** Die Anlage stellt in der BA „Dauerbetrieb" ständig Energie zur Verfügung. Die Anlage heizt auf bis „Kessel Soll" erreicht ist, wechselt in den „Stocker Stopp" und startet wieder bei erreichen der „Kessel MIN" Temperatur, unabhängig der aktuellen Anforderung.

**b) Betrieb der Anlage mit einem Raumgerät:** Hier reagiert die Anlage nur auf Anforderungen durch die Hausanlage. Ist keine Anforderung gegeben (aus Heizkreisen oder Boiler) so schaltet die Anlage ab und startet erst wieder, wenn eine Heizkreisanforderung besteht, oder z.B. „Boiler Start" unterschritten wird. Auch die Abschaltung durch die Außentemperatur (siehe Menü AT-Regelung) ist an den Betrieb **mit** einem Raumgerät gebunden.

Im Winter ist im Normalfall die Betriebsart „Dauerbetrieb" zu wählen, um eine gleichmäßige Heizleistung zu erreichen. Sie haben die Möglichkeit im Menü Außentemperatur-Regelung eine oder zwei Nachtabsenkungen einzustellen. [S. 1]

```
Kesseltemp.        57°
Kessel SOLL        80°
```
Aktuelle Kesseltemperatur / Angestrebte Kesseltemperatur. Mit der + / - Taste kann man Einstellungs-Sollwerte in einen vorgegebenen Bereich verändern. [S. 1]

```
Kesseltemp.        57°
Kessel MIN  (55°)  65°
```
Aktuelle Kesseltemperatur. a) ab dieser Kesseltemp. beginnt der Kessel zu modulieren (> der höchsten Anforderung bzw. immer > 55°C); b) Kesselstarttemperatur nach Stockerstop. [S. 1]

```
Aktuell            0:00
Aschenlade       150:00
```
Aktuelle Laufzeit / Eingestellter Entleerungsintervall für die Aschenlade. Nach jedem entleeren der Aschenlade ist der Aschezähler wieder zurückzustellen. Zum Zurücksetzen des Zählers wechseln sie in den **Dauerbetrieb** zum oben angeführten Parameter. Durch **gleichzeitiges** Drücken der „+" und „-" Taste wird der „Aktuelle Wert" auf Null gesetzt. [S. 1]

```
Aschenlade entleeren
  Löschen mit +/-
```
```
Anlage wird gestoppt
  Löschen mit +/-
```
Sind 150 Std. erreicht, so erscheinen auf dem Display diese Meldungen. Diese 2 Meldungen wechseln im 2 sec. Intervall. [S. 1]

```
Aschenlade voll
  Löschen mit +/-
```
Ist der Wert "Aschenlade" um 50 überschritten so erscheint diese Meldung. **Die Anlage wird mit Fehler 20 abgestellt!** Mit „Quit" kann diese Meldung kurz ausgeblendet werden. Zum zurücksetzen des Zählers drücken Sie die Tasten „+" und „-" **gemeinsam**. Hier müssen sie nicht mehr in den Dauerbetrieb wechseln. [S. 2]

```
Sackbetrieb        EIN
  EIN+ /AUS-
```
Mit dieser Funktion kann der Sackbetrieb eingeschaltet werden. Die Befüllung des Zwischenbehälters kann mit Säcken durchgeführt werden und die Saugfunktion ist deaktiviert. Die eingestellte Saugzeit dient als Parameter für die Reinigung. [S. 2]

```
Saugfenster        EIN
Saugfreigabe      4:00
```
Aktueller Status (Anlage befindet sich in Saugfreigabe) / Beginn des Saugfensters (ab dieser Zeit kann gesaugt werden). [S. 2]

```
Saugfenster        EIN
Saugsperre       22:00
```
Aktueller Status. / Ende des Saugfensters. Zwischen Freigabe und Sperre muss immer 1 Std. Unterschied sein, da dieser Schaltimpuls auch für die Reinigung verwendet wird. Zur Saugsperre wird die Funktion „Saugen" aktiviert. Das Saugen erfolgt nach der „V1-Nachlaufzeit" und anschließendem Abkühlen des Kessels. Dadurch kann durchaus 1 Std. oder mehr vergehen, bis die Anlage wirklich reinigt und saugt. [S. 2]

```
Nächster Putzvorgang
  Nach Freigabe
```
Das Reinigen ist durch die Einstellungen „Saugfreigabe" und „Saugsperre" gesperrt. [S. 2]

```
Nächster Putzvorgang
  in 60m00s
```
Aktuelle Stockerlaufzeit, nach der die nächste Reinigung durchgeführt wird. Nach Auslösen des Reinigungs- Zyklus wartet die Anlage die unter „V1-Nachlauf" eingestellte Zeit ab und reinigt anschließend den Kessel. [S. 2]

```
Nächster Saugvorgang
  nach Freigabe
```
Das Saugen ist derzeit gesperrt. Z.B.: durch die Einstellungen „Saugfreigabe" und „Saugsperre". [S. 2]

```
Nächster Saugvorgang
  in 219m29s
```
Aktuelle Stockerlaufzeit, nach der die nächste Reinigung durchgeführt wird, in der Regel jedoch 1 x täglich bei erreichen der „Saugsperre-Zeit". (as printed) [S. 2]

Ist am Beginn der Saugsperre > 1/5 des Saugintervalls (von 350min) abgelaufen, so wird der Kessel abgestellt, gereinigt und anschließend der Zwischenbehälter befüllt. Ist eine Boileranforderung aktiv, so wird diese noch vollendet. Wenn weniger als 1/5 abgelaufen ist, oder der Behälter „voll" meldet, so wird nicht gesaugt. [S. 2]

```
Saugen/Putzen      AUS
Putzen einleiten   +/-
```
Mit dem Drücken auf die + Taste wird ein Saugvorgang eingeleitet. [S. 3]

```
Saugen/Putzen      EIN
Putzen einleiten   +/-
```
Der „Saug / Reinigungszyklus" wurde mit „+" aktiviert. Die Anlage ist in der Nachlaufzeit oder in der Abkühlfase vor dem Reinigen. Sollte der Kessel auf Betriebstemperatur sein, so ist eine Sperrzeit festgelegt, in der der Kessel abkühlt. Erst dann wird die Reinigung und anschließend das Saugen eingeleitet. [S. 3]

```
Vorgabe
Saugposition         2
```
Hier kann auf die verschiedenen Saugpositionen umgeschaltet werden. [S. 3]

```
Anzahl der Sonden    3
```
Anzahl der Absaugpunkte eingeben (1-4 möglich). [S. 3]

```
Boiler 1 Temp.     60°
Kein Boilerfühler    2
```
Anzeige der aktuellen Boilertemperatur. [S. 3]

```
Kein Boilerfühler    3
Kein Boilerfühler    4
```
Es können bis zu 24 Boilerfühler angeführt sein (entsprechend den montierten Modulen). [S. 3]

```
Version       080325.L
Pellets:  Abgas-Z
```
Hier wird die aktuelle Programmversion angezeigt. Es handelt sich um ein Pellets – Programm. [S. 3]

```
Version       080325.L
Pellets:  Lambda-Z
```
Die Anlage kann mit Abgaszündung oder Lambdazündung betrieben werden. (siehe Zusatzparameter Service). [S. 3]

```
Basis         xxxxxx.x
Pellets:
```
Drückt man die „Quit-Taste", so erscheint die Basisversion des Programms. [S. 3]

### Parameterliste Dauerbetrieb [SL-P BA 2008, Kap. 5, S. 3]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Kessel SOLL | Gewünschte Kesseltemperatur | 80-90° | 80° |
| Kessel MIN | Gew. Kesselminimum Temp. | 50-75° | 65° |
| Aschenlade | Parameter für Aschemeldung | 1-200 | 200 |
| Saugfreigabe | Beginnzeit f. Saugvorgang | 00:00 bis 22:00 | 04:00 |
| Saugsperre | Endzeit f. Saugvorgang | 01:00 bis 23:00 | 22:00 |
| Anzahl Sonden | | 1 - 4 | 4 |

---

## Kap. 6 — Uhrzeitbetrieb (timer operation) [SL-P BA 2008, Kap. 6, S. 1–2]

Den Uhrzeitbetrieb verwenden Sie in der Übergangszeit, in der die volle Heizleistung nicht mehr den ganzen Tag benötigt wird. Sie haben die Möglichkeit zweimal im Laufe des Tages die Heizung ein- bzw. ausschalten zu lassen. Durch das Abschalten in der Nacht wird eine natürliche Temperaturabsenkung erreicht.

**a) Betrieb der Anlage ohne Raumgerät:** Die Anlage wird an den einzelnen Wochentagen lt. den eingestellten Zeiten betrieben. Diese Zeiten werden genau eingehalten, unabhängig der aktuellen Außentemperatur, bestehender Anforderungen,… Während diesem „EIN-Fenster" läuft die Anlage analog dem **Dauerbetrieb ohne Raumgerät**.

**b) Betrieb der Anlage mit einem Raumgerät:** Ist ein Raumgerät installiert, steht die Betriebsart „Uhrzeitbetrieb" nicht zur Verfügung. Wird diese Betriebsart ausgewählt, so schaltet die Anlage nach einer Minute in den Dauerbetrieb. Als Ersatz für diese Betriebsart steht im Menü „Außentemperaturregelung" für jeden Mischkreis einzeln eine „Freigabe – und Sperrzeit" zur Verfügung.

Gleichzeitiges Drücken von der + Taste und zusätzlich Quit ermöglicht größere Zeitsprünge. [S. 1]

```
Kesseltemp.        57°
Uhrzeit          12:49
```
Aktuelle Kesseltemperatur / Aktuelle Uhrzeit. [S. 1]

```
Kesseltemp.        57°
Uhrzeit    U     12:49
```
U…Die Anlage ist auf Grund der aktuellen Uhrzeit in einem „EIN-Zustand". [S. 1]

```
Kesseltemp.        57°
Uhrzeit    B     12:49
```
B…Die Anlage ist auf Grund der Funktion „Komb.Boiler-Uhr" (Service) in einem „EIN-Zustand". [S. 1]

```
Mo Di Mi Do Fr Sa So
*
```
Aktueller Wochentag. Die Anwahl des Wochentages erfolgt mit der + / - Taste. Um den Wert für diesen Tag zu ändern, gehen Sie mit V in die nächste Menüebene. Mit Z kommen sie eine Ebene höher und mit + / - ändern Sie die Werte. Durch drücken der „Quit"-Taste können Sie die Einstellungen auf den nächsten Tag kopieren. So können Sie der Anlage täglich mitteilen, wann sie eingeschaltet bzw. ausgeschaltet sein soll, z.B. bei einem Wochenendhaus. [S. 1]

```
*
Zeit 1 EIN       05:00
```
Der Stern zeigt Ihnen den aktuellen Wochentag an. Startzeit 1. [S. 2]

```
*
Zeit 1 AUS       21:30
```
Aktueller Wochentag / Stoppzeit 1. [S. 2]

```
*
Zeit 2 EIN       21:30
```
Aktueller Wochentag / Startzeit 2. [S. 2]

```
*
Zeit 2 AUS       21:30
```
Aktueller Wochentag / Stoppzeit 2. Das 2. Zeitfenster wird automatisch nach hinten verschoben um Überschneidungen der Zeitfenster zu vermeiden. [S. 2]

### Parameterliste Uhrzeitbetrieb [SL-P BA 2008, Kap. 6, S. 2]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Zeit 1 EIN | Startzeit 1 d. Anlage | 00:00 – 24:00 | 00:00 |
| Zeit 1 AUS | Stopzeit 1 d. Anlage | 00:00 – 24:00 | 00:00 |
| Zeit 2 EIN | Startzeit 2 d. Anlage | 00:00 – 24:00 | 00:00 |
| Zeit 2 AUS | Stopzeit 2 d. Anlage | 00:00 – 24:00 | 00:00 |

Diese Werte können für jeden Wochentage getrennt vergeben werden (Mo–So table for the owner's values; blank in the manual).

---

## Kap. 7 — Boilerbetrieb (hot-water / buffer operation) [SL-P BA 2008, Kap. 7, S. 1–3]

Es können je nach Anzahl der installierten Module serienmäßig bis zu 24 Boiler bedient werden. In den jeweiligen Boiler muss ein Temperaturfühler (PT 100) eingebaut werden. Fällt die Boilertemperatur unter die eingegebene „Boiler START" Temperatur, z.B. 40°C, so zündet die Anlage automatisch, das Boilerwasser wird bis zur „Boiler SOLL" Temperatur aufgeheizt und die Anlage stellt sich wieder ab. Alle weiteren Boiler werden automatisch miterhitzt. Bei höherem Wasserverbrauch sollten Sie die Anlage eventuell auf Dauerbetrieb umschalten, da diese Methode energiewirtschaftlich günstiger ist. [S. 1]

```
Kesseltemperatur   74°
```
Aktuelle Kesseltemperatur. [S. 1]

```
B1 B2 B3 B4
*
```
Boilereinstellungen werden angezeigt bis Boiler 24. Die Anwahl des Boilers erfolgt mit der + / - Taste. Um den Wert für diesen Boiler zu ändern gehen Sie mit V in die nächste Menüebene. Mit Z kommen sie eine Ebene höher und mit + / - ändern Sie die Werte. Nachfolgende Einstellungen gelten immer spezifisch für die einzelnen Boiler. [S. 1]

```
Boiler 1 Temp.     38°
Boiler 1 SOLL      60°
```
Aktuelle Boiler-Temperatur / gewünschte Boiler-Temperatur. [S. 1]

```
Boiler 1 Temp.     38°
Boiler 1 START     40°
```
Aktuelle Boiler-Temperatur / Boiler-Starttemperatur. Bei Unterschreitung der „START"- Temperatur wird die Anlage gestartet. [S. 1]

```
Boiler 1 Temp.     38°
Boiler Hysterese    5°
```
Boiler-Hysterese: Ist die Heizanlage in Betrieb, so schaltet die Boilerladepumpe 5° unter Boiler SOLL wieder ein. [S. 1]

```
Boilerfreigabe
Pumpe EIN bei      63°
```
Erst über dieser Kesseltemperatur schaltet sich die Boilerpumpe bei Bedarf ein (Basistemperatur). [S. 1]

ACHTUNG: Im „Boilerbetrieb" ist die Rücklaufanhebepumpe an die Boilerladepumpe gebunden und schaltet erst mit Erreichen der „Boilerfreigabe Temp." ein, bei Erreichen der „Boiler-Soll Temp." mit einer Verzögerung von 300 sec. wieder aus. Somit wird verhindert, dass die RLAH-Pumpe den Puffer wieder entleert. [S. 1]

```
Resttemp.Verwertung AUS
  EIN + / AUS -
```
Mit +/- können sie die Resttemp.Verwertung EIN/AUS schalten. Gilt in allen Betriebsarten. Ist die Resttemperaturverwertung eingeschaltet, so wird die nach dem Abschalten im Kessel befindliche Energie in den Speicher geladen, bis eine Temperaturdifferenz zwischen Boiler und Kessel von 5° besteht. [S. 1–2]

```
B.UWP Freigabe     EIN
Freig.1  EIN     00:00
```
Ab dieser Zeit beheizt die Anlage den Boiler (z.B.: 5:00 morgens). EIN/AUS gibt den aktuellen Status an. [S. 2]

```
B.UWP Freigabe     EIN
Freig.1  AUS     00:00
```
Ab dieser Zeit beheizt die Anlage den Boiler (z.B.: 9:00 morgens) nicht mehr. EIN/AUS gibt den aktuellen Status an. [S. 2]

```
B.UWP Freigabe     EIN
Freig.2  EIN     00:00
```
Ab dieser Zeit beheizt die Anlage den Boiler (z.B.: 16:00). EIN/AUS gibt den aktuellen Status an. [S. 2]

```
B.UWP Freigabe     EIN
Freig.2  AUS     00.00
```
Ab dieser Zeit beheizt die Anlage den Boiler (z.B.: 19:00) nicht mehr. EIN/AUS gibt den aktuellen Status an. [S. 2]

**Puffer-Betrieb** (menu items; the hydraulic explanation is in system-integration.md, Kap. 7):

```
Boiler 1  mit   2 PT100
  1PT100/2PT100
```
(ZS) Mit „+" stellen Sie in den Zusatzparameter Service den Boiler auf 2-Fühlerbetrieb um. [S. 2]

```
Boiler 1 Temp.     53°
Fühler oben
```
(B1) Ist Boiler 1 auf 2 Fühler eingestellt (Zusatzparameter Service), so kann unter B1 nur mehr die „Start" Temperatur eingestellt werden. Die Boiler (Puffer) „Soll-Temperatur" ist unter B2 einzustellen. [S. 2]

```
Boiler 1 Temp.     53°
Boiler 1 START     65°
```
(B1) [S. 2]

```
Boiler 2 Temp.     43°
Boiler 2 SOLL      75°
```
(B2) Am „B2" ist nur die „Boiler SOLL" Temperatur einzustellen. [S. 2]

```
Boiler 2 Temp.     43°
Fühler unten
```
(B2) [S. 2]

```
Solar M1+2      B1=EIN
  AUS/B1/B4/.../B22
```
(ZS) Durch das aktivieren der Funktion „Solar" sind die ausgewählten Mischkreise dem jeweiligen Pufferspeicher zugeordnet. [S. 3]

### Parameterliste Boilerbetrieb — Für jeden Boiler individuell einstellbar! [SL-P BA 2008, Kap. 7, S. 3]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Boiler SOLL | Max. Boilertemperatur | 10-100° | 60° |
| Boiler START | Unterste Boilertemperatur | 5-58° | 40° |
| Boiler Hysterese | | 0 bis 40° | 5° |
| Boilerpumpe EIN | Einschalttemp. der Ladepumpe | 1 bis 100° | 63° |
| Freig. 1 EIN | | 00:00 bis 24:00 | 00:00 |
| Freig. 1 AUS | | 00:00 bis 24:00 | 00:00 |
| Freig. 2 EIN | | 00:00 bis 24:00 | 00:00 |
| Freig. 2 AUS | | 00:00 bis 24:00 | 00:00 |

---

## Kap. 8 — Uhr - Boilerbetrieb (timer + boiler operation) [SL-P BA 2008, Kap. 8, S. 1–2]

Es wird die Temperatureinstellung von der Betriebsart „Boilerbetrieb" verwendet. Die Anlage zündet erst, wenn die freigegebene Zeit erreicht ist und die Boilertemperatur unterschritten wurde. Diese Betriebsart ist geeignet für die Zusammenarbeit mit einer Solaranlage. Sie können der Heizanlage mitteilen, dass die Anlage z.B. erst nach 16:00 Uhr bei Bedarf den Boiler nachheizt. Der Boiler wird bis zur Boiler SOLL Temperatur aufgeheizt. [S. 1]

```
Kesseltemperatur   74°
Uhrzeit          16.15
```
Aktuelle Kesseltemperatur / Aktuelle Uhrzeit. [S. 1]

```
Boilerheizfreigabe
1 EIN            05:00
```
Freigabezeit 1 der Anlage. [S. 1]

```
Boilerheizfreigabe
1 AUS            07:00
```
Sperrzeit 1 der Anlage. [S. 1]

```
Boilerheizfreigabe
2 EIN            00:00
```
Freigabezeit 2 der Anlage. [S. 1]

```
Boilerheizfreigabe
2 AUS            00.00
```
Sperrzeit 2 der Anlage. [S. 1]

```
Boilerheizfreigabe
3 EIN            00.00
```
Freigabezeit 3 der Anlage. [S. 1]

```
Boilerheizfreigabe
3 AUS            00:00
```
Sperrzeit 3 der Anlage. Mit diesen 6 Parametern können Sie 3 Zeitfenster definieren, in denen bei Bedarf die Anlage gestartet wird. [S. 1]

```
Boiler 1 Temp.     60°
Kein Boilerfühler    2
```
Aktuelle Boilertemperatur. [S. 1]

```
Kein Boilerfühler    3
Kein Boilerfühler    4
```
Kann, je nach install. Modulen bis Boilerfühler 24 angezeigt werden. [S. 1]

```
Version       xxxxxx.x
Pellets:
```
Hier wird die aktuelle Programmversion angezeigt. Es handelt sich um ein Pellets-Programm. [S. 1]

```
Basis         xxxxxx.x
Pellets:
```
Wird die Quit - Taste gedrückt, so sehen Sie die Basisversion des Programms. [S. 1]

### Parameterliste Uhr-Boilerbetrieb, Boiler 1 [SL-P BA 2008, Kap. 8, S. 2]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| 1 EIN | Freigabezeit 1 | 00:00 – 24:00 | 00:00 |
| 1 AUS | Sperrzeit 1 | 00:00 – 24:00 | 00:00 |
| 2 EIN | Freigabezeit 2 | 00:00 – 24:00 | 00:00 |
| 2 AUS | Sperrzeit 2 | 00:00 – 24:00 | 00:00 |
| 3 EIN | Freigabezeit 3 | 00:00 – 24:00 | 00:00 |
| 3 AUS | Sperrzeit 3 | 00:00 – 24:00 | 00:00 |

---

## Kap. 9 — Außentemperaturregelung (outdoor-temperature control) [SL-P BA 2008, Kap. 9, S. 1–8]

**Achtung:** Das Menü „Außentemp. Reg." ist keine Betriebsart, sondern ein Einstellungsmenü für die einzelnen Mischkreise. [S. 1]

**Funktion:** Die Steuerung ordnet einer Außentemperatur die erforderliche Vorlauftemperatur zu. Je kälter es draußen ist, desto höher wird die Vorlauftemperatur von der Steuerung vorgegeben. Hierzu ist es notwendig, eine Heizkurve zu erstellen. [S. 1]

**Die Heizkurve:** Die Heizkurve gibt an, welche Vorlauftemperatur bei einer bestimmten Außentemperatur gewählt wird. Die Steilheit der Heizkurve gibt an, um wie viel Grad sich die Vorlauftemperatur ändert, wenn die Außentemperatur um 1°C steigt oder fällt. [S. 1]

Graph on S. 1 (Außentemperaturkurve Max +20°C / Min -20°C, Vorlauftemperaturkurve Min 20°C / Max 50°C): A: Wert, den Sie unter „Außentemp. MAX" einstellen. B: Wert, den Sie unter „Vorlauf MIN" einstellen. C: Wert, den Sie unter „Außentemp. MIN" einstellen. D: Wert, den Sie unter „Vorlauf MAX" einstellen. „Vorlauf MAX" ist die höchste angesteuerte Vorlauftemperatur. „Vorlauf MIN" und „Außentemp. MAX / MIN" sind nur Bezugspunkte auf der jeweiligen Kurve! [S. 1]

Bei einer Außentemp. von +20°C würde eine „Vorlauf SOLL" Temperatur von 20°C vorgegeben werden. Bei einer Außentemperatur von -20°C eine Vorlauf SOLL Temperatur von 50°C. Die Heizkurven sind individuell für Ihren Heizkreis zu erstellen. Nach einer gewissen Einstellungsphase und Erprobungphase müsste es nicht mehr notwendig sein, diese Werte zu ändern. [S. 1]

Die aktuelle Raumtemperatur kann über einen Raumtemperaturfühler in die Berechnung der „Vorlauf SOLL" Temperatur einbezogen werden. Dabei kann der Raumeinfluss von 0% (reine Außentemperaturregelung) bis 100% (reine Raumtemperaturregelung) frei unter dem Parameter „Raumeinfluss %" gewählt werden. Jeder geregelte Heizkreis kann mit einem eigenen Raumtemperaturfühler ausgestattet werden. Für die Raumtemperaturregelung ist ebenfalls eine Temperaturkurve zu erstellen. [S. 1]

**Erstellen der Raumtemperaturkurve:** Graph on S. 2 (Raumtemperaturkurve Max +25°C / Min +15°C, Vorlauftemperaturkurve Min 20°C / Max 50°C): A: Wert, den Sie unter „Raum MAX" eingeben. B: Wert, den Sie unter „Vorlauf MIN" eingeben. C: Wert, den Sie unter „Raum MIN" eingeben. D: Wert, den Sie unter „Vorlauf MAX" eingeben. Bei einer Raumtemperatur von 15°C würde eine „Vorlauf Soll" Temperatur von 50°C vorgegeben werden. Bei einer Raumtemperatur von 25°C eine „Vorlauf SOLL" Temperatur von 20°C. Achtung: Auch „Raum MIN" und „Raum MAX" sind keine angesteuerten Fixwerte, sondern nur Bezugspunkte auf der Raumtemperaturkurve. [S. 2]

(Das Raumgerät and its switch positions A–F: see system-integration.md, Kap. 9.)

**Einstellen der Parameter:** Die Parameter gelten jeweils für den ausgewählten Heizkreis (M1, M2, ...M16). Mit der +/- Taste können Sie die jeweiligen Mischerkreise auswählen. Mit der V/Z Taste können Sie in die nächsten Menüebenen weiterschalten. [S. 4]

```
M1 M2 M3 M4
*
```
Mit der +/- Taste den gewünschten Heizkreis auswählen. Wird eine mischergesteuerte Rücklaufanhebung montiert, so ist für diese immer Heizkreis 1 (M1) zu verwenden. [S. 4]

```
Modul        vorhanden
Mischerkreis       AUS
```
Anzeige des akt. Status. Mir der +/- Taste können Sie den Mischkreis Ein/Aus-schalten, [S. 4]

```
Modul        vorhanden
Mischerkreis       EIN
```
```
Modul        vorhanden
Rücklaufmischer    EIN
```
Auf Rücklaufanhebung stellen (Nur Mischkreis 1) oder [S. 4]

```
Modul        vorhanden
Nachtabsenkung     EIN
```
ständig abgesenkt betreiben [S. 4]

```
Modul            fehlt
Mischerkreis       EIN
```
Sind keine weiteren Module installiert oder ist die Busverbindung unterbrochen, so wird dies hier angezeigt. [S. 4]

```
Uhrzeit          21:43
```
Aktuell eingestellte Uhrzeit. (Sommerzeit stellt sich selbstständig um) [S. 4]

```
Mo Di Mi Do Fr Sa So
*
```
Mit der +/- Taste können Sie den aktuellen Wochentag einstellen. [S. 4]

Die nachfolgenden 4 Absenkzeiten „Tag 1 EIN/AUS" und „Tag 2 EIN/AUS" können für jeden Wochentag spezifisch eingestellt werden. Wenn die gleiche Einstellung auf den nächsten Tag kopiert werden soll, so drücken Sie die „Quit"-Taste, und wählen mit der „+" Taste den nächsten Tag. Die eingestellten Werte können Sie in der Tabelle am Ende des Kapitels notieren. [S. 5]

```
*
Tag 1 EIN  T     05:00
```
Beginn Volllast [S. 5]
```
*
Tag 1 AUS  T     09:00
```
Ende Volllast [S. 5]
```
*
Tag 2 EIN  T     16.00
```
Beginn Volllast [S. 5]
```
*
Tag 2 AUS  T     22:00
```
Ende Volllast [S. 5]

Die oben angefügten Werte würden folgendes Heizbild ergeben (bar diagram on S. 5: Volllast 05:00–09:00 and 16:00–22:00, Abgesenkt otherwise): In der Zeit von 5:00 bis 9:00 und von 16:00 bis 22:00 Uhr würde die Anlage nach der errechneten „Vorlauf SOLL" Temperatur lt. Heizkurve regeln. In der Zeit von 22:00 bis 5:00 und von 9:00 bis 16:00 Uhr würde diese „Vorlauf SOLL" Temperatur um den Wert, der unter „Vorlaufabsenkung" eingegeben ist, reduzieren. In den Zeitfenstern steht der Hinweis T für Vollbetrieb und N für abgesenkten Betrieb. [S. 5]

```
Vorlauf SOLL       40°
Vorlaufabsenkung   20°
```
Aus der Heizkurve errechnetes Vorlauf SOLL / Temperatur, um die der Vorlauf abgesenkt werden soll [S. 5]

```
Vorlauf IST        **°
Vorlauf max        50°
```
Aktuelle Vorlauftemperatur / Heizkurve Vorlauf MAX [S. 5]

```
Vorlauf SOLL       40°
Vorlauf min        30°
```
Anzeige: Aus der Heizkurve errechnetes Vorlauf SOLL / Heizkurve: Vorlauf MIN [S. 5]

```
Aussentemp.IST    -14°
Aussentemp. max    20°
```
Anzeige: Aktuelle Außentemperatur / Heizkurve: Außentemperatur MAX [S. 5]

```
Aussentemp.IST    -14°
Aussentemp. min   -20°
```
Anzeige: Aktuelle Außentemperatur / Heizkurve: Außentemperatur MIN [S. 6]

```
Raum IST - 50      20°
Zuord.Raumfühler     1
```
Anzeige: Aktuelle Raumtemperatur. Hier kann ein bestimmtes Raumgerät diesem HK zugeordnet werden. Es können auch mehrere HK das gleiche Raumgerät verwenden. [S. 6]

Nach „Raum IST" wird angezeigt, welche Schalterstellung das Raumgerät hat: `-` kein Raumgerät vorhanden; `A` für AUS; `N` für Abgesenkt (Mond.Symbol); `B` für Boilerbetrieb (in der Hausanl. wurde Boiler ausgewählt); `UB` für Boilerbetrieb (in der Hausanl. wurde Uhrboiler ausgewählt); `E` für Error (keine ordnungsgemäße Messung möglich); `T` für Absenkung deaktiviert (Sonne-Symbol); `U` für Normalbetrieb (Uhr-Symbol). Die Zeit gibt an, ab wann die Anlage in die am Raumgerät eingestellte Betriebsart wechselt. [S. 6]

```
Raum IST  -50      20°
Raum max           23°
```
Anzeige: Aktuelle Raumtemperatur / Heizkurve: Raumtemperatur MAX [S. 6]

```
Vorlauf SOLL       40°
Raum min           18°
```
Anzeige: Aus der Heizkurve errechnetes Vorlauf SOLL / Heizkurve: Raumtemperatur MIN [S. 6]

```
Vorlauf SOLL       40°
Raumeinfluss       50%
```
Anzeige: Aus der Heizkurve errechnetes Vorlauf SOLL / Gewichtung der Raumtemperaturkurve zur Außentemperaturkurve [S. 6]

```
Heizung
Frostschutz bei   -50°
```
Bei Unterschreitung dieser Temperatur schalten alle Heizungspumpen ein [S. 6]

```
Heizung
Pumpe EIN bei      55°
```
Die Heizkreispumpen schalten erst bei Kesseltemp. von >55°C ein [S. 6]

```
Heizung
Pumpe AUS bei      50°
```
Die Heizkreispumpen schalten bei einer Kesseltemp. von <50°C aus [S. 6]

Die folgenden Parameter haben unterschiedliche Funktionen wenn die Anlage **mit Raumgerät** oder **ohne Raumgerät** betrieben wird.

**a) Betrieb der Anlage ohne ein Raumgerät:** Die Anlage schaltet die Pumpen entsprechend den Einstellungen „AUS" und „EIN". Die Anlage selber heizt jedoch weiter bis „Kessel Soll" erreicht ist, wechselt in den „Stocker Stopp" und startet wieder bei erreichen der „Kessel MIN" Temperatur, unabhängig der aktuellen Anforderung. [S. 6]

**b) Betrieb der Anlage mit einem Raumgerät:** Die Anlage schaltet die Pumpen entsprechend den Einstellungen „AUS" und „EIN". Sind alle Pumpen im System abgeschaltet (= es besteht keine Energiebedarf mehr) so schaltet der Kessel ab. Erste wenn aus den Heizkreisen oder dem Boilern eine Anforderung gemeldet wird startet die Anlage wieder. [S. 6–7]

```
Aussentemp IST     28°
Pumpe AUS bei      15°
```
Anzeige: Aktuelle Außentemperatur / Die Heizkreispumpe schaltet bei einer Außentemp. über 15°C ab. [S. 7]

```
Anlage AUS durch AT
AT-Abschalt.bei    15°
```
Ist die Anlage aufgrund der Außentemperatur abgeschaltet, so erscheint diese als Meldung am Display. [S. 7]

```
HZ Nachtabschalt.  AUS
UWP Freigabe     00:00
```
Anzeige: Aktueller Status EIN/AUS / Zeit, wann die Heizkreispumpe einschalten soll. [S. 7]

```
HZ Nachtabschalt.  AUS
UWP Sperre       00:00
```
Anzeige: Aktueller Status EIN/AUS / Zeit, wann die Heizkreispumpe ausschalten soll. [S. 7]

```
Abschaltung durch
  UWP Sperrzeit
```
Ist die Anlage aufgrund dieser Sperrzeit abgeschaltet, so erscheint diese als Meldung am Display. [S. 7]

```
HZ Nachtabschalt.  AUS
UWP Freigabe    <   7°
```
Anzeige: Aktueller Status EIN/AUS / Sinkt die Außentemperatur unter den Wert dieses Parameters, so wird der Parameter „UWP Sperre xx:xx" umgangen und die Pumpe schaltet ein. Ist für jeden Heizkreis frei einstellbar. [S. 7]

```
Abschaltung durch
  Raumgerät
```
Eine Abschaltung durch das Raumgerät wird ebenfalls am Display angezeigt. [S. 7]

### Parameterliste f. Außentemperaturregelung [SL-P BA 2008, Kap. 9, S. 8]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Nacht1 AUS | Ende der Absenkzeit 1 | 00:00 – 24:00 | 00:00 |
| Nacht1 EIN | Beginn der Absenkzeit 1 | 00:00 – 24:00 | 00:00 |
| Nacht2 AUS | Ende der Absenkzeit 2 | 00:00 – 24:00 | 00:00 |
| Nacht2 EIN | Beginn der Absenkzeit 2 | 00:00 – 24:00 | 00:00 |

Diese Werte können für jeden Wochentag getrennt vergeben werden (Mo–So table; blank in the manual).

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Vorlaufabsenkung | Absenktemperatur | 0-50°C | 20°C |
| Vorlauf max | Vorlaufkurve max | 37 bis 125°C | 50°C |
| Vorlauf min | Vorlaufkurve min | 0 bis 73°C | 30°C |
| Außentemp.max | Außentemp.Kurve max | 0 bis 50°C | 20°C |
| Außentemp.min | Außentemp.Kurve min | -50 bis 50°C | -20°C |
| Raum max | Raumtemp.Kurve max | 20° bis 40°C | 23°C |
| Raum min | Raumtemp.Kurve min | 0 bis 21°C | 18°C |
| Raumeinfluss | Verhältnis AT/RT | 0-100% | 50% |
| Frostschutz bei*° | Frostschutzeinrichtung | -50 bis 10°C | -50°C |
| Heizung Pumpe EIN bei | Einschalttemp. der Heizungspumpen | 65 bis 100°C | 55°C |
| Heizung Pumpe AUS bei | Ausschalttemp. der Heizungspumpen | 0 bis 70°C | 50°C |
| Pumpe AUS bei | Abschalttemp. d. Pumpe | 0° bis 30°C | 15°C |
| UWP Freigabe | Einschaltzeit der Anlage | 0.00 bis 24.00 | 00:00 |
| UWP Sperre | Abschaltzeit der Anlage | 0:00 bis 24:00 | 00:00 |
| UWP Freigabe | Freigabe lt. Außentemp. | -55 bis +50°C | -50°C |

> GAP: "Heizung Pumpe EIN bei" has Standard 55°C but a printed Einstellbereich of 65 bis 100°C — the default lies outside the printed range. Transcribed as printed; see verification.md.

> GAP: The "Absenkzeiten" are named "Tag 1/2 EIN/AUS" in the menu (S. 5) but "Nacht1/2 EIN/AUS" in the parameter list (S. 8). Transcribed as printed; the mapping between the two names is not stated.

---

## Kap. 10 — Prüfbetrieb (test / emission-measurement mode) [SL-P BA 2008, Kap. 10, S. 1–2]

Der Prüfbetrieb ist eine spezielle Betriebsart für die Abgasmessung. Die Messung darf nur bei 100% Kesselleistung durchgeführt werden.

**Folgende Parameter sind im Prüfbetrieb geändert:**
- Kessel Soll wird auf 90°C gesetzt, der Kessel moduliert erst ab 80°C.
- Der Betriebsartenwechsel in den Prüfbetrieb ist kein Aus/Ein Signal.
- Die Mischkreise regeln auf das eingestellte „Vorlauf Max", damit die Wärme entsprechend abgeleitet wird. Die Abschaltung aufgrund Aussentemp. ist deaktiviert.
- Die Ein- und Ausschalt-Temperaturen der Heizkreispumpen sind identisch zum Regelbetrieb.
- Die Boilerladepumpen werden eingeschaltet. Die Pumpen schalten lt. eingestellter „Pumpe EIN" Temperatur und „Pumpe AUS" Temperatur (Boilerbetrieb). Es gibt keine Begrenzung durch Boiler Soll Temperatur.
- Die Sperre der Boilerladepumpen wegen zu geringer Temperaturdifferenz zwischen Kessel und Boiler (im Regelbetrieb 5°C) ist deaktiviert.

**Vorgehensweise:**

```
aktiviere mit Taste
Quit und Prüfbetrieb
```
Wird auf die Taste Prüfbetrieb gedrückt, so erscheint die Meldung „aktivieren mit Quit und Prüfbetrieb". Erst wenn beide Tasten gemeinsam gedrückt werden, wird der Prüfbetrieb gestartet. [S. 1]

```
Prüfbetrieb
wurde aktiviert
```
Es erscheint kurz die Meldung „Prüfbetrieb wurde aktiviert". Entsprechend dem aktuellen Anlagenstatus wird die Messung freigegeben oder in einer Meldung angezeigt, warum jetzt keine Messung möglich ist. [S. 1]

```
Keine Messung
Zündung
```
Die Anlage befindet sich noch im Zündprogramm. Abwarten, bis die Anlage in den Regelbetrieb geht. [S. 1]

```
Messung
Bitte warten
```
Die Anlage ist im Regelbetrieb, hat aber noch nicht 100% Kesselleistung erreicht. („Pausezeit IST" > „Pausezeit Min") [S. 1]

```
Messung
freigegeben
```
Die Anlage hat jetzt 100% Leistung erreicht. Es kann mit der Abgasmessung begonnen werden. [S. 1]

```
Messung Achtung
keine Wärmeabgabe
```
Im Prüfbetrieb wird die „Kessel SOLL" Temperatur auf 90°C erhöht. Der Kessel moduliert erst bei 80°C. Ab diesem Zeitpunkt kommt die Meldung „keine Wärmeabgabe". Da der Kessel bereits die Leistung reduziert, ist keine korr. Messung mehr möglich. Für mehr Wärmeabnahme sorgen und neue Messung beginnen. [S. 2]

```
Keine Messung
Heizanlage Aus
```
Ist die Anlage über die „AUS" Taste am Display oder über das Raumgerät abgeschaltet, so erscheint die Meldung „Heizanlage Aus". [S. 2]

```
Keine Messung
Stocker Stop
```
Ist die Anlage abgeschaltet, weil „Kessel Soll" erreicht ist, so wird „Keine Messung – Stocker Stop" angezeigt. [S. 2]

```
Prüfbetrieb
```
Erscheint durch Drücken der Taste Prüfbetrieb, wenn dieser schon aktiviert wurde. Mit dem Auswählen einer Betriebsart wird der Prüfbetrieb beendet. [S. 2]

---

## Kap. 11 — Handbetrieb (manual mode) [SL-P BA 2008, Kap. 11, S. 1–2]

Zum Testen der einzelnen elektrischen Anlagenkomponenten oder bei eventuellen Störungen kann die Anlage auf Handbetrieb umgeschaltet werden. Durch Drücken der Taste + / - wird die entsprechende Aktion ausgeführt.

```
Brenner Füllen     -/+
Akt. Füllzeit       0s
```
Mit der „+" Taste starten Sie das Brenner Füllen. Mit „-" stoppen sie den Motor wieder. [S. 1]

```
Putzen: Handbetrieb
 - ZU  / + AUF   *
```
Mit der + / - Taste wird die Putzschwinge geöffnet oder geschlossen. Der Motor stoppt, wenn der Sensor belegt ist. Achten Sie darauf, dass die Drehschwinge nach der manuellen Reinigung immer als geschlossen angezeigt wird, da sonst am Display die Meldung „Brennerstörung" erscheint. Der Stern am Display kennzeichnet den geschlossenen Zustand des Brenners. [S. 1]

```
Putzen: STOP-/Start+
Putzzeit:      0F / 0S
```
Durch Drücken der + / - Taste wird der Putzvorgang gestartet. Der Motor stoppt, wenn der Sensor belegt ist. [S. 1]

```
Stocker         00mA +
Erdtank         00mA -
```
Beim Drücken der Taste + läuft der Stockermotor (Anzeige: Stromaufnahme). Ist eine Förderschnecke von einem Erdtank am Ausgang „Austragung" angeschlossen, so kann diese hier gestartet werden. [S. 1]

```
Putzmotor         00mA
Externer Start     AUS
```
Der Putzmotor läuft, solange die Taste +/- gedrückt wird. Anzeige auf aktuellen Status (AUS od. EIN). [S. 1]

```
Lüfter V1           0%
```
Der Saugzuglüfter kann hier eingeschaltet werden (in 5%-Schritten ansteigend) [S. 1]

```
Glühstab             +
EIN=   0s/AUS=      0s
```
Glühstab wird beheizt, solange die Taste gedrückt bleibt. (Achtung: der Glühstab kann bei zu langer Betätigung Schaden nehmen!!) [S. 1]

```
Boilerladepumpe 1    +
Boilerladepumpe 2    -
```
Die Ladepumpe1 läuft, solange die Taste gedrückt ist. Die Ladepumpe2 läuft, solange die Taste gedrückt ist. [S. 1]

```
Boilerladepumpe 3    +
Rücklaufanhebung     -
```
Die Ladepumpe3 läuft, solange die Taste gedrückt ist. Die Rücklaufanhebepumpe kann eingeschaltet werden. [S. 1]

```
Alarm                +
Heizungspumpe        -
```
Test der angeschlossenen Hupe/Blinklicht. Test aller angeschlossenen Heizungspumpen. [S. 1]

```
STB              <100°
Drehrost geschlossen
```
Anzeige über Status des STB. Anzeige Drehrost geschlossen/offen. [S. 1]

```
Mischer AUF          +
Mischer ZU           -
```
Bei Betätigung der „+" oder „-" Taste öffnen bzw. schließen alle angeschlossenen Mischer, die auf EIN gestellt sind. [S. 2]

```
Saugposition 1       +
Saugposition 2       -
```
Manuelle Anwahl von Saugposition 1 / 2. [S. 2]

```
Saugposition 3       +
Saugposition 4       -
```
Manuelle Anwahl von Saugposition 3 / 4. [S. 2]

```
Sauger             +/-
Behälter    nicht voll
```
Manueller Start der Saugturbine mit +; (Achtung: läuft solange, bis –Taste gedrückt wird!!) Anzeige Behälter voll / nicht voll. [S. 2]

---

## Kap. 12 — Zusatzparameter Verbrennung (combustion service parameters) [SL-P BA 2008, Kap. 12, S. 1–3]

Durch einmaliges, gleichzeitiges drücken der Tasten „V" und „Z" erreichen Sie dieses Menü aus jeder Betriebsart. Zurück kommen Sie durch Drücken einer beliebigen Betriebsarttaste. Den Wert ändern Sie mit der „+" oder „-" Taste.

```
Abgas IST           0°
Kesselleistung    100%
```
Aktuelle Abgastemperatur / Aktuelle Kesselleistung [S. 1]

```
Leistung   15KW
```
Aktuell eingestellte Leistungsstufe. Das Programm gilt immer für alle 4 Leistungsbereiche (SL-P 8,12,15 und 25). Hier ist die entsprechende Leistungsstufe einzustellen. **Die Einstellung muss mit der Bauart des Kessels übereinstimmen, da sonst Schaden an der Anlage entstehen kann.** **Achtung!: Bei Programm-Updates wird immer Leistungsstufe 15 kW installiert.** [S. 1]

```
Pausenzeit      250 zs
Pause MIN        33 zs
```
Anzeige „aktuelle Pausenzeit" / Eingestellte „Pause MIN" Zeit. [S. 1]

```
Pausenzeit      250 zs
Pause MAX       120 zs
```
Anzeige „aktuelle Pausenzeit" / Eingestellte „Pause MAX" Zeit [S. 1]

```
Pausezeit       250 zs
Pause Start     250 zs
```
Anzeige „aktuelle Pausenzeit" / Eingestellte „Pause Start" Zeit. [S. 1]

„Aktuelle Pausenzeit": Während der Zündung: Kessel beginnt mit „Pause Start" (250zs) Pause. Regelbetrieb: Im Regelbetrieb sinkt die Pausenzeit stufenweise auf den unter „Pause MIN" eingestellten Wert. Reduktionsphase: Für die Reduktionsfase gibt es mehrere Systemzustände: a) Ist eine Boiler- oder Pufferladung aktiv so beginnt der Kessel 10° vor dem Kessel Soll mit der Reduktion. b) Ist eine Heizkreisanforderung als höchste Anforderung aktiv, so beginnt der Kessel ab dieser Temperatur zu reduzieren mindestens jedoch >55° c) Ist weder eine Heizkreis- oder Boileranforderung bekannt (z.B.: EIN über Externen Start) so beginnt der Kessel bei 10° vor dem Kessel Soll mit der Reduktion. Die Pausenzeit erhöht sich schrittweise von „Pause MIN" auf die „Pause Max" Zeit. [S. 1]

> GAP: The unit "zs" is used throughout Kap. 12 and is not defined anywhere in the document. See verification.md.

```
Förderzeit        0 zs
Soll             18 zs
```
aktuelle Förderzeit. Im Regelbetrieb schiebt die Stockerschnecke den hier eingestellten Zeitraum ein. Achtung: die tatsächliche Förderzeit verändert sich wenn der Kessel die Lambda-Vorabschaltung erreicht. [S. 1–2]

```
Förderzeit        0 zs
Start            20 zs
```
Eingestellt Start Förderzeit. [S. 2]

```
Aktuell             0s
Starteinschub     200s
```
Tats. Förderzeit; zählt herunter während die Stockerschecke läuft. / Eingestellter Starteinschub. Nach dem Putzen und Saugen beginnt die Anlage mit dem Starteinschub. Ist ein 2. Zündversuch notwendig, wird der ½ Starteinschub durchgeführt. [S. 2]

```
Aktuell             0s
Starttaktzeit      10s
```
Aktuell eingestellte Starttaktzeit. Nach dem Starteinschub fördert die Anlage solange Material in den Brennraum, bis die Starttaktzeit erreicht ist. Dabei wechseln sich die „Pause Start"- Zeit und die „Förderzeit Start" ab. Ist die Starttaktzeit erreicht, so wird kein weiteres Material in den Brennraum gefördert, bis die Anlage in den Regelbetrieb wechselt. [S. 2]

```
Lambda Ist           0
Lambda SOLL        510
```
Aktueller Lambda-Wert. Bei Erreichen von Lambda-Soll wird die V1 Drehzahl auf den eingestellten Wert „V1 MAX" gestellt. Die Lambda0 Steuerung kommt nur zum Tragen, wenn die Anlage mit Pause-MIN läuft (z.B.: Regelbetrieb mit 100% Kesselleistung). [S. 2]

```
Lambda Ist           0
Lambda0            490
```
Aktueller Lambda-Wert. / Eingestellter Lambda0 Wert. [S. 2]

```
Aktuell             0s
Lambda0 Timer     2Min
```
Aktuelle Zeit, wenn Lambda0 Steuerung aktiviert ist. / Eingestellter Lambda0 Timer Wert. Ist der aktuelle Lambda-Wert für die unter „Lambda0 Timer" eingestellte Zeit unter dem „Lambda0-Wert" so wird die V1 Drehzahl auf den eingestellten Wert „V1 MAX" gestellt [S. 2]

```
Lambda Ist           0
Vorabschaltung 1   520
```
Aktueller Lambda-Wert. Steigt der Lambda-Wert über „Vorabschaltung 1", so verkürzt sich die „Förderzeit SOLL" um 1/3. [S. 2]

```
Lambda Ist           0
Vorabschaltung 2   530
```
Aktueller Lambda-Wert. Steigt der Lambda-Wert weiter bis „Vorabschaltung 2", so verkürzt sich die „Förderzeit SOLL" um 2/3. [S. 2]

```
Lambda Ist           0
Lambda STOP        540
```
Aktueller Lambda-Wert. Steigt der Lambda-Wert weiter bis „Lambda STOP", so wird der Einschub gestoppt. [S. 2]

```
V1 IST              0%
V1 MIN             25%
```
Aktuelle Drehzahl des Saugzuggebläses / Eingestelltes MIN des Saugzuggebläses. Wird verwendet, wenn die Anlage im Regelbetrieb läuft. [S. 3]

```
V1 IST              0%
V1 MAX             30%
```
Aktuelle Leistung d. Saugzuggebläses. / Eingestelltes „V1 MAX". Bei erreichen von „Lamda SOLL" wird das Saugzuggebläse auf „V1 Max" erhöht. [S. 3]

```
V1 IST              0%
V1 START           60%
```
Aktuelle Leistung d. Saugzuggebläses. / Eingestellt Leistung des Saugzuggebläse beim Starten. „V1 START" wird verwendet beim Zündprogramm, bis die Anlage in den Regelbetrieb (Zünddifferenz erreicht) geht. [S. 3]

### Parameterliste für Zusatzparameter Verbrennung — Werkeinstellung der Einzelnen Kesseltypen SL-P 8 / 12 / 15 / 25 [SL-P BA 2008, Kap. 12, S. 3]

| Parameter | SL-P 8 | SL-P 12 | SL-P 15 | SL-P 25 |
|---|---|---|---|---|
| Pause MIN | 40 | 24 | 33 | 15 |
| Pause MAX | 75 | 75 | 120 | 120 |
| Pause Start | 250 | 250 | 250 | 250 |
| Förderzeit Soll | 10 | 9 | 18 | 20 |
| Förderzeit Start | 20 | 20 | 20 | 20 |
| Starteinschub | 120 | 120 | 200 | 200 |
| Starttaktzeit | 10 | 10 | 10 | 10 |
| Lambda Soll | 510 | 510 | 510 | 510 |
| Lambda0 | 490 | 490 | 490 | 490 |
| Lambda0 Timer | 2 | 2 | 2 | 2 |
| Vorabschaltung 1 | 520 | 520 | 520 | 520 |
| Vorabschaltung 2 | 530 | 530 | 530 | 530 |
| Lambda STOP | 540 | 540 | 540 | 540 |
| V1 MIN | 15 | 15 | 25 | 35 |
| V1 MAX | 20 | 20 | 30 | 45 |
| V1 START | 60 | 60 | 60 | 60 |

Alle diese Werte werden bei Programmupdates auf Werkeinstellung zurückgesetzt. [S. 3]

The "Pause MIN" row was re-read from the scan at full resolution and is confirmed as printed: 40/24/33/15. It is not monotonic across the model range; that is how the manual prints it. (An earlier GAP marker here is closed; verification.md lines 9 and 40.)

> GAP: Units for the table rows are not repeated in the table (the menu items use zs, s, Min and %).

---

## Kap. 13 — Zusatzparameter Service (service parameters) [SL-P BA 2008, Kap. 13, S. 1–4]

Durch zweimaliges, gleichzeitiges drücken der Tasten „V" und „Z" erreichen Sie dieses Menü aus jeder Betriebsart. Zurück kommen Sie durch Drücken einer beliebigen Betriebsarttaste. Den Wert ändern Sie mit der „+" oder „-" Taste.

```
Stocker           00mA
Maximalstrom     900mA
```
Aktuelle Stromaufnahme des Stockermotors / Einstellung Max. Strom. Um Schaden am Motor zu vermeiden dürfen die Ströme nicht höher hinaufgestellt werden. [S. 1]

```
Erdtank           00mA
Maximalstrom    1000mA
```
Der Ausgang 6 kann für einen externen Austragungsmotor (z.B.: Erdtankschnecken...) verwendet werden. Hier können lt. Zulieferer die max. Ströme eingestellt werden. Der Ausgang wird getaktet!! (125sec EIN, 10 sec. AUS). Der Ausgang wird sofort bei erreichen der „Vollmeldung" im Zwischenbehälter abgeschaltet. Die Saugturbine hat 10 sec. Nachlaufzeit. [S. 1]

```
Putzmotor         00mA
Maximalstrom    2500mA
```
Aktuelle Stromaufnahme des Putzmotors / Einstellung Max. Strom [S. 1]

```
Saugen / Putzen    AUS
Putzzeit           60s
```
Hier kann die „Putzzeit" (Länge des Putzvorganges) eingestellt werden. [S. 1]

```
Brenneraufzeit
Putzen AUF       50 zs
```
Zeit, die der Putzmotor im Handbetrieb unter „Brenner Auf" beschalten wird [S. 1]

```
Aktuell nach Freigabe
Putzintervall     100m
```
Aktueller Wert im Betrieb. Zählt vom eingestellten Wert herunter. / Eingestellter Putz / Reinigungsintervall. Nach Ablaufen dieser Zeit (Stockerlaufzeit in min.) wird die Anlage abgestellt und nach Ablauf der „V1 Nachlaufzeit" gereinigt. Anschließend erfolgt eine standardmäßige Zündung. [S. 1]

```
Aktuell nach Freigabe
Saugintervall     350m
```
Aktueller Wert im Betrieb. Zählt vom eingestellten Wert herunter. / Eingestellte Förderzeit. Nach Ablaufen dieser Zeit wird der Behälter wieder befüllt (Stockerlaufzeit in min.). Wird dieser Parameter zu weit hinaufgestellt, sodass der Behälter leer wird und das Feuer erlischt, geht die Anlage auf Störung => „Temperatur abgefallen" ; „Anlage neu starten"; Eintrag erfolgt im Fehlerspeicher und Datenlogger. Vor einem Saugvorgang erfolgt immer zuerst eine Reinigung. [S. 1]

```
Aktuell             0s
Max.Füllzeit      600s
```
Saugzeit nach der, falls vom Sensor keine „Voll-Meldung" kommt, auf die nächste Sonde weitergeschaltet wird. [S. 1]

```
Aktuell            0 s
Startzeit          17m
```
Aktuelle Zeit im laufenden Zündvorgang. / Gesamtzeit eines Zündvorganges. [S. 1]

Die Anlage führt max. 4 Zündversuche durch. Der 2. Zündversuch erfolgt mit halbem Starteinschub. Ist der 2. Zündversuch auch nicht erfolgreich, so erfolgt eine Reinigung. Der dritte Zündversuch ist analog dem ersten Versuch, der vierte analog dem Zweiten. [S. 2]

```
Pellets : Lambda-z
Zünddifferenz       3°
```
Aktuelle Zündungsart: Lambdazündung. Bei Einstellung 3° wechselt die Anlage in die „Lambdazündung". Bei der „Lambdazündung" merkt sich die Anlage am Beginn des Zündvorganges den niedrigsten Lambdawert. Wird dieser für mind. 2 Minuten um mehr als 10 Punkte überschritten, so wechselt die Anlage in den Regelbetrieb = Ende des Zündvorganges. [S. 2]

```
Pellets : Abgas-z
Zünddifferenz       4°
```
Aktuelle Zündungsart: Abgaszündung. Bei Einstellung 4° wechselt die Anlage in die „Abgaszündung". Bei der „Abgaszündung" merkt sich die Anlage am Beginn des Zündvorganges (ab Starteinschub) die aktuelle Abgastemperatur. Steigt diese um 4° oder mehr an, so wechselt die Anlage in den Regelbetrieb. = Ende des Zündvorganges. [S. 2]

```
Abgas IST           0°
Nachzünddifferenz  10°
```
Aktuelle Abgastemperatur. Nachzündfunktion wurde in diesem Programm wieder deaktiviert da sie nicht die gewünschten Vorteile gebracht hat. Hat somit keine Bedeutung mehr. [S. 2]

```
Aktuell            00s
V1 Nachlauf       420s
```
Anzeige aktuelle Nachlaufzeit / Mind. Nachlaufzeit des Saugzuggebläses. **Abstellen durch Stockerstopp:** Nach Erreichen der „Kessel Soll" Temperatur läuft der Saugzug die eingestellte Zeitspanne nach. Bei Erreichen der „Kessel MIN" – Temperatur startet die Anlage wieder. **Abstellen durch Sauganforderung:** Bei einer „Sauganforderung" läuft der Saugzug mind. die eingestellte Zeitspanne nach. Zusätzlich wird die unter „Kessel Temp. + Ventilator STOP" (ZS) eingestellte Temperaturdifferenz der Kesseltemperatur zur Abgastemperatur eingehalten. Erst dann wird der Saugvorgang eingeleitet. **Abstellen durch Reinigungsanforderung:** Bei einer Reinigungsanforderung läuft der Saugzug die eingestellt Zeitspanne nach. Anschließend wird die Anlage gereinigt und wieder gestartet.. [S. 2]

```
Nachlaufzeit
Zündung            60s
```
Hat die Anlage aus der Zündphase heraus in den Regelbetrieb gewechselt, so heizt der Zünder noch 60 sec. länger. [S. 2]

```
Aktuell             0s
Glühstab  EIN     250s
```
Aktuelle Zündzeit. [S. 2]

```
Aktuell             0s
Glühstab  AUS       1s
```
Der Zünder (Glühstab) wird getaktet. 250 sec. EIN und 1 sec. AUS. [S. 3]

```
Akt. Füllzeit       0s
Brenner Füllen     90s
```
Im Handbetrieb „Brenner Füllen" lt. hier eingestellter Zeit. [S. 3]

```
Betrieb-STD      0h00m
```
Aktuelle Betriebsstunden. Löschen mit +/- [S. 3]

```
Aktuell          30Min
Displayschoner   30Min
```
Einstellung Displayschoner [S. 3]

```
Komb.Boiler-Uhr    AUS
  EIN+/AUS-
```
**Achtung!!** Ist ein Raumgerät installiert ist dieser Parameter ungültig (=> kein Uhrzeitbetrieb). „AUS": Im „Uhrzeitbetrieb" wird Boiler nur während des eingestellten Zeitfensters (z.B.: 16-22 Uhr) beheizt. „EIN": auch außerhalb des eingestellten „Zeitfensters" wird der Boiler lt. „Boiler START" beheizt. [S. 3]

```
Legionellensch.    AUS
  AUS/MO/DI../SO
```
Die „Boiler SOLL" Temperatur wird am ausgewählten Tag auf 70°C gesetzt. Wird einmal 70°C erreicht, so wird auf das eingestellte „Boiler SOLL" zurückgesetzt. Es wird **keine** zusätzliche Boilerladung veranlasst!! Wird an diesem Tag der Boiler nicht geladen, so bleibt die Funktion unerfüllt. [S. 3]

```
Rostschutz         AUS
  AUS/MO/DI../SO
```
An ausgewähltem Tag werden alle Mischer und Pumpen kurz beschaltet. Verwendung: z.B.: im Sommer, damit sich keine Anlagenteile festlegen. [S. 3]

```
M1+2 Zuordnung zu
Transfermischer    AUS
```
Nur in Verbindung mit Transfermodul. Zuordnung in der Steuerung M1, M2, M3, M4 [S. 3]

```
M1+2 Zuordnung zu
Transfermischer      1
```
In diesem Fall wären die Mischkreise 1 und 2 am Ende der Fernleitung, die durch die Transferpumpe eins betrieben wird. [S. 3]

```
Boiler 1  mit   1 PT100
  1PT100/2PT100
```
Einstellmöglichkeit, ob der Boiler / Puffer mit einem oder zwei Fühlern ausgestattet ist. [S. 3]

```
Boiler 1  mit   2 PT100
  1PT100/2PT100
```
Der Boiler / Puffer ist auf 2-Fühler umgestellt, d.h. der Ausgang B1 im Modul ist der obere Fühler, der B2 der untere Fühler. Es kann immer der erste Boiler im Modul als Pufferspeicher verwendet werden (B1, B4, B7,…B22). Ist der Puffer auf 2 Fühler gestellt, so ist der B1 Fühler oben, der B2 unten. [S. 3]

```
Solar M1+2         AUS
  AUS/B1/B4/.../B22
```
Zuordnung des entsprechenden Mischkreises zu einem ausgewählten Puffer. Die „Boiler START" Temperatur (Fühler oben) muss höher sein als die „Pumpe START" Temp. des entsprechenden Mischkreises. Sonst steht die Pumpe. Der Kessel heizt bei erreichter überschrittener „Boiler START" Temp. nicht!! [S. 3–4]

```
Kesselübertemperatur
Vermeidung         90°
```
Alle Mischer werden auf eingestellt. Max aufgefahren und die Boilerladepumpe wird eingeschaltet. [S. 4]

```
Pufferübertemperatur
Vermeidung         90°
```
Gleich wie „Kesselübertemperatur" jedoch auf den Puffer bezogen. [S. 4]

```
Aktuell *          AUS
Extern Start:   Direkt
```
Aktueller Status (EIN = geschlossen; AUS = unterbrochen). **Direkt:** Die Anlage hält sich genau an die übergeordnete Steuerung: Externes Signal EIN: wird von Hand auf AUS gedrückt, so stoppt die Anlage. Nach der „V1 Nachlaufzeit" startet die Anlage wieder. Externes Signal AUS: wird von Hand auf EIN gedrückt, so startet die Anlage, wird aber nach der Mindestlaufzeit (20 min) wieder gestoppt. [S. 4]

```
Aktuell *          AUS
Extern Start:   Impuls
```
**Impuls:** Die Anlage wird nur über ein kurzes Signal geschaltet: Externes Signal EIN: wird von Hand auf AUS gedrückt, so stoppt die Anlage und bleibt gestoppt. Externes Signal AUS: genau gegengleich zum Signal EIN. [S. 4]

```
Aktuell *          AUS
Ext.Stop d. Fremdofen
```
Ext-Stop d. Fremdofen: Über einen Abgassensor im Rauchrohr eines "Zweitofens" kann die Heizkreisregelung auch bei kaltem Kessel betrieben werden (Heizkreispumpe EIN bei „Kesseltemperatur" wird umgangen). AUS= „Zweitofen" kalt – unser Kessel startet bei Anforderung. EIN = „Zweitofen" heiß – unser Kessel übernimmt Wärmeverteilung [S. 4]

```
Aktuell *          AUS
Sensor 70° Zwischenb
```
Sensor 70° Zwischenb: Am Ausgang 16 kann auch ein 70° Sensor installiert werden. (Schweiz) [S. 4]

```
Aktuell *          AUS
nur 70° auf Alarm
```
Nur wenn der „70° Sensor" am Zwischenbehälter anspricht wird der Alarmausgang in den Modulen beschaltet. Alle weiteren Fehler die normalerweise Alarm auslösen werden unterdrückt [S. 4]

```
Aktuell *          AUS
Protokollierung
```
Nur für Programmtests in der Entwicklungsumgebung notwendig. Hat für die Anlage keine Bedeutung. [S. 4]

```
Kesseltemp.         0°
+Ventilatorstop    20°
```
Temp. Differenz zw. Kesseltemp und Abgastemp. Erst dann wird z.B.: der Saugvorgang eingeleitet. Wird die Anlage mit Abgaszündung betrieben (Zünddifferenz >4°) ist der Wert auf 10° zu stellen. [S. 4]

> GAP: Kap. 13 has no printed Parameterliste with Einstellbereich/Standard columns; only the display example values above are given.

---

## Kap. 14 — Zusatzparameter Fühlerabgleich (sensor calibration) [SL-P BA 2008, Kap. 14, S. 1]

Durch gleichzeitiges Drücken der Tasten **V** und **Z** aus dem Hauptmenü erreichen Sie diese Ebene. Zurück gelangen Sie durch Drücken einer Betriebsarttaste.

Die Werte für **Nullung** und **Normierung** aller Fühler sind vom Werk auf 100 gesetzt. Es kann in der Praxis jedoch vorkommen, dass die gemessenen Werte nicht exakt sind.

Um die Fühler abzugleichen, wird bei einer tiefen Temperatur die **Nullung** verändert. Nun wird der Fühler an ein heißes Medium gelegt und mit der **Normierung** der obere Temperaturpunkt passend dazugestellt. Bei den Raumtemperaturfühlern gibt es nur die **Nullung**.

Vermindert man die eingestellten Nullungs - Normierungswerte, so erhöhen sich die angezeigten Temperaturen. Zur Abgleichung der Fühler ist ein Temperaturmessgerät zu verwenden.

**Achtung:** Bei den Raumtemperaturfühlern und dem Außentemperaturfühler erfolgt bei der Messung eine Mittelwertbildung über mehrere Minuten. Diese Zeitverzögerung wirkt sich auch beim Fühlerabgleich aus.

Es sollten nur externe Geräte (Boilerfühler, Vorlauffühler, Raumfühler und Transfermischer) bei Bedarf angepasst werden. Die in den Kessel eingebauten Fühler (Abgas, Kesseltemp,..) unbedingt unverändert lassen.

> GAP: No menu items (display boxes) or parameter list are printed for this chapter; the names of the individual Nullung/Normierung entries are not given.

---

## Kap. 15 — Zusatzparameter Hausanlage (house-system service parameters) [SL-P BA 2008, Kap. 15, S. 1–3]

Durch zweimaliges gleichzeitiges Drücken der Taste V und Z aus dem Hauptmenü erreichen Sie diese Ebene. Zurück gelangen Sie durch Drücken einer Betriebsarttaste. Den Wert ändern Sie mit den +/- Tasten.

```
HZP: 1 2 3 4
```
Heizungspumpen. Der Stern zeigt an, welcher Heizungspumpenausgang aktiv ist. [S. 1]

```
M:   1 2 3 4
```
Mischer. + oder – zeigt Ihnen, ob der entsprechende Mischer auf- oder zufährt. [S. 1]

```
B: RL 1 2 3 4 5 6
```
Boilerpumpen und Boilerfühler. Der Stern zeigt an, welche Pumpe in Betrieb ist. Die drei Punkte zeigen an, dass ein Modul korr. angeschlossen und z.B. auf B1+2+3 konfiguriert ist. Achtung: Sind mehrere Module gleich konfig. so erkennt man das nur daran, dass die weiteren Anschlüsse z.B.: B4+5+6 fehlen. [S. 1]

```
Transfer: 1 2 3 4
```
Der Stern zeigt an, welche Pumpe in Betrieb ist. Die Punkte zeigen an, dass ein EM2 als Transfermodul angeschlossen ist und diesen z.B.: auf Tr1+Tr2 konfiguriert ist. [S. 1]

```
Rücklauf IST         °
Rücklauf SOLL      55°
```
aktuelle Rücklauftemp. (nur bei Mischergeregelter RLAH) / angestrebte Rücklauftemperatur. (Mixer-controlled RLAH set-up text: see system-integration.md, Kap. 15.) [S. 1]

```
Rücklaufanhebung
Pumpe EIN bei      40°
```
Bei dieser Kesseltemperatur schaltet sich die Rücklaufanhebung ein. [S. 1]

```
Rücklaufanhebung
Pumpe AUS bei     110°
```
Bei dieser Kesseltemperatur schaltet die Rücklaufpumpe aus. Um ein Überhitzen des Kessels zu vermeiden, diese Einstellung nicht verändern!! [S. 1]

```
Akt...TAKT          4s
Regelungstakt      20s
```
Mischerverstellzyklus. Im Abstand dieser Taktzeit werden die IST und SOLL Temperaturen verglichen und alle Mischer regeln entsprechend. Sollte sich Ihr Mischer immer von einem Extrem ins andere verstellen, ändern Sie die Zeit nach oben. Hiermit geben Sie dem trägen Temperaturfühler mehr Zeit sich anzupassen. [S. 2]

```
M1 Mischer steht
M1 Verstellzeit     5s
```
Anzeige Status d. Mischers: auf/zu/steht. / Verstellzeit pro Zyklus. Ist die Vorlauftemperatur IST um mehr als 15°C größer oder kleiner als die Vorlauftemperatur SOLL, so beträgt die Verstellzeit 3x jenen Wert in Sekunden pro Regelungstakt. Ist die Vorlauftemperatur IST in einem Bereich von +/- 1°C der Vorlauftemperatur SOLL, ist ein Verstellen des Mischers nicht von Nöten, erscheint in der Anzeige die Meldung „Mischer steht". Das Gleiche gilt auch für die Mischer 2-16. [S. 2]

```
Tr.Mischer 1 steht
Verstellzeit        5s
```
Anzeige Status d. Mischers : auf/zu/steht / Verstellzeit pro Zyklus [S. 2]

```
Mischerlaufzeit    300
```
Zeit, nach der die Pumpen ausschalten. Bekommt der Mischer die unter Mischerlaufzeit eingestellte Zeit nur „Zu" - Signale, weil die Vorlauf IST Temperatur höher als die Vorlauf SOLL Temperatur ist, so ist anzunehmen, dass kein Energiebedarf mehr vorliegt und die Pumpe wird abgeschaltet. Bei Unterschreiten der Vorlauf SOLL-Temperatur wird diese wieder eingeschaltet. Bei einer Einstellung der Mischerlaufzeit auf 5000 Sekunden (AUS) laufen die Heizkreispumpen auf Dauerbetrieb. [S. 2]

```
Raumsteuerung bei
Boilerb.: BOILER
```
```
Raumsteuerung bei
Boilerb.: UHR-BOILER
```
mit +/- können Sie einstellen, in welcher Betriebsart gewählt wird, wenn Sie den Raumtemperaturfühler auf „Boilerbetrieb" gestellt haben (Boiler oder Uhr-Boiler). [S. 2]

```
Mischer 1
Modul OK
```
```
Aussentemperatur
Modul OK
```
```
Boiler 1
Modul OK
```
(no description printed) [S. 2]

### Parameterliste Zusatzparameter Hausanlage [SL-P BA 2008, Kap. 15, S. 3]

| Parameter | Bezeichnung | Einstellbereich | Standard |
|---|---|---|---|
| Rücklauf SOLL | angestrebte RL-Temperatur | 1° bis 100°C | 63°C |
| RL-Pumpe EIN bei | Einschalttemp. der RL-Pumpe | 0° bis 120°C | 55°C |
| RL-Pumpe AUS bei | Ausschalttemp. der RL-Pumpe | 0° bis 120°C | 110°C |
| Regelungstakt | Vergleich IST-Soll aller Mischer | 15 bis 250 sec. | 20 sec |
| M1 Verstellzeit | Mischerverstellzeit Heizkreis | 1 bis 5 sec | 5 sec |
| TR Verstellzeit | Mischerverstellzeit Transferkreis | 1 bis 5 sec | 5 sec |
| Mischerlaufzeit | Schaltzeit Pumpe AUS | 0 bis 4999 / Aus | 300 sec |

> GAP: "Mischerlaufzeit" Einstellbereich is printed "0 bis 4999 / Aus" while the text on S. 2 says "5000 Sekunden (AUS)". "RL-Pumpe EIN bei" Standard 55°C differs from the display example "Pumpe EIN bei 40°" on S. 1, and "Rücklauf SOLL" Standard 63°C differs from the display example 55° and from Kap. 1, S. 5 ("auf 55° einzustellen"). Transcribed as printed; see verification.md.

---

## Kap. 17 — Fehlermeldungen (error messages) [SL-P BA 2008, Kap. 17, S. 1–3]

Printed chapter heading on S. 1 reads "14.) Beschreibung möglicher Fehlermeldungen und dazu Hinweise zum Beheben von Störungen !" while the footer and the contents page number it Kapitel 17.

**Vorsicht Verletzungsgefahr!** Bei manuellen Eingriffen der Anlage im Handbetrieb immer höchste Vorsicht walten lassen. Der Hersteller übernimmt keine Garantie auf Personenschäden durch unsachgemäße Wartung! [S. 1]

| Fehlermeldung | Abhilfe |
|---|---|
| **F2** Brennerstörung (wird nicht automatisch quittiert) | Am Display Quit Taste drücken (Fehlermeldung wird damit ca. 20 Sek. ausgeblendet). Danach in die Betriebsart „Handbetrieb" schalten. In zweiter Zeile „Putzen: Handbetrieb" die Taste „–" (Minus) kurz drücken, den offen gebliebenen Brenner schließen. Der eingeblendete Stern in der zweiten Zeile zeigt den geschlossenen Zustand des Brenners an. Gelingt das nicht, Brenner-Rost durch Drücken der Taste „+" (Plus) ganz öffnen, danach kontrollieren ob sich ein Fremdkörper zwischen Brennergrundplatte und Rost verklemmt hat, diesen entfernen und danach den Rost mit der Taste „–" wieder schließen. Eventuell Putzmechanik und Reinigungs-Federn auf Leichtgängigkeit kontrollieren. Danach die Anlage wieder starten. [S. 1] |
| **F3** Wasserfühler defekt | Kontrollieren auf einwandfreie Elektroinstallation bzw. Steckverbindung. Auf Temperatur im Heizraum achten, Fühler darf nicht im Minus °C Bereich messen. (Speziell bei Erstinbetriebnahme) [S. 1] |
| **F4** Zündstörung | Kontrolle, ob sich genug Heizmaterial im Brenner befindet bzw. überprüfen ob Glühstab funktioniert (kann im Handbetrieb kontrolliert werden). Es wäre auch möglich, dass aus dem Pellets-Behälter zu wenig oder keine Pellets gefördert werden können. Kontrolle, ob sich die Zellradschleuse und die Stockerschnecke während des Brennerfüll-Vorgangs dreht und auch Pellets vorhanden sind. [S. 1] |
| **F5** Übertemperatur Kessel | Beim Auftreten dieser Meldung kontrollieren, ob genügend Leistungsabnahme erfolgt bzw. dass eine Busverbindung zwischen Steuerung und Modul besteht. Richtige Einstellung des STB kontrollieren! Funktion der jeweiligen Pumpen und Mischer testen. **Achtung:** STB ist mechanisch zu entriegeln!! Der Knopf zum Entriegeln befindet sich über der Ofentür (schwarze Abdeckung) [S. 2] |
| **F6** Abgasfühler defekt | Steckverbindung und richtige Einstellung im Zusatzparameter (Fühlerabgleich) kontrollieren, ansonsten Kontakt mit Vertreter oder Firmenservice aufnehmen. Ab 330° Abgastemperatur wird der Abgas-Fühler als defekt angezeigt. Bei Absinken der Abgastemperatur wird diese Meldung wieder gelöscht. [S. 2] |
| **F9** Stockermotor Überstrom | Vermutlich befindet sich in der Zellradschleuse ein Fremdkörper. Zuerst Quit Taste drücken. Anlage auf Handbetrieb schalten und Stockerschnecke kurz manuell betätigen. Sollte die Schnecke blockiert sein, den Fremdkörper entfernen. [S. 2] |
| **F14** Putzstörung | Meldung quittieren. Anlage auf Handbetrieb schalten, danach Brennerrost durch drücken der „–" Taste schließen. Drehrostschalter muss belegt sein, danach Anlage wieder neu starten. Wird durch Neustart normalerweise automatisch quittiert! [S. 2] |
| **F16** Fehler am Putzmotor (Drehrostschalter) | Meldung quittieren. Kontrolle im Handbetrieb, ob Drehrost als geschlossen angezeigt wird. Wenn dies nicht der Fall ist, Drehrost mit Taste schließen. Eventuell auch auf richtige Einstellung des Drehrostschalters kontrollieren. (Abstand 2mm). [S. 2] |
| **F17** Fehler am Putzmotor (Überstrom) | Kontrolle, ob sich die Reinigungsfedern leicht auf und ab bewegen können, (dazu muss zuerst der Wärmetauscherdeckel entfernt werden). [S. 2] |
| **F19** Temperatur abgefallen – Anlage neu starten | Meldung quittieren. Dieser Fehler tritt auf, wenn die Kessel- und Abgastemperatur über einen Zeitraum von 30 Minuten kleiner als die eingestellte RL- Pumpe – EIN ist. Heizmaterialqualität und Heizmaterialmenge im Brennraum überprüfen. Anlage neu starten. [S. 3] |
| **F20** Brennerstörung | „Drehrost nicht vollständig geschlossen"; Dieser Fehler wird bei Neustart automatisch quittiert. [S. 3] (Kap. 5, S. 2 also states the Anlage is stopped with Fehler 20 when the Aschenlade counter is exceeded by 50.) |
| **F26** Pelletsvorr. kontrollieren | Diese Meldung erscheint, wenn der Behälter nach einem vollständigen Durchlauf aller Absaugpunkte nicht voll geworden ist. Abhilfe: Pelletsvorrat im Lagerraum überprüfen. Kontrolle, ob Saugturbine und Saugschlauch undicht oder verlegt sind (z.B.: Schutzgitter im Zwischenbehälter) [S. 3] |
| **F57** Phase fehlt Stockermotor | Wird nur angezeigt, wenn ein Unterstrom gemessen wird, etwa bei nicht eingestecktem Motoranschlusskabel oder defektem Motor. [S. 3] |
| **F58** Abkühlphase Stockermotor | (no Abhilfe printed) [S. 3] |
| **F59** Interne Überstrom | Stocker Protokoll Meldung [S. 3] |
| **F167** Taste defekt | Diese Fehlermeldung wird erzeugt, wenn während dem Netzeinschalten eine Taste gedrückt wird oder eine Taste klemmt. Bsp.: Bedienpult IPN 167 1. Der Fehler wird nummeriert von 1 bis 7 lt. Tastatur 1 = Dauerbetriebtaste; 2 = Uhrzeitbetriebtaste;… 7 = Handbetriebtaste [S. 3] |

> GAP: Error numbers not listed in the manual (F1, F7, F8, F10–F13, F15, F18, F21–F25, F27–F56, F60–F166) have no printed description. The manual does not say whether the list is complete.
