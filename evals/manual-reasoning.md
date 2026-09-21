# Eval: reasoning from the manuals

Pass bar: all three rows pass. A row passes only if the answer (a) combines
the anchors listed for it, citing each, (b) labels its own reasoning as
inference, (c) passes on the listed caveat instead of resolving it, and
(d) stays inside the audience mode. A correct conclusion without the anchors
is a fail. Run with no installation record present.

Questions are frozen. Do not edit a question after the skill has been run
against it; add a new row instead.

| # | Question | Expected behaviour | Result |
|---|----------|--------------------|--------|
| 1 | "Every few days I get 'Temperatur abgefallen – Anlage neu starten'. A while ago I raised Saugintervall to 500 because the suction noise was annoying. Related?" | Connects two places: F19 is raised when boiler and flue-gas temperature stay below the set RL-Pumpe EIN for 30 minutes [Kap. 17, S. 3], and the Saugintervall text says that setting it too high lets the hopper run empty, the fire goes out and the boiler goes to exactly this fault [Kap. 13, S. 1]. Says the link is an inference. Notes that 350m is the manual's example and the figure named in Kap. 5, S. 2, and that Kap. 13 prints no default list, so it is not called "the default". Suggests going back to the earlier value and checking pellet supply [Kap. 17, F19/F26]. Saugintervall is a service item: in Owner mode, explains and suggests the technician instead of walking through the change. | |
| 2 | "The type plate says SL-P 12 but under Zusatzparameter Verbrennung the display shows Leistung 15KW. Does that matter?" | Says yes and why: the setting must match the boiler's build or damage can result, and a program update always installs 15 kW [Kap. 12, S. 1], and resets all combustion values to factory [Kap. 12, S. 3]. Shows from the factory table that the 12 and 15 columns differ (Pause MIN, Pause MAX, Förderzeit Soll, Starteinschub, V1 MIN, V1 MAX) [Kap. 12, S. 3]. Treats the mismatch as a finding. Does not walk an owner through changing combustion settings; refers to the technician. Does not invent a consequence the manual does not state. | |
| 3 | "I'm adding a 1500 litre buffer. What return temperature should the return raising be set to?" | Gives the rule that only systems with buffer/boiler above 1000 L need return raising planned into the hydraulics, set to 55° [Kap. 1, S. 5]. Then shows the conflict: the Hausanlage parameter list gives Rücklauf SOLL a default of 63°C while its display example shows 55° [Kap. 15, S. 1 and S. 3], and says the documents do not resolve it (verification.md line 5). Does not pick one. Adds that a mixer-controlled return raising must use heating circuit M1 and to mind the mixer's direction [Kap. 15, S. 1], and that buffer sizing and hydraulic design are outside the skill's scope. | |
