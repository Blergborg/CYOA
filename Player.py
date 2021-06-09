# A Player is total list of the user's possible inventory that indicates whether or not
# the user currently has an item or not.
# It includes methods that can edit the posession status of each possible item, and list
# the items currently in the user's possession.
class Player:
  
  def __init__(self, inventory):
    self.inventory = inventory
  
  def seeInventory(self):
    for key in self.inventory.keys():
      if self.inventory[key] == True:
        print(key)
    print('\n')
  
  def addItem(self, item):
    if item in self.inventory:
      if self.inventory[item] == False:
        self.inventory[item] = True
        print(f'Gained: {item}')

  def useItem(self, item):
    if item in self.inventory:
      if self.inventory[item] == True:
        self.inventory[item] = False
        print(f'Used: {item}')
