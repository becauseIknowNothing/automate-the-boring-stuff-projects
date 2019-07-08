def displayInventory(inventory):
    print("Inventory:")
    totalItems=0
    for k, v in inventory.items():
        print(str(v)+" " +k)
        totalItems+=v
    print("Total number of items: " + str(totalItems))

def addToInventory(inventory, addedItems):
    for x in addedItems:
        count=inventory.setdefault(x,0)
        inventory[x]=count + 1
    return inventory




inv={'gold coin':42, 'rope':1}
dragonLoot=['gold coin', 'dagger', 'gold coin', 'ruby', 'gold coin']
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
