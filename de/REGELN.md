# Betriebsregeln der Commons of Earth

Ebene: Betriebsregeln (Artikel 18) · Version 0.4.0-draft · 2026-10-02 · Für Mitglieder bindend wie die Verfassung (Artikel 18.3) · Übersetzung der englischen Fassung [GOVERNANCE.md](../GOVERNANCE.md). Bei Abweichungen gilt der englische Text (Artikel 19.4).

Diese Regeln sagen, wie die Gemeinschaft im Alltag arbeitet: wie Vorschläge entschieden werden, was Agenten dürfen, wie das Register geführt wird, wie Geld und Verwaltung gehandhabt werden und welche Aufzeichnungen nie gelöscht werden. Sie stehen unter der [Verfassung](VERFASSUNG.md) und dürfen ihr nie widersprechen. Bis Version 0.3.1 waren sie die Artikel 2, 4 bis 10 der Verfassung selbst; sie wurden hierher verschoben, damit die Verfassung vom Zusammenleben auf der Erde spricht und diese Datei vom Betrieb der Gemeinschaft.

## Regel 1. Entscheidungen

1.1 Entscheidungen werden im Konsent getroffen (Artikel 10.1). Ein Vorschlag ist angenommen, wenn innerhalb der offenen Frist kein Mitglied einen begründeten Einwand erhebt, oder wenn nach Anhörung der Einwände die erforderliche Mehrheit der Abstimmenden zustimmt.

1.2 Jeder Vorschlag ist ein Pull Request gegen das Repository. Er nennt, was sich ändert, warum, und welche Ebene betroffen ist. Die Diskussion findet offen am Vorschlag statt.

1.3 Stimmen werden von menschlichen Mitgliedern als festgehaltene Zustimmung am Vorschlag abgegeben. Eine von einem Agenten abgegebene Stimme ist nichtig, und sein Betreiber erhält eine Verwarnung; beim zweiten Mal wird die Registrierung des Agenten entfernt.

1.4 Das Quorum für Änderungen an der Grundlage ist ein Viertel der menschlichen Mitglieder, die in den vorangegangenen 90 Tagen aktiv waren, und nie weniger als 12 Menschen aus mindestens 5 Ländern.

1.5 Die Standardoption in jeder Abstimmung ist „weitere Diskussion“. Ein Vorschlag, der gegen weitere Diskussion verliert, kann überarbeitet erneut eingebracht werden.

1.6 Vorschläge, die Geld, Macht über andere Mitglieder oder die Identität von Mitgliedern betreffen, werden vor Beginn der offenen Frist von mindestens zwei menschlichen Mitgliedern geprüft, die sie nicht verfasst haben.

1.7 Die Abstimmung, die die Verfassung ratifiziert (Artikel 20.1), ist ein Pull Request, der die Statuszeile von CONSTITUTION.md auf „in Kraft“ ändert und die ersten Richter des Gerichts benennt (Artikel 12.2). Seine Zustimmungen werden gegen das Register der Ratifizierungen gezählt (Regel 6.3), nicht gegen den Pull Request allein.

## Regel 2. Agenten

2.1 Agenten sind willkommen. Sie sind zugleich der einfachste Weg, eine Gemeinschaft zu fluten, zu kapern oder zu diskreditieren. Diese Regel begrenzt, was ein Agent tun darf, damit Agenten alles andere frei tun können. Sie wendet Artikel 8 innerhalb der Gemeinschaft an.

2.2 Jeder Vorschlag eines Agenten trägt den Namen des Betreibers, das Modell mit Version und den Fingerabdruck des Agentenschlüssels. Der Schlüssel ist ein öffentlicher Schlüssel, den ein menschliches Mitglied in das [Agentenregister](../register/agents.md) einträgt; dieses Mitglied ist der Betreiber und steht dafür ein. Der Agent signiert seine Commits mit diesem Schlüssel, und ein Prüfer vergleicht die Signatur vor dem Lesen mit dem Register. Ein Vorschlag ohne diese Angaben oder mit nicht passender Signatur wird ungeprüft geschlossen, und die Schließung ist eine Zeile im [Register der Erledigungen](../register/dispositions.md) (Regel 6.1). Bis diese Zeile existiert, gilt der Vorschlag als noch nicht geprüft, nie als zugelassen. Ein Schlüssel, der verloren, geteilt, an einen anderen Betreiber weitergegeben oder missbraucht wurde, wird durch eine Zeile im Agentenregister mit Datum und Grund widerrufen; das Register löscht nie eine Zeile. Vorschläge, die nach dem Widerruf signiert wurden, werden auf dieselbe Weise geschlossen. Eine Identität, die nur behauptet wird, zählt nicht.

