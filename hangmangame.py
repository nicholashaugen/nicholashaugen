# Hangperson game to guess words
# uses turtle
import random
import turtle
import math
import time

wordList = ["jazz", "spanish", "dictionary", "tissue", "yarn", "pumpkin", "moustache", "clock", "basketball",
            "sweatshirt",
            "turtle", "coffee", "goggles", "skateboard", "race", "conducted", "eloquent", "peculiar", "guess", "animal", "pencil"]
colorList = ["Green", "Red", "Orange", "Purple", "Teal", "Magenta", "Pink", "Gold"]
secretword = random.choice(wordList)
wrongLetters = []
correctLetters = []
# print(wordList)
# DONT SHOW PEOPLE THIS
print(f"The secret word is {secretword}.")
randomColor = random.choice(colorList)
sWidth = 1400
sHeight = 700
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHeight)
screen.bgcolor(randomColor)
topFont = 30
t = turtle.getturtle()
t.shape("turtle")
t.color(242, 242, 208)
t.width(5)
t.speed(0)
t.penup()

topscreenturtle = turtle.Turtle()
topscreenturtle.shape("turtle")
topscreenturtle.color(242, 242, 208)
topscreenturtle.width(5)
topscreenturtle.speed(0)

bottomscreenturtle = turtle.Turtle()
bottomscreenturtle.shape("turtle")
bottomscreenturtle.color(242, 242, 208)
bottomscreenturtle.width(5)
bottomscreenturtle.speed(0)
bottomscreenturtle.penup()
bottomscreenturtle.goto((-1 * int(sWidth/2) + int(sWidth * .1), -1 * int(sHeight/2) + int(sWidth * 0.1)))

t.hideturtle()
wrongGuesses = 0
MAX_GUESSES = 13
screenWord = "" #now its global



def drawGallows():
    t.forward(int(sWidth / 8))
    t.right(90)
    t.forward(int(sHeight * .25))
    t.left(90)
    t.pendown()
    t.forward(int(sWidth * .3))
    t.backward(int(sWidth * .15))
    t.left(90)
    t.forward(int(sHeight * 0.6))
    t.left(90)
    t.forward(int(sWidth * .15))
    t.left(90)
    t.forward(int(sHeight * .15))


def drawHead():
    t.right(90)
    t.circle(int(sHeight * 0.06))


def drawBody():
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.06) * 2)
    t.pendown()
    t.forward(int(sHeight * .15))


def drawRLeg():
    t.right(20)
    t.pendown()
    t.forward(int(sHeight * .15))
    t.penup()
    t.backward(int(sHeight * .15))


def drawLLeg():
    t.left(40)
    t.pendown()
    t.forward(int(sHeight * .15))
    t.backward(int(sHeight * .15))
    t.right(20)


def drawRShoe():
    t.left(20)
    t.forward(int(sHeight * .15))
    t.circle(int(sHeight * .02))
    t.backward(int(sHeight * .15))
    t.right(40)
    t.forward(int(sHeight * .15))


def drawLShoe():
    t.left(180)
    t.circle(int(sHeight * .02))
    t.right(180)
    t.backward(int(sHeight * 0.15))
    t.right(160)
    t.forward(int(sHeight * 0.075))
    t.right(135)


def drawRArm():
    t.forward(int(sHeight * .1))
    t.backward(int(sHeight * .1))


def drawLArm():
    t.right(90)
    t.forward(int(sHeight * .1))
    t.backward(int(sHeight * .1))


def drawLHand():
    t.forward(int(sHeight * .1))
    t.right(90)
    t.circle((sHeight * .02))
    t.penup()
    t.left(90)
    t.backward(int(sHeight * .1))


def drawRHand():
    t.left(90)
    t.forward(int(sHeight * 0.1))
    t.right(90)
    t.pendown()
    t.circle(sHeight * .02)
    t.left(90)
    t.backward(int(sHeight * 0.1))
    t.right(90)


def drawREye():
    t.penup()
    t.right(135)
    t.forward(int(sHeight * .15))
    t.right(90)
    t.forward(int(sHeight * .025))
    t.pendown()
    t.circle(int(sHeight * .006))
    t.penup()
    t.backward(int(sHeight * .05))


