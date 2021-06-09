from Player import Player
from Option import Option

# A room is a collection of options with an id and a description to show the user.
# It includes methods create a list of option objects and interact with them.
# Should check if the requirements for an option are met before asking option to display itself.
class Room:
  def __init__(self, id, description, options):
    self.id = id
    self.description = description
    self.options = []
    # args or len(args) > 0 for check?
    # do I even need a check?
    if len(options)>0:
      for option in options:
        self.options.append(Option(option))
    self.valid = []


  def describe(self, player):
    # give room description
    print('\n' + self.description)      
    # track index of choice presented
    index = 0
    # clear array of currently valid options
    self.valid = []
    # loop through, display, and record currently valid options
    # again, should check be this or len(self.options)?
    if len(self.options)>0:
      print('\n')
      for option in self.options:
        index += 1
        check = option.display(player)
        if check != None:
          print (f'{index}) {check}')
          self.valid.append(index)

  def choose(self, player):
    # get valid input
    while(True):
      selection = str(input("\nWhat do you do? (enter number) "))
      if (not selection.isdigit()) or (int(selection) not in self.valid):
        print("\nPlease enter a number from the listed options.\n")
        self.describe(player)
      else:
        break
    # invoke option (returns id/index of next room)
    return self.options[int(selection) - 1].give_result(player)
    