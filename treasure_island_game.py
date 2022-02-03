#three single quotes allows us to print multiple strings in the console
print(''' 
                                                       
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')


print("Welcome to Treasure Island!")
print("")
print("Your mission is to make decisions rightfully in order to survive and finally get your treasure!")
print("")
crossroad = input('''You\'re about to cross a road in order to go to your island.\nWhich direction will you go? Type "left" or "right": ''').lower()
# \ will escape the string and see it as a text.
#.lowercase() will give freedom to users to type their decisions in both upper or lowercase wihtout generating any error.
#again using triple single quotes to multiple strings together.
if crossroad == "left":
  lake = input('''Cool! You have reached a lake.\nType "swim" if you want to swim over the lake and\n"wait" if you want to wait for a boat: ''').lower()
  if lake == "wait":
    room = input('''Great! You are very close to your treasure!\nNow for a night you have to choose among 3 rooms for you to take rest.\nChoose carefully which room you want to choose. Type "1","2" or "3": ''')
    if room == "2":
      print("Congratulations! You have discovered the treasue <3")
    else:
      print("Game Over! You entered the wrong room full of monsters who made you their feast and you died. ")
  else:
    print("Game Over! You got eaten by sea monsters while swimming")
else:
  print("Game Over! You died after falling into a pit full of snakes ")

 


