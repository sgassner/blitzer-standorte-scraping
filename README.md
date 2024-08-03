# Web Scraping: Blitzer-Standorte

Dieses Skript wurde konzipiert, um automatisiert neue Blitzer-Standorte in St. Gallen (SG) und Liechtenstein (FL) zu identifizieren. Das Projekt nutzt fortgeschrittene Techniken des Web Scraping mittels `BeautifulSoup` und `Selenium`, um sowohl statische als auch dynamisch geladene Daten effektiv zu extrahieren. Die extrahierten Informationen werden in JSON-Dateien strukturiert verwaltet, während Benachrichtigungen zu Standortänderungen über den Dienst Pushover versendet werden. Der Zugriff auf dynamisch generierte Webseiten wird durch einen Selenium WebDriver realisiert, der innerhalb eines Docker-Containers betrieben wird.

## Funktionsweise

1. **Datenextraktion für SG**: Die Funktion `check_blitzer_sg()` dient zur Extraktion der Blitzer-Daten von der offiziellen Website der Blitzer-Standorte in St. Gallen. Die Bibliothek `requests` wird eingesetzt, um die HTML-Seite zu laden, während `BeautifulSoup` die relevanten Informationen aus den HTML-Tabellenstrukturen extrahiert.

2. **Datenextraktion für FL**: Für die dynamische Datenextraktion von der offiziellen Website der Blitzer-Standorte in Liechtenstein wird `Selenium` verwendet. Da die Seite interaktive Elemente enthält, wird ein Headless-Browser eingesetzt. Der WebDriver operiert innerhalb eines Docker-Containers und kommuniziert über einen Remote-Endpunkt mit der Anwendung.

3. **Zustandsverwaltung**: Mittels der Funktionen `load_previous_state()` und `save_current_state()` werden die aktuellen Zustände der Blitzer-Daten in JSON-Dateien gespeichert und geladen. Diese Mechanismen ermöglichen es dem Skript, Veränderungen in den Blitzer-Standorten zuverlässig zu erkennen.

4. **Push-Benachrichtigungen**: Die Funktion `send_notification()` ist dafür verantwortlich, Benachrichtigungen über den Pushover-Dienst zu senden, falls neue Blitzer-Standorte identifiziert werden.

## Komponenten

- **BeautifulSoup**: Dient zur Analyse und Extraktion von Daten aus HTML-Dokumenten.
- **Selenium**: Ermöglicht die Interaktion mit dynamisch generierten Webseiten. Der WebDriver wird in einem Docker-Container betrieben, was die Ausführung in isolierten Umgebungen unterstützt.
- **requests**: Wird verwendet, um HTML-Seiten zu laden.
- **Pushover**: Ein Dienst, der für das Senden von Push-Benachrichtigungen genutzt wird.

## Verwendung

- **Docker-Setup**: Zur lokalen Ausführung des Skripts ist es erforderlich, einen Selenium WebDriver in einem Docker-Container zu betreiben. Docker und das entsprechende Selenium Docker-Image (z.B. `selenium/standalone-chrome`) müssen auf dem System installiert und gestartet sein.
  
- **Chromedriver**: Der Zugriff auf den WebDriver erfolgt über die Remote-URL `http://localhost:4444/wd/hub`. Dies eliminiert die Notwendigkeit, einen lokalen Chromedriver manuell zu verwalten.

- **Benachrichtigung**: Die Platzhalter `YOUR_PUSHOVER_USER_KEY` und `YOUR_PUSHOVER_API_TOKEN` müssen durch gültige Pushover-Schlüssel ersetzt werden, um Benachrichtigungen zu ermöglichen.

- **Zustandsdateien**: Die JSON-Zustandsdateien `state_file_blitzer_sg.json` und `state_file_blitzer_fl.json` werden verwendet, um den aktuellen Stand der Blitzer-Standorte zu verfolgen. Der Pfad `YOUR_PATH` zu diesen Dateien sollte entsprechend der lokalen Verzeichnisstruktur angepasst werden.
