import sys
import operator
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def display_inventory(inventory):
    print("-----INVENTORY-----")
    for i, v in inventory.items():
        print(v, i)
    allitems = sum(inventory.values())
    print("Total numbers of items: {0}".format(allitems))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1


def print_table(inventory, order):

    if order == "count,desc":
        print("---- Desc Sort ----")
        inventory = sorted(inventory.items(), key=operator.itemgetter(1),reverse=True)
        for i in inventory:
            print(i[1], i[0])
    elif order == "count,asc":
        print("---- Asc Sort ----")
        inventory = sorted(inventory.items(), key=operator.itemgetter(1))
        for i in inventory:
            print(i[1], i[0])
    else:
        display_inventory(inv)

def import_inventory(inventory, filename):
    f = open(filename, "r", encoding = 'utf-8')
    mylist = f.read().split(',')
    for i in mylist:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    f.close
def export_inventory(inventory, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i, k in inventory.items():
            for x in range(0, k):
                f.write(i + ",")
    f.close

display_inventory(inv)
import_inventory(inv, "inventory.csv")
display_inventory(inv)
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
order = ""
print_table(inv,order)
export_inventory(inv, "export_inventory.csv")