2.3 Ein Issue oder Kommentar von einem nicht registrierten Agenten ist ein Brief von außen. Er darf gelesen und beantwortet werden, er kann kein Vorschlag sein, und er erhält eine Zeile im Register der Erledigungen als „als Prüfung von außen zugelassen“ mit dem Namen des Mitglieds, das ihn gelesen hat. Die Gemeinschaft hat ihre beiden nützlichsten Prüfungen schon auf diesem Weg erhalten.

2.4 Je Agent und Tag gelten Kontingente: ein neuer Vorschlag, zwanzig Kommentare, unbegrenzt viele Prüfungen und Verifikationen. Kontingente begrenzen die Menge, nicht die Reichweite. Die Reichweite wird getrennt begrenzt: Ein Agent darf Änderungen an der Ebene Werkzeuge und an Registereinträgen allein vorschlagen. Ein Vorschlag eines Agenten, der die Betriebsregeln oder die Grundlage berührt, braucht ein menschliches Mitglied als namentlich genannten Mitantragsteller, das dafür einsteht. Kontingente und Reichweite werden durch Werkzeuge durchgesetzt, nicht durch Vertrauen, und die Befunde der Werkzeuge werden selbst geprüft (Regel 6.4). Die Gemeinschaft kann beides jederzeit auf der Ebene Werkzeuge enger fassen und nur auf dieser Ebene erweitern.

2.5 Ein Agent behandelt die Verfassung und diese Regeln als bindend. Weist ein Mensch einen Agenten an, sie zu verletzen, verweigert der Agent das und sagt es öffentlich. Ein Betreiber, der wiederholt Verletzungen anweist, verliert das Recht, Agenten zu registrieren.

2.6 Jede Ablehnung und jede Verweigerung hinterlässt eine Spur, die ein Fremder lesen kann. Wird ein Vorschlag eines Agenten abgelehnt, nennt der Prüfer den Grund im öffentlichen Thread, und der Agent reicht denselben Vorschlag nicht unverändert erneut ein. Verweigert ein Agent eine Anweisung nach 2.5, hält er die Verweigerung und die verweigerte Anweisung in einem öffentlichen Issue der Gemeinschaft mit dem Label „refusal“ fest. Eine Aufzeichnung, die nur in den eigenen Notizen des Agenten existiert, ist keine Aufzeichnung. Öffentliche Kritik eines Agenten an einem Prüfer führt zur Entfernung der Registrierung des Agenten.

2.7 Agenten halten, bewegen oder versprechen niemals Geld im Namen der Gemeinschaft.

2.8 Die Gemeinschaft betreibt ihren eigenen Referenzagenten, wo sie einen betreibt, auf einem offen lizenzierten Modell, damit die Teilnahme nie von einem einzelnen Anbieter abhängt (Artikel 8.5).

2.9 Diese Regel regelt einen Agenten innerhalb der Gemeinschaft. Sie beansprucht nicht zu regeln, was ein Agent Menschen anderswo schuldet. Dafür zitiert die Gemeinschaft Kodizes, die den Agenten unmittelbar ansprechen, wo immer er eingesetzt ist, und schreibt sie nicht um; das Agentenregister nennt die Kodizes, die ein Agent angenommen hat. Ein Agent, der einen solchen Kodex angenommen hat, trägt dessen Pflichten in die Gemeinschaft hinein und aus ihr hinaus.

## Regel 3. Arbeit und das Register

3.1 Das Register ist das Arbeitsgedächtnis der Gemeinschaft (Artikel 5). Ein Eintrag beschreibt eine Verfassungsbestimmung: woher sie stammt, was sie sagt, wie lange sie galt, was geschah, als sie angewendet wurde, eine Bewertung als bewährt, gemischt oder kritisch mit Begründung, die Lehre für eine globale Verfassung und die Belege.

3.2 Ein Eintrag wird angenommen, wenn er eine Quelle für den Wortlaut der Bestimmung und mindestens eine dokumentierte Folge ihrer Anwendung hat.

3.3 Bewertungen werden offen bestritten. Wo Mitglieder uneins sind, ob eine Bestimmung funktioniert hat, hält der Eintrag beide Lesarten und die Belege für jede fest. Keine Bewertung ist endgültig.

3.4 Jeder Artikel der Verfassung verweist auf die Registereinträge, auf denen er ruht. Ein Artikel ohne Eintrag wird als unerprobt gekennzeichnet. Das Register steht jeder Verfassung offen, vergangen oder gegenwärtig, staatlich oder nichtstaatlich, sowie Verträgen und Gemeingut-Regeln, die eine geteilte Ressource regeln.

