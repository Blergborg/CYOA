from Player import Player

# An Option is a choice slected by the user that advances the story in some way.
# Options have methods to say which room should be accessed next, and any changes
# that need to be made to a player's inventory. 
class Option:
  def __init__(self, opt_data):
    self.text = opt_data['text']
    self.available = opt_data['available']
    self.result = opt_data['result']
    self.gain = opt_data['gain']
    self.lose = opt_data['lose']
    self.goto = opt_data['goto']


  def display(self, player):
    # confirm option is available
    availability = self.available
    valid = None
    if availability != None:
      if availability.startswith('!'):
        if player.inventory[availability[1:]] == False:
          valid = self.text
      elif player.inventory[availability] == True:
        valid = self.text
    else:
      valid = self.text
    return valid

  # doesn't feel properly OO. 
  # return gain/lose item values to main or room, then call player methods there?
  def give_result(self, player):
    # communicate result text
    if self.result:
      print('\n' + self.result + '\n')
    # make/communicate inventory changes
    if self.gain:
      player.addItem(self.gain)
    if self.lose:
      player.useItem(self.lose)
    # return next room to go to
    return self.goto
