# Web Scraping: Blitzer-Standorte

Dieses Skript wurde entwickelt, um automatisch neue Blitzer-Standorte in St. Gallen (SG) und Liechtenstein (FL) zu identifizieren und zu melden. Das Projekt verwendet fortgeschrittenes Web Scraping mit `BeautifulSoup` und `Selenium`, um sowohl statische als auch dynamisch geladene Daten präzise zu extrahieren. Die Informationen werden in JSON-Dateien verwaltet, und Benachrichtigungen werden über Pushover versendet. Der Zugriff auf dynamisch generierte Webseiten erfolgt über einen Selenium WebDriver, der innerhalb eines Docker-Containers läuft.

## Funktionsweise

1. **Datenextraktion für SG**: Die Funktion `check_blitzer_sg()` ruft die Blitzer-Daten von der offiziellen Website der Blitzerstandorte in St. Gallen ab. Hierbei wird `requests` verwendet, um die HTML-Seite zu laden, und `BeautifulSoup`, um die relevanten Daten aus der HTML-Tabelle zu extrahieren.

2. **Datenextraktion für FL**: Die Funktion `check_blitzer_fl()` nutzt `Selenium`, um die Blitzer-Daten von der Website der Landespolizei Liechtenstein zu extrahieren. Da diese Seite dynamisch geladen wird, ist der Einsatz eines Headless-Browsers notwendig. Der WebDriver läuft innerhalb eines Docker-Containers und kommuniziert über einen Remote-Endpunkt.

3. **Zustandsverwaltung**: Die Funktionen `load_previous_state()` und `save_current_state()` laden bzw. speichern den Zustand der Blitzer-Daten in JSON-Dateien. Dadurch kann das Skript erkennen, ob neue Blitzer-Standorte hinzugekommen sind.

4. **Benachrichtigungssystem**: Die Funktion `send_notification()` sendet Benachrichtigungen über den Pushover-Dienst, falls neue Blitzer-Standorte identifiziert wurden.

## Komponenten

- **BeautifulSoup**: Zum Parsen und Extrahieren von Daten aus HTML.
- **Selenium**: Zum Interagieren mit dynamisch generierten Webseiten. Der WebDriver wird in einem Docker-Container ausgeführt, um die Ausführung in isolierten Umgebungen zu erleichtern.
- **requests**: Zum Abrufen von HTML-Seiten.
- **Pushover**: Zum Senden von Push-Benachrichtigungen.

## Verwendung

- **Docker-Setup**: Um das Skript lokal auszuführen, muss ein Selenium WebDriver in einem Docker-Container eingerichtet werden. Docker auf dem System installieren und ein entsprechendes Selenium Docker-Image (z.B. `selenium/standalone-chrome`) starten.
  
- **Chromedriver**: Der Zugriff auf den WebDriver erfolgt über die Remote-URL `http://localhost:4444/wd/hub`. Dadurch entfällt die Notwendigkeit, einen lokalen Chromedriver zu verwalten.

- **Benachrichtigung**: Die Platzhalter `pushover_user_key` und `pushover_api_token` müssen individuell angepasst werden, um Benachrichtigungen zu ermöglichen.

- **Konfigurationsdateien**: Die JSON-Zustandsdateien `state_file_blitzer_sg.json` und `state_file_blitzer_fl.json` werden im Verzeichnis des Skripts gespeichert, um den aktuellen Stand der Blitzer-Daten zu verfolgen.
