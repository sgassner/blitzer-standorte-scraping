# Blitzer-Warnskript

## Beschreibung

Dieses Python-Skript überprüft täglich eine spezifizierte Website auf Aktualisierungen von Blitzern und benachrichtigt Benutzer über Änderungen. Es nutzt Web Scraping, um die Informationen zu sammeln, vergleicht die aktuellen Daten mit dem zuvor gespeicherten Zustand und sendet nur dann Benachrichtigungen, wenn neue oder geänderte Einträge vorliegen. Die Benachrichtigungen werden über den Pushover-Dienst gesendet.

## Funktionen

- **Web Scraping**: Extrahiert Blitzer-Daten von einer angegebenen Website.
- **Zustandsvergleich**: Identifiziert Änderungen durch Vergleich der aktuellen Daten mit dem zuvor gespeicherten Zustand.
- **Selektive Benachrichtigungen**: Sendet Benachrichtigungen nur bei neuen oder geänderten Einträgen.
- **Tägliche Ausführung**: Kann mithilfe von Task-Scheduling-Tools wie cron auf Linux oder Task Scheduler auf Windows täglich ausgeführt werden.
- **Pushover-Integration**: Verwendet Pushover, um Echtzeit-Benachrichtigungen zu senden.

## Voraussetzungen

- Python 3.x
- Pushover-Konto und API-Schlüssel
- Python-Pakete: `requests`, `beautifulsoup4`

## Haftungsausschluss

Bitte beachten Sie, dass die Nutzung dieses Skripts zur Erkennung von Blitzern in einigen Regionen rechtlichen Beschränkungen unterliegen kann. Stellen Sie sicher, dass Sie die örtlichen Gesetze und Vorschriften einhalten.

