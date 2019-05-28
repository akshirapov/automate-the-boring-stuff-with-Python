# inventory

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v), k)
        item_total += v
    print('\nTotal number of items: ' + str(item_total))


def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
