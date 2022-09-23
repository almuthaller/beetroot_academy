# Recreate a https://en.wikipedia.org/wiki/Battleship_(game) with a python. 
# Firstly - two users have a 2 lists of ships. They place them one after another on a battle-field. 
# For it they just wrote a coordinates like it "ship start: x-1, y-1. Ship end x-2, y-1". 
# After it, they start shooting each other table. If user A hits a ship - print "hit" and allow him to go one more time. 
# Hit command will be "Try x-1, y-1". If all ships destroyed for one of users - print ("User {name} win") and finish the game

# Alternative task: play against computer

# Ships:
# Battleship 4
# Destroyer 3
# Submarine 2
# Patrol Boat 1


my_ships = []
water = []

# Output battlefield as table:

battlefield = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def print_row(row_number):
    if row_number == 9:
        print(f"{row_number + 1}", battlefield[row_number])
    else:
        print(f"{row_number + 1} ", battlefield[row_number])

def print_battlefield():
    print("   ", "A  B  C  D  E  F  G  H  I  J")
    row_count = 0
    while row_count < 10:
        print_row(row_count)
        row_count += 1


# Place ships:

x_coordinates = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}

def place_ship(letter, number):
    x_coord = x_coordinates[letter] - 1
    y_coord = number - 1
    battlefield[y_coord][x_coord] = 1

place_ship("A", 3)    
print_battlefield()



# generate coputer's ships

# place my ships

# computer generated guesses

# function for hit or miss

# show battlefield as output? your own field can be invisible, just print (so and so many ships left)