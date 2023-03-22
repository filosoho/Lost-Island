print('''
                                                    ____
                                        v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                         .
          X        \O/                              |\\
          X ####    M                               |_\\
          X.###########.  .                       __|__
    .###################.                         \\   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Welcome to Lost Island.")
print("Your mission is to find a way out.") 

direction = input("\nWhich way would you like to go? Right or left? ").lower()
if direction == 'left':
  action = input("Do you want to swim or wait? swim/wait ").lower()
  if action == 'wait':
    rescue = input("You see a ship, a helicopter and a girl in the water. Which do you choose? ship/helicopter/girl? ").lower()
    if rescue == 'girl':
      print("The girl is a Superwoman and flies with you to the land. You are rescued! You win!")
    elif rescue == 'ship':
      print("You boarded the ship, but they are pirates! Arrrrrgghh! You died. Game over.")
    elif rescue == 'helicopter':
      print("The helicopter takes you in, but it rans out of fuel. You sank in the ocean. Game over.")
    else:
      print("Game over.")
  else:
    print("A shark attacked you. You died. Game over.")
else:
  print("You fell into the ocean. Game over.")
      
  