def drawLEye():
    t.pendown()
    t.circle(int(sHeight * .006))
    t.penup()
    t.forward(int(sHeight * .025))
    t.right(90)
    t.forward(int(sHeight * .03))
    t.left(90)


def drawMouth():
    t.pendown()
    t.forward(int(sHeight * .03))
    t.backward(int(sHeight * .06))



# drawHead()
# drawBody()
# drawRLeg()
# drawLLeg()
# drawRShoe()
# drawLShoe()
# drawRArm()
# drawLArm()
# drawLHand()
# drawRHand()
# drawREye()
# drawLEye()
# drawMouth()


def updateDrawing():
    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawBody()
    if wrongGuesses == 3:
        drawRLeg()
    if wrongGuesses == 4:
        drawLLeg()
    if wrongGuesses == 5:
        drawRShoe()
    if wrongGuesses == 6:
        drawLShoe()
    if wrongGuesses == 7:
        drawRArm()
    if wrongGuesses == 8:
        drawLArm()
    if wrongGuesses == 9:
        drawLHand()
    if wrongGuesses == 10:
        drawRHand()
    if wrongGuesses == 11:
        drawREye()
    if wrongGuesses == 12:
        drawLEye()
    if wrongGuesses == 13:
        drawMouth()

def drawWrongLetters():
    topscreenturtle.hideturtle()
    topscreenturtle.clear()
    letterString = "Wrong Letters: "
    for l in wrongLetters:
        letterString += l + ", "
    letterString = letterString[0: len(letterString) - 2]
    topscreenturtle.write(letterString, move=False, align="right", font=("Arial", topFont, "normal"))


def drawWord():
    global screenWord
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomscreenturtle.clear()
    bottomscreenturtle.hideturtle()
    bottomscreenturtle.penup()
    bottomscreenturtle.goto(-1 * int(sWidth/2) + int(sWidth * .1), -1 * int(sHeight/2) + int(sWidth * 0.1))
    bottomscreenturtle.setheading(0)

    screenWord = ""

    for letter in secretword.lower():
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottomscreenturtle.write(screenWord, move=False, align="left", font=("Arial", 86, "normal"))

    #t.goto(currentLoc)
    #t.setheading(currentHead)
print(secretword)


def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ", "

    boxTitle = "Letters used:" + badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topscreenturtle.hideturtle()
    topscreenturtle.clear()
    topscreenturtle.write(msg, move=False, align="right", font=("Arial", topFont, "normal"))
    time.sleep(2)
    topscreenturtle.clear()

def printWinOrLose(win):
    topscreenturtle.clear()
    if win:
        topscreenturtle.write("You Win!!!", move=False, align="left", font=("Arial", 70, "normal"))
    else:
        topscreenturtle.write("You Lose!!!", move=False, align="left", font=("Arial", 70, "normal"))


def getWordGuess():
    playerWordGuess = screen.textinput("Guess it", "Enter your guess of the word?")

    if playerWordGuess.lower() == secretword:
        printWinOrLose(True)
        return False
    else:
        printWinOrLose(False)
        time.sleep(1)
        writeErrorMessage(f"The secret word was {secretword}.")
        return False

gameOn = True
updateDrawing()
while gameOn:
    drawWord()
    guess = getGuess()
    if guess == "$$":
        gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need a single letter. Guess again.")
        drawWrongLetters()
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("You fool! That's not a letter!")
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guesses " + guess + ". Guess again dummy!")
    elif guess.lower() in correctLetters:
        writeErrorMessage(guess + " is in the word. Guess again you dummy.")
    else:
        if guess.lower() in secretword.lower():
            correctLetters.append(guess.lower())
            drawWord()
        else:
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updateDrawing()

        if(wrongGuesses >= MAX_GUESSES):
            writeErrorMessage("You are out of guesses. Game Over.")
            gameOn = False
            writeErrorMessage(f'The secret word was "{secretword.upper()}".')

        if "_" not in screenWord:
            writeErrorMessage("Excellent!!! YOU WIN!!")
            gameOn = False


    #get a guess()
    #check the guess()


turtle.mainloop()