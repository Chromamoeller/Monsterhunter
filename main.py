from handle_data import small_monsters, large_monsters
import tkinter
from tkinter import font
import random
from player import Player

player1 = Player('', 150, 150, 'Sword and Shield', [])

# Setup für die UI
window_x = 900
window_y = 900
root = tkinter.Tk()
root.geometry(f"{window_x}x{window_y}")
canvas = tkinter.Canvas(root, width=900, height=450, bg='lightgray')
canvas.pack()
stats_font = font.Font(family="Helvetica", size=16, weight="bold", slant="italic")
monster_name_font = font.Font(family="Helvetica", size=20, weight="bold", slant="italic")
small_monster_text = ""
large_monster_text = ""
current_monster_to_fight_name_text = ""
current_monster_to_fight_type_text = ""
current_monster_to_fight_weaknesses_text = ""


# Wird durch Button "kleines Monster" aufgerufen. Displayed random ein monster aus der Liste von kleinen Monster
def display_current_small_monster():
    global current_monster_to_fight_name_labe
    global current_monster_to_fight_size_lable
    global current_monster_to_fight_weaknesses_lable
    random_number = random.randint(0, len(small_monsters) - 1)
    current_monster_to_fight_name_labe.config(text=small_monsters[random_number]["name"])
    current_monster_to_fight_size_lable.config(text=small_monsters[random_number]["type"])
    current_monster_to_fight_weaknesses_lable.config(text=small_monsters[random_number]['weaknesses'][0]['element'])
    show_weakness(small_monsters[random_number])
    generate_hp_for_monster(small_monsters[random_number])


# Wird durch Button "großes Monster" aufgerufen. Displayed random ein Monster aus der Liste von der großen Monster
def display_current_large_monster():
    global current_monster_to_fight_name_labe
    global current_monster_to_fight_size_lable
    global current_monster_to_fight_weaknesses_lable
    random_number = random.randint(0, len(large_monsters) - 1)
    current_monster_to_fight_name_labe.config(text=large_monsters[random_number]["name"])
    current_monster_to_fight_size_lable.config(text=large_monsters[random_number]["type"])
    current_monster_to_fight_weaknesses_lable.config(text=large_monsters[random_number]["weaknesses"][0]['element'])
    show_weakness(large_monsters[random_number])
    generate_hp_for_monster(large_monsters[random_number])


# UI
# player UI

# Spieler maximale Anzeige die schraffiert angezeigt wird hinter der eigentlichen Anzeige als indikator wie viel leben
# einem Spieler fehlt
max_player_health_bar = canvas.create_rectangle(10, 10, player1.max_hp, 30, fill='red', outline='black',
                                                stipple="gray50")
# Spieler tatsächliche Hp dargestellt in Rot
player_health_bar = canvas.create_rectangle(10, 10, player1.current_hp, 30, fill='red', outline='black')

# Buttons und so Zeug

# Ein Kontainer der wie eine ordner Struktur agieren soll
main_buttons_frame = tkinter.Frame(root, borderwidth=2, relief="groove", width=200, height=450)
main_buttons_frame.place(x=0, y=451)

# Ein Kontainer für die stats eines Monsters
status_frame = tkinter.Frame(root, borderwidth=2, relief="groove", width=200, height=450)
status_frame.place(x=700, y=451)

# Button zum Anzeigen von kleinen Monstern
create_small_monster = tkinter.Button(main_buttons_frame, text="Kleines Monster", command=display_current_small_monster,
                                      width=20,
                                      height=2)
create_small_monster.place(x=0, y=0)

# Button zum Anzeigen von großen Monstern
create_large_monster_btn = tkinter.Button(main_buttons_frame, text="Großes Monster",
                                          command=display_current_large_monster, width=20,
                                          height=2)
create_large_monster_btn.place(x=0, y=50)

# Zeigt den Namenstext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_name_labe = tkinter.Label(root, text=current_monster_to_fight_name_text,
                                                   font=monster_name_font)
current_monster_to_fight_name_labe.place(x=window_x/2-50, y=455)

# Zeigt den Größentext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_size_lable = tkinter.Label(status_frame, text=current_monster_to_fight_type_text,
                                                    font=stats_font)
current_monster_to_fight_size_lable.place(x=0, y=0)

# Zeigt den Schwächetext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_weaknesses_lable = tkinter.Label(status_frame, text=current_monster_to_fight_weaknesses_text,
                                                          font=stats_font)
current_monster_to_fight_weaknesses_lable.place(x=0, y=50)


# Findet für jedes monster seine Schwäche und wie groß die Schwäche ist und schreibt sie in die Console
def show_weakness(monster):
    list_of_weaknesses_and_stars = []
    for weakness in monster['weaknesses']:
        # print(weakness['element'], weakness['stars'])
        list_of_weaknesses_and_stars.append(weakness['element'])
        list_of_weaknesses_and_stars.append(weakness['stars'])
    print(monster['name'], "Schwäche", list_of_weaknesses_and_stars)


# Erstellt für jedes Monster eigene Hp-Werte abhängig von größe des Monsters
def generate_hp_for_monster(monster):
    if monster['type'] == 'small':
        print("Es bekommt 100 Hp")
    elif monster['type'] == 'large':
        print("Es bekommt 300 Hp")


root.mainloop()
