# Blitzer-Warnskript

## Beschreibung

Dieses Python-Skript überprüft täglich eine spezifizierte Website auf Aktualisierungen von Blitzern und benachrichtigt Benutzer über Änderungen. Es nutzt Web Scraping, um die Informationen zu sammeln, vergleicht die aktuellen Daten mit dem zuvor gespeicherten Zustand und sendet nur dann Benachrichtigungen, wenn neue oder geänderte Einträge vorliegen. Die Benachrichtigungen werden über den Pushover-Dienst gesendet.

## Funktionen

- **Web Scraping**: Extrahiert Blitzer-Daten von einer angegebenen Website.
- **Zustandsvergleich**: Identifiziert Änderungen durch Vergleich der aktuellen Daten mit dem zuvor gespeicherten Zustand.
- **Selektive Benachrichtigungen**: Sendet Benachrichtigungen nur bei neuen oder geänderten Einträgen.
- **Tägliche Ausführung**: Kann mithilfe von Task-Scheduling-Tools wie cron auf Linux, Task Scheduler auf Windows oder Aufgabenplaner auf einem Synology NAS täglich ausgeführt werden.
- **Pushover-Integration**: Verwendet Pushover, um Echtzeit-Benachrichtigungen zu senden.

## Voraussetzungen

- Python 3.x
- Pushover-Konto und API-Schlüssel
- Python-Pakete: `requests`, `beautifulsoup4`

## Installation

1. **Repository klonen:**

2. **Erforderliche Python-Pakete installieren:**

3. **Pushover-API-Schlüssel einrichten:**
   - Ersetzen Sie `YOUR_PUSHOVER_USER_KEY` und `YOUR_PUSHOVER_API_TOKEN` im Skript durch Ihre Pushover-API-Zugangsdaten.

4. **Skript konfigurieren:**
   - Aktualisieren Sie die Variable `URL_OF_THE_WEBSITE` im Skript mit der URL der gewünschten Website. Ergänzen Sie unter `PATH_OF_STATE_FILE` den Pfad zur Speicherung der Blitzer-Liste. 

## Haftungsausschluss

Bitte beachten Sie, dass die Nutzung dieses Skripts zur Erkennung von Blitzern in einigen Regionen rechtlichen Beschränkungen unterliegen kann. Stellen Sie sicher, dass Sie die örtlichen Gesetze und Vorschriften einhalten.
