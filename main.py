from getData import small_monsters, large_monsters
import tkinter
import random


root = tkinter.Tk()
root.geometry("800x800")
small_monster_text = ""
large_monster_text = ""
current_monster_to_fight_name_text = ""
current_monster_to_fight_type_text = ""
current_monster_to_fight_weaknesses_text = ""




def display_current_small_monster():
   global current_monster_to_fight_name_labe
   global current_monster_to_fight_type_lable
   global current_monster_to_fight_weaknesses_lable
   randomNumber = random.randint(0, 15)
   current_monster_to_fight_name_labe.config(text=small_monsters[randomNumber]["name"])
   current_monster_to_fight_type_lable.config(text=small_monsters[randomNumber]["type"])
   current_monster_to_fight_weaknesses_lable.config(text=small_monsters[randomNumber]['weaknesses'][0]['element'])


def display_current_large_monster():
   global current_monster_to_fight_name_labe
   global current_monster_to_fight_type_lable
   global current_monster_to_fight_weaknesses_lable
   randomNumber = random.randint(0, 41)
   current_monster_to_fight_name_labe.config(text=large_monsters[randomNumber]["name"])
   current_monster_to_fight_type_lable.config(text=large_monsters[randomNumber]["type"])
   current_monster_to_fight_weaknesses_lable.config(text=large_monsters[randomNumber]["weaknesses"][0]['element'])


create_small_monster = tkinter.Button(root, text="Kleines Monster", command=display_current_small_monster)
create_small_monster.pack()


create_large_monster_btn = tkinter.Button(root, text="Großes Monster", command=display_current_large_monster)
create_large_monster_btn.pack()




current_monster_to_fight_name_labe =tkinter.Label(root, text=current_monster_to_fight_name_text)
current_monster_to_fight_name_labe.place(x=600, y=10)


current_monster_to_fight_type_lable = tkinter.Label(root, text=current_monster_to_fight_type_text)
current_monster_to_fight_type_lable.place(x=600, y=50)


current_monster_to_fight_weaknesses_lable = tkinter.Label(root, text=current_monster_to_fight_weaknesses_text)
current_monster_to_fight_weaknesses_lable.place(x=600, y=90)


for i in large_monsters[41]['weaknesses']:
   print(i['stars'])




root.mainloop()




























