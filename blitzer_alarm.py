#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:02:57 2024

@author: sgassner
"""

# Libraries laden
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
import json
import os

# Pfade und URLs
url_blitzer_sg = "https://www.sg.ch/sicherheit/kantonspolizei/verkehr/radar.html"
url_blitzer_fl = "https://www.landespolizei.li/radar"
state_file_blitzer_sg = "PATH"
state_file_blitzer_fl = "PATH"
pushover_user_key = "pushover_user_key"
pushover_api_token = "pushover_api_token"

# Funktion zum Abrufen der Blitzer-Daten SG
def check_blitzer_sg():
    response = requests.get(url_blitzer_sg)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Blitzer-Daten extrahieren
    table = soup.find('table')
    rows = table.find_all('tr')

    blitzer_list_sg = []
    for row in rows[1:]:  # Header-Zeile überspringen
        columns = row.find_all('td')
        if len(columns) >= 3:
            ort = columns[1].text.strip()
            strasse = columns[2].text.strip()
            blitzer_list_sg.append(f"{ort} - {strasse}".strip())
    
    return blitzer_list_sg

# Funktion zum Abrufen der Blitzer-Daten FL mit Selenium
def check_blitzer_fl():
    options = Options()
    options.headless = True  # Führen Sie den Browser im Headless-Modus aus
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # Docker-Container URL
        options=options
    )
    
    driver.get(url_blitzer_fl)
    
    blitzer_list_fl = []
    radar_sections = driver.find_elements(By.CLASS_NAME, 'radar-list__item')
    for radar in radar_sections:
        radar_title_elem = radar.find_element(By.CLASS_NAME, 'radar-list__item-title')
        radar_address_elem = radar.find_element(By.CLASS_NAME, 'radar-list__item-address')
        radar_title = radar_title_elem.text.strip()
        radar_address = radar_address_elem.text.strip()
        blitzer_list_fl.append(f"{radar_title} - {radar_address}".strip())
    
    driver.quit()
    
    # Sortiere die Liste nach der Radarnummer in aufsteigender Reihenfolge
    blitzer_list_fl.sort(key=lambda entry: int(entry.split()[1]))
    
    return blitzer_list_fl

# Funktion zum Laden des vorherigen Zustands
def load_previous_state(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Funktion zum Speichern des aktuellen Zustands
def save_current_state(current_state, file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(current_state, file, ensure_ascii=False, indent=4)

# Funktion zum Senden von Benachrichtigungen
def send_notification(message, title="Achtung Blitzer!"):
    pushover_url = "https://api.pushover.net/1/messages.json"
    payload = {
        'token': pushover_api_token,
        'user': pushover_user_key,
        'message': message,
        'title': title,
        'priority': 1
    }
    response = requests.post(pushover_url, data=payload)
    print(f"Notification sent with response: {response.status_code}")

# Hauptlogik
if __name__ == "__main__":
    # Blitzer-Daten Kanton St. Gallen überprüfen
    current_blitzer_sg = check_blitzer_sg()
    previous_blitzer_sg = load_previous_state(state_file_blitzer_sg)
    
    # Berechnung der Unterschiede
    new_blitzer_sg = [entry for entry in current_blitzer_sg if entry not in previous_blitzer_sg]
    
    if new_blitzer_sg:
        message = f"Neue Blitzer-Standorte (SG) per {datetime.now().strftime('%Y-%m-%d')}:\n" + "\n".join(new_blitzer_sg)
        send_notification(message, title="Neue Blitzer (SG)")
        print("SG notification sent")
    else:
        print("Keine neuen Blitzer in SG gefunden.")

    save_current_state(current_blitzer_sg, state_file_blitzer_sg)
    
    # Blitzer-Daten Liechtenstein überprüfen
    current_blitzer_fl = check_blitzer_fl()
    previous_blitzer_fl = load_previous_state(state_file_blitzer_fl)
    
    # Berechnung der Unterschiede
    new_blitzer_fl = [entry for entry in current_blitzer_fl if entry not in previous_blitzer_fl]
    
    if new_blitzer_fl:
        message = f"Neue Blitzer-Standorte (FL) per {datetime.now().strftime('%Y-%m-%d')}:\n" + "\n".join(new_blitzer_fl)
        send_notification(message, title="Neue Blitzer (FL)")
        print("FL notification sent")
    else:
        print("Keine neuen Blitzer in FL gefunden.")
        
    save_current_state(current_blitzer_fl, state_file_blitzer_fl)
