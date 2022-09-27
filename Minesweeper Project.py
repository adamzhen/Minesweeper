import random

#FUNCTIONS
def printGrid(matrix): #prints grid
    print("  a b c d e f g h i j")
    print(" ---------------------")
    for i in range(10):
        print(str(i), end = "|")
        for j in range(10):
            print(str(matrix[i][j]), end = "|")
        print("\n ---------------------")
def setMines(n): #randomly creating n mines
    indices = [0,1,2,3,4,5,6,7,8,9]
    for i in range(n):
        r = random.choice(indices)
        c = random.choice(indices)
        while [r, c] in mines:
            r = random.choice(indices)
            c = random.choice(indices)
        mines.append([r, c])
        BOARD[r][c]="X"
def countMines(w, h): #counting number of mines adjacent to a certain square
    neighbors = []
    for i in range(w-1, w+2):
        for j in range(h-1,h+2):
            if i<=9 and i>=0 and j<=9 and j>=0:
                neighbors.append(BOARD[i][j])
    return neighbors.count("X")
def drawNumbers(): #setting up adjacent mine numbers
    for i in range(w):
        for j in range(h):
            if [i, j] not in mines:
                c = countMines(i, j)
                if c>0:
                    BOARD[i][j]=c;
def inputFormat(x): #turns string input into a list
    return [x[0:1].upper(), int(x[1:2]), convertLetters[x[2:3].lower()]]
def validInput(x): #checks for correct format of input
    valFormat = (x[0:1].upper()=="R" or x[0:1].upper()=="F") and x[1:2] in strnumbers and x[2:3].lower() in letters
    if not valFormat:
        return valFormat
    else:
        nx = inputFormat(x)
        return [nx[1], nx[2]] not in revealed
def winningBoard(): #creates the correct format for the winning board
    ans = [[" " for x in range(w)] for y in range(h)] 
    for i in range(10):
        for j in range(10):
            if KEY[i][j]==" ":
                ans[i][j]="R"
            elif KEY[i][j]=="X":
                ans[i][j]="F"
            else:
                ans[i][j]=KEY[i][j]
    return ans

#MAIN CODE
w, h = 10, 10
BOARD = [[" " for x in range(w)] for y in range(h)] 
KEY = [[" " for x in range(w)] for y in range(h)]
WIN = [[" " for x in range(w)] for y in range(h)]
mines = []
revealed = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
strnumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = [0,1,2,3,4,5,6,7,8,9]
convertLetters = {letters[i]: numbers[i] for i in range(len(letters))}

print("WELCOME TO MINESWEEPER\n")
printGrid(BOARD)
mode = input("GAME MODE\nVisible mode is only for debugging, Hidden mode is the actual game \nEnter 1 for visible mode or 2 for hidden mode: ")
while mode!="1" and mode!="2":
    mode = input("Please enter 1 or 2: ")
setMines(10)
drawNumbers()
KEY = BOARD
WIN = winningBoard()
if mode=="1":
    print("\nVISIBLE MODE\n")
elif mode=="2":
    print("\nHIDDEN MODE\n")
    BOARD = [[" " for x in range(w)] for y in range(h)]
continueGame = True
print("DIRECTIONS")
print("Play by entering 3-character inputs: The 1st character should be either R for reveal, or F for flag.")
print("The next 2 characters should be which location you want to reveal or flag, using the row number \nfollowed by the column letter of the desired location.")
print("Ex. r2e, f8a")
print("Flagging a location will put an F on it, and if you want to remove the flag, simply flag the location again.\nRevealing a location will tell you the number of mines next to it. If there are no mines, it will show an R.")
print("Enter quit if you ever want to quit the game.")
print("HAVE FUN!\n")
#GAME LOOP
while continueGame:
        printGrid(BOARD)
        x = input("Enter input: ")
        #quit game mechanism
        if x.lower() == "quit":
            break
        while not validInput(x):
            x = input("Please enter a valid input: ")
        [t, a, b] = inputFormat(x)
        if t=="R":
            if KEY[a][b]=="X":
                BOARD[a][b]="X"
                printGrid(BOARD)
                print("You hit a mine. GAME OVER.")
                continueGame = False
            elif KEY[a][b]==" ":
                BOARD[a][b]="R"
            else:
                BOARD[a][b]=KEY[a][b]
            revealed.append([a, b])
        elif t=="F":
            if BOARD[a][b]=="F":
                BOARD[a][b]=" "
            else:
                BOARD[a][b]="F"  
        if BOARD==WIN:
            printGrid(BOARD)
            print("Congratulations! YOU WON!!")
            continueGame = False

