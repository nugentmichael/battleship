# Battleship Game in Python!

# Import randint function from the random library.
from random import randint

# Create an empty list and store it in the grid variable.
grid = []

# Create a 5x5 grid of "O"s.
for x in range(10):
  grid.append(["O"] * 10)

# Loop through the rows and add an empty blank character space between each column character.
def ocean_board(grid):
  for row in grid:
    print " ".join(row)

# Dsplay the ocean board grid.
ocean_board(grid)

# Randomize the row order.
def random_row(grid):
  row = []
  rand_row = randint(0, len(grid) - 1)
  row += [rand_row - 1, rand_row, rand_row + 1]
  return row

# Randomize the column order.
def random_col(grid):
  col = []
  rand_col = randint(0, len(grid[0]) - 1)
  col += [rand_col - 1, rand_col, rand_col + 1]
  return col

# Set the ship_row and ship_col variables to where the battleship is located on the grid.
ship_row = random_row(grid)
ship_col = random_col(grid)

# Uncomment if you wish to display where the battleship is located on the grid.
print ship_row
print ship_col

# Add global hit counter variable.
hit = 0

# Run through player turns.
for turn in range(9):
  # Display the current turn number and prompt the player for their guess to where the battleship is located on the grid.
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Column: "))

  # If the guessed row and column equals to where the battleship is located, the battleship has sunk and the game is now over.
  if guess_row in ship_row and guess_col in ship_col:
    print "I've been hit!"
    # Increase the hit count by one.
    hit = hit + 1

    # If the hit counter equals to 3, the battleship has sunk, and the game is now over.
    if hit == 3:
      print "You sunk my battleship!"
      break
  # If the battleship has not sunk, keep playing.
  else:
    # If the guess is outside of the grid, display an error message.
    if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
      print "The battleship is not docked. Please try another guess in the ocean."
    # If the player has already guessed to where the battleship is location on the grid...
    elif (grid[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    # If the player guessed an area to where the battleship is not located, they missed.
    else:
      print "You missed my battleship!"
      grid[guess_row][guess_col] = "X"

    # Advance the turn number by one.
    print turn + 1
    ocean_board(grid)

    # After four turns, the game is now over.
    if turn == 9:
      print "Game Over!"