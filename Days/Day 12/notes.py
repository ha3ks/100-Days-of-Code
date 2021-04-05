##Day 12

#Nam2spaces and Scope

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope
player_health = 10

def game():
    def drink_potion():
        potion_strentgh = 2
        print(player_health) #local variable

    drink_potion()
#will show 'is not defined' error as it is outside of the function.
print(potion_strentgh)   #global variable


# There is no Block Scope in Python

game_level = 3
def create_enemy():
    enemies = ["Skeletons", "Zombies", "Aliens"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)


#How to modify a global variable
enemies = 1

def increase_enemies():
#  global enemies            
#  enemies += 1                                               
#goes out and finds the global variable but can cause issues where the global has been created elsewhere in the code (could be buggy), can read it and use it but just dont try and modify it
  print(f"enemies inside function: {enemies}")
  return enemies + 1


increase_enemies()
print(f"enemies outside function: {enemies}")


#Python Constraints and Global scope
Pi= 3.14159
URL = "http@//www.google.com"

#normally these have CAPS so you can call them later and know not to change them



#EXECRISE The Number Guessing Game