import random

options = ("piedra", "papel", "tijera")

rounds = 1
computer_wins = 0
user_wins = 0

def choose_options():
  user_option = input("Piedra, papel o tijera? --")
  user_option = user_option.lower()
  
  
while True: 
  print("+" *10)
  print("ROUND", rounds)
  print("+", 10)

  print("computer_wins", computer_wins)
  print("user_wins", user_wins)
  
  user_option = input("Piedra, papel o tijera? --")
  user_option = user_option.lower()
  
  computer_option = random.choice(options)
  
  
  if not user_option in options: 
    print("Esa opción no es válida")
    continue #Se salta lo siguiente
  
  print("User option---", user_option)
  print("Computer Option--", computer_option)
  
  if user_option == computer_option:
    print("Empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("Usuario ganó")
      user_wins += 1
      
    else:
      print("papel gana a piedra")
      print("Computer ganó")
      computer_wins += 1
