#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:02:57 2024

@author: sgassner
"""

# Libraries laden
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

# Pfade und URLs
url = "URL_OF_THE_WEBSITE"
state_file = "PATH_OF_STATE_FILE"
pushover_user_key = "YOUR_PUSHOVER_USER_KEY"
pushover_api_token = "YOUR_PUSHOVER_API_TOKEN"

# Funktion um Website zu scrapen
def check_blitzer():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tabelle mit Blitzern finden
    table = soup.find('table')
    rows = table.find_all('tr')

    blitzer_list = []
    for row in rows[1:]:  # Erste Zeile überspringen
        columns = row.find_all('td')
        if len(columns) >= 3:
            gemeinde = columns[0].text.strip()
            ort = columns[1].text.strip()
            strasse = columns[2].text.strip()
            blitzer_list.append(f"{gemeinde} - {ort} - {strasse}")
    
    return blitzer_list

# Funktion um letzten Stand der Tabelle zu laden
def load_blitzer_list():
    if os.path.exists(state_file):
        with open(state_file, 'r') as file:
            return json.load(file)
    return []

# Funktion um aktuellen Stand der Tabelle zu speichern
def save_blitzer_list(current_state):
    with open(state_file, 'w') as file:
        json.dump(current_state, file)

# Funktion um Mitteilung über Pushover zu senden
def send_notification(message):
    pushover_url = "https://api.pushover.net/1/messages.json"
    payload = {
        'token': pushover_api_token,
        'user': pushover_user_key,
        'message': message,
        'title': 'Achtung: Neue Blitzer!',
        'priority': 1
    }
    requests.post(pushover_url, data=payload)

# Mitteilung über Änderungen der Blitzer schicken und aktuelle Tabelle speichern
if __name__ == "__main__":
    aktuelle_blitzer = check_blitzer()
    letzte_blitzer = load_blitzer_list()
    
    neue_blitzer = list(set(aktuelle_blitzer) - set(letzte_blitzer))
    
    if neue_blitzer:
        message = f"Neue Blitzer vom {datetime.now().strftime('%Y-%m-%d')}:\n" + "\n".join(neue_blitzer)
        send_notification(message)
    
    save_blitzer_list(aktuelle_blitzer)
