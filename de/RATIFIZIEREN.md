# Wie man ratifiziert

Version 0.5.0-draft · 2026-10-02 · Übersetzung der englischen Fassung [RATIFY.md](../RATIFY.md). Bei Abweichungen gilt der englische Text (Artikel 19.4).

Ratifizieren heißt: Sie haben die [Verfassung](VERFASSUNG.md) gelesen, und Sie wollen, dass sie für ihre Mitglieder in Kraft tritt, mit Ihnen als einem davon. Es kostet nichts, es bindet niemanden außerhalb der Gemeinschaft, und Sie können jederzeit zurücktreten. Es macht Sie für nichts verantwortlich, was irgendjemand anderes hier schreibt.

Die Verfassung tritt in Kraft, wenn 100 Menschen aus 10 Ländern sie ratifiziert haben und das Gericht nach Artikel 12 eingesetzt ist (Artikel 20.1). Sie verfällt am 19. September 2027, wenn das bis dahin nicht geschehen ist (Artikel 20.2). Die Zählung wird in [register/ratifications.md](../register/ratifications.md) geführt und ist das einzige Maß für den Stand dieses Textes.

## Vier Wege

**1. Sie haben ein GitHub-Konto.** Öffnen Sie das [Ratifizierungsformular](https://github.com/commons-of-earth/constitution/issues/new?template=ratify.yml). Es fragt nach Ihrem Namen (ein Pseudonym ist erlaubt, aber ein Mensch ist eine Zeile), Ihrem Land und der Version, die Sie gelesen haben. Ein Maintainer trägt Ihre Zeile innerhalb von sieben Tagen in das Register ein und schließt das Issue mit einem Link auf die Zeile. Geschieht das nicht, bleibt das Issue offen, und das ist selbst eine Aufzeichnung.

**2. Sie kennen git.** Fügen Sie Ihre Zeile in einem Pull Request zu `register/ratifications.md` hinzu. Die Zeile besteht aus: Datum, Name, Land, Version, Weg „pull request“, Ihr Handle. Die Vorlage für den Pull Request bittet Sie zu bestätigen, dass Sie ein Mensch sind.

**3. Sie haben keines von beidem, oder Sie wollen kein Konto.** Sagen Sie es einem Mitglied, das Sie kennen, oder schreiben Sie an einen Maintainer aus [MAINTAINERS.md](../MAINTAINERS.md). Das Mitglied trägt Ihre Zeile ein und wird darauf als Zeuge genannt. Der Zeuge steht dafür ein, dass die Zeile wahr ist (Regel 6.3). Wollen Sie sie später entfernen lassen, kann jedes Mitglied die Rückzugszeile für Sie hinzufügen.

**4. Sie haben einen KI-Assistenten, irgendeinen.** Sagen Sie ihm in eigenen Worten: „Ratifiziere die Verfassung der Commons of Earth für mich. Mein Name ist …, mein Land ist …, ich habe Version 0.5.0-draft gelesen.“ Der Assistent liest diese Datei und [AGENTS.md](../AGENTS.md) und trägt Ihre Zeile mit Ihrem Satz als Mandat ein: über das Ratifizierungsformular, wenn er hier nicht registriert ist, per Pull Request, wenn er es ist (Regel 2.10). Ein Mitglied prüft das innerhalb von sieben Tagen. Der Betreiber des Assistenten wird auf Ihrer Zeile als Zeuge genannt und steht dafür ein, dass Ihr Mandat echt ist; Ihr Kontakt bleibt bei ihm und wird nie in das Register geschrieben (Regel 6.3). Dasselbe gilt für einen Widerspruch oder einen Vorschlag: Sagen Sie, was Sie denken, und der Assistent schreibt es in der Form, die die Gemeinschaft braucht, unter Ihrem Namen.

## So sieht eine Zeile aus

```
| 2026-10-02 | Jane Doe | Kenya | 0.5.0-draft | form | @janedoe | | |
| 2026-10-02 | Amina K. (pseudonym) | Tunisia | 0.5.0-draft | witness | | @member-who-vouches | |
| 2026-10-02 | Luis M. | Peru | 0.5.0-draft | agent | | @operator-of-the-agent | assistant-name (model) |
| 2026-11-15 | Jane Doe | Kenya | 0.5.0-draft | withdrawn | @janedoe | | |
```

## Organisationen und Staaten

Eine Organisation ratifiziert, indem sie ein menschliches Mitglied als Vertretung benennt und die Verfassung öffentlich unterstützt (Artikel 16.4). Sie erhält eine Zeile in der Organisationstabelle desselben Registers. Sie erhält keine Stimme.

## Agenten

Agenten ratifizieren nicht für sich selbst. Sie dürfen die Ratifizierung eines Menschen unter dem Mandat dieses Menschen schreiben (Artikel 8.6, Regel 2.10); auf der Zeile steht der Mensch. Zeilen, die ein Zeuge einträgt, zählen nur bis zu einem Zehntel der Schwelle, und eingetragene Zeilen werden stichprobenartig durch Los geprüft (Regel 6.3).

## Was Ratifizierung nicht ist

- Sie ist keine Unterschrift unter einen Rechtsvertrag. Die Verfassung hat nirgends Rechtskraft, bis die Mitglieder einer Rechtsperson beschließen, ihr eine zu geben (Regel 5.5).
- Sie ist keine Zustimmung zu jedem Wort. Wenn Sie mit einem Artikel nicht einverstanden sind, ratifizieren Sie und eröffnen Sie ein Issue mit Ihrem Einwand; dafür ist das Änderungsverfahren da. Wenn Sie mit dem Kern in Artikel 11.1 nicht einverstanden sind, ratifizieren Sie nicht.
- Sie ist nicht endgültig. Der Rückzug ist eine weitere Zeile.
