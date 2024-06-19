from getData import data

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
        number += 1

    for i in large_monsters:
        print(f"{number}  {i['name']} es ist {i['type']}")
        number += 1
        

sort_monster()

list_of_all_species = set([])
for i in small_monsters:
    list_of_all_species.add(i['species'])
for i in large_monsters:
    list_of_all_species.add(i['species'])
