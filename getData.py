import requests
import json
data = []
try:
    with open('monsterFromMonsterHunterWorldAPI.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print("Fehler beim Laden der JSON-Datei:", e)

if data ==[]:
    url = 'https://mhw-db.com/monsters'
    try:
        # API-Anfrage senden und die Antwort erhalten
        response = requests.get(url)

        # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
            # JSON-Daten aus der API-Antwort extrahieren
            data = response.json()

            # Hier kannst du mit den JSON-Daten arbeiten
            with open('monsterFromMonsterHunterWorldAPI.json', 'w') as f:
                json.dump(data, f)
        else:
            print(f"Fehler bei der API-Anfrage. Statuscode: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Verbindung zur API: {e}")
else:
    print("Daten Vorhanden")

