from Test_Input import testinput

# Function that converts the expected input into a list of integers.
def convertToListOfDigits(maze):
    maze = maze.split("\n")
    digitmaze = list(map(int, maze))
    return digitmaze

# Function that performs every step required for part one, not sure how to break down. Tried extracting such that
# one step could be isolated and tested, but didn't seem particularly neat or useful.
def jump(maze):
    maze = convertToListOfDigits(maze)
    numberofsteps = 0
    index = 0
    while(index < len(maze)):
        stepstojump = maze[index]
        maze[index] += 1
        index = stepstojump + index
        numberofsteps += 1

    return numberofsteps


# Function for part 2, with if statement extracted below, again not sure how to structure better.
def jumpPart2(maze):
    maze = convertToListOfDigits(maze)
    numberofsteps = 0
    index = 0
    while(index < len(maze)):
        stepstojump = maze[index]
        changeOffsetValue(index, maze)
        index = stepstojump + index
        numberofsteps += 1

    return numberofsteps


def changeOffsetValue(index, maze):
    if maze[index] < 3:
        maze[index] += 1
    else:
        maze[index] -= 1

# print(jumpPart2(testinput))