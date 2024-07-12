# Web Scraping: Blitzer-Standorte

Das Skript identifiziert und meldet automatisch neue Blitzer-Standorte in St. Gallen (SG) und Liechtenstein (FL). Das Projekt nutzt fortgeschrittenes Web Scraping mit `BeautifulSoup` und `Selenium`, um dynamisch geladene Daten präzise zu extrahieren. Die Informationen werden in JSON-Dateien verwaltet und Benachrichtigungen über Pushover versendet.

## Funktionsweise

1. **Datenextraktion für SG**: Mit der Funktion `check_blitzer_sg()` werden die Blitzer-Daten von der offiziellen Website der Blitzerstandorte in St. Gallen abgerufen. Hierbei wird `requests` verwendet, um die HTML-Seite zu laden, und `BeautifulSoup`, um die relevanten Daten aus der HTML-Tabelle zu extrahieren.

2. **Datenextraktion für FL**: Die Funktion `check_blitzer_fl()` nutzt `Selenium`, um die Blitzer-Daten von der Website der Landespolizei Liechtenstein zu extrahieren. Da diese Seite dynamisch geladen wird, ist der Einsatz eines Headless-Browsers notwendig.

3. **Zustandsverwaltung**: Die Funktionen `load_previous_state()` und `save_current_state()` laden bzw. speichern den Zustand der Blitzer-Daten in JSON-Dateien. Dadurch kann das Skript erkennen, ob neue Blitzer-Standorte hinzugekommen sind.

4. **Benachrichtigungssystem**: Die Funktion `send_notification()` sendet Benachrichtigungen über den Pushover-Dienst, falls neue Blitzer-Standorte identifiziert wurden. 

## Komponenten

- **BeautifulSoup**: Zum Parsen und Extrahieren von Daten aus HTML.
- **Selenium**: Zum Interagieren mit dynamisch generierten Webseiten.
- **requests**: Zum Abrufen von HTML-Seiten.
- **Pushover**: Zum Senden von Push-Benachrichtigungen.

## Verwendung

- **Chromedriver**: Es muss sichergestellt werden, dass der passende Chromedriver für die verwendete Chrome-Version heruntergeladen und der Pfad im Skript korrekt gesetzt ist. Alternativ kann **webdriver-manager** verwendet werden, um den ChromeDriver automatisch zu verwalten.
- **Benachrichtigung**: Die Platzhalter `pushover_user_key` und `pushover_api_token` müssen individuell angepasst werden.
