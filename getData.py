import requests
import json
data = []
try:
   with open('data.json', 'r') as f:
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
           with open('data.json', 'w') as f:
               json.dump(data, f)
       else:
           print(f"Fehler bei der API-Anfrage. Statuscode: {response.status_code}")
   except requests.exceptions.RequestException as e:
       print(f"Fehler bei der Verbindung zur API: {e}")
else:
   print("Daten Vorhanden")


small_monsters = []
large_monsters = []
def sort_monster():


   for i in data:
       if i["type"] == 'small':
           small_monsters.append(i)
       elif i["type"] == "large":
           large_monsters.append(i)




   number = 1
   for i in small_monsters:
       print(f"{number}  {i['name']} es ist {i['type']}")
       number +=1


   for i in large_monsters:
       print(f"{number}  {i['name']} es ist {i['type']}")
       number +=1






sort_monster()