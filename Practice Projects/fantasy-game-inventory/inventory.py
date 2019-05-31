# inventory


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v), k)
        item_total += v
    print('\nTotal number of items: ' + str(item_total))


def add_to_inventory(inventory, add_items):
    for item in add_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
