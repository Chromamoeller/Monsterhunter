from handle_data import small_monsters, large_monsters
import tkinter
import random

# Setup für die UI
root = tkinter.Tk()
root.geometry("800x800")
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


# Button zum Anzeigen von kleinen Monstern
create_small_monster = tkinter.Button(root, text="Kleines Monster", command=display_current_small_monster)
create_small_monster.pack()

# Button zum Anzeigen von großen Monstern
create_large_monster_btn = tkinter.Button(root, text="Großes Monster", command=display_current_large_monster)
create_large_monster_btn.pack()

# Zeigt den Namenstext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_name_labe = tkinter.Label(root, text=current_monster_to_fight_name_text)
current_monster_to_fight_name_labe.place(x=600, y=10)

# Zeigt den Größentext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_size_lable = tkinter.Label(root, text=current_monster_to_fight_type_text)
current_monster_to_fight_size_lable.place(x=600, y=50)

# Zeigt den Schwächetext eines aktuellen Monsters an, welches durch die beiden Buttons erstellt wurde.
current_monster_to_fight_weaknesses_lable = tkinter.Label(root, text=current_monster_to_fight_weaknesses_text)
current_monster_to_fight_weaknesses_lable.place(x=600, y=90)


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