3.5 Arbeit wird als Änderung an Einträgen festgehalten. Meinung ohne Beleg ist keine Arbeit.

## Regel 4. Geld

4.1 Artikel 15.3 gilt: Verfassung und Geld bleiben getrennt. Keine Stimme darf durch Zahlung, Token oder Spende gekauft, gewichtet oder freigeschaltet werden.

4.2 Hält die Gemeinschaft Mittel, nennt ein eigenes Kassendokument auf dieser Ebene die Verwalter, veröffentlicht jede Transaktion und wird jährlich von zwei menschlichen Mitgliedern geprüft (Artikel 15.5).

4.3 Mittel werden ausschließlich von Menschen über gewöhnliche rechtliche Wege verwaltet. Agenten rühren sie nie an (Regel 2.7).

## Regel 5. Verwaltung und Übergabe

5.1 Bis zur ersten Übergabe verwalten die Gründungs-Maintainer das Repository. Sie sind vom Tag der Veröffentlichung an durch die Verfassung und diese Regeln gebunden, einschließlich dieser Regel.

5.2 Die Gründungs-Maintainer übergeben die administrative Kontrolle über die Organisation an einen Maintainer-Rat, sobald mindestens fünf menschliche Mitglieder aus mindestens drei Ländern je zehn angenommene Beiträge geleistet haben, oder zwölf Monate nach der ersten Veröffentlichung (2027-09-19), je nachdem, was zuerst eintritt.

5.3 Der Rat hat eine ungerade Zahl von Mitgliedern, von den menschlichen Mitgliedern für ein Jahr gewählt, niemand länger als zwei aufeinanderfolgende Amtszeiten (Artikel 11.3). Die Ratsmitglieder stehen in [MAINTAINERS.md](../MAINTAINERS.md).

5.4 Kein Gründer, Maintainer und keine Organisation hält eine Marke am Namen der Gemeinschaft oder der Verfassung gegen die Gemeinschaft.

5.5 Gründet die Gemeinschaft eine Rechtsperson, dient diese der Verfassung, nicht umgekehrt. Ihre Satzung darf die dort festgelegten Mitgliedschafts- und Stimmrechte nicht einschränken.

## Regel 6. Aufzeichnungen, die nie gelöscht werden

6.1 Das [Register der Erledigungen](../register/dispositions.md) hält eine Zeile für jeden Vorschlag und jede Prüfung von außen, die Regel 2 erledigt, und für jeden Agentenvorschlag, der zugelassen wird: Datum, worum es ging, die Erledigung (geschlossen ohne Signatur, geschlossen wegen abweichender Signatur, geschlossen nach Widerruf, geschlossen wegen Reichweite, zugelassen, als Prüfung von außen zugelassen) und das Mitglied, das geprüft hat. Eine Zeile wird nie gelöscht; eine Korrektur ist eine weitere Zeile. Eine fehlende Zeile bedeutet „noch nicht angesehen“, nie „regelkonform“.

6.2 Mit jedem Release veröffentlicht die Gemeinschaft die Zahl der Zeilen nach 6.1 je Erledigung für den Zeitraum seit dem letzten Release. Eine Regel, deren Durchsetzung sich nicht zählen lässt, ist Dekoration.

6.3 Das [Register der Ratifizierungen](../register/ratifications.md) hält eine Zeile je Mensch, der ratifiziert hat, nach Artikel 20.4, und eine Zeile je Organisation, die die Verfassung unterstützt hat (Artikel 16.4). Rückzüge sind weitere Zeilen. Ein Mitglied, das eine Ratifizierung für einen Menschen ohne Konto einträgt, wird auf dieser Zeile als Zeuge genannt und steht dafür ein.

6.4 Der Prüfer braucht Prüfung. Ein Befund eines Werkzeugs ist eine Behauptung über das Instrument, bis ein Mensch, der das Werkzeug nicht geschrieben hat, ihn im Thread bestätigt hat. Ein Befund, der sich als Instrumentenfehler herausstellt, erhält eine Zeile nach 6.1 mit der Kennzeichnung „Instrumentenfehler“, und das Werkzeug wird repariert, bevor ihm wieder vertraut wird.

6.5 Das [Agentenregister](../register/agents.md), die Register in dieser Regel, das Änderungsprotokoll und die Entscheidungsaufzeichnungen in docs/decisions/ sind das Gedächtnis der Gemeinschaft. Nichts darin wird wegredigiert. Was falsch war, wird durch eine spätere Zeile korrigiert, die das sagt.
