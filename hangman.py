# hangman.py

# Name: Isabella Wang
# Collaborators: jessie helped :)

## getting modules
from graphics import *
from time import sleep
## drawing screen and background
win = GraphWin("Hangman", 800, 900)
win.setBackground("lemonchiffon")


## defining my functions
#Scaffold code here
def Scaffold():
    Scaffold_horiz = Line(Point(200, 500), Point(300, 500))
    Scaffold_horiz.setWidth(3)
    Scaffold_horiz.draw(win)
    Scaffold_vert = Line(Point(250, 500), Point(250, 200))
    Scaffold_vert.setWidth(3)
    Scaffold_vert.draw(win)
    Scaffold_minihoriz = Line(Point(250,200), Point(375, 200))
    Scaffold_minihoriz.setWidth(3)
    Scaffold_minihoriz.draw(win)
    Scaffold_minivert = Line(Point(375, 200), Point(375, 225))
    Scaffold_minivert.setWidth(3)
    Scaffold_minivert.draw(win)

#Head code here

def Face():
    Face = Circle(Point(375, 250), 25)
    Face.setWidth(3)
    Face.setFill("navajowhite")
    Face.draw(win)
    return Face

def EyeShape():
    EyeShape = Oval(Point(370, 230), Point(380, 250))
    EyeShape.setWidth(3)
    EyeShape.setFill("white")
    EyeShape.draw(win)
    return EyeShape

def Pupil():
    Pupil = Circle(Point(375, 245), 5)
    Pupil.setWidth(3)
    Pupil.setFill("black")
    Pupil.draw(win)
    return Pupil

def Mouth():
    Mouth = Line(Point(370, 260), Point(380,260))
    Mouth.setWidth(3)
    Mouth.draw(win)
    return Mouth

#Torso code here

def Torso():
    Body = Polygon(Point(375, 275), Point(355, 450), Point(395, 450))
    Body.setWidth(3)
    Body.setFill("lawngreen")
    Body.draw(win)
    return Body

#Left Leg code here
def Left_Leg():
    Leg = Oval(Point(330, 450), Point(375, 480))
    Leg.setWidth(3)
    Leg.setFill("yellowgreen")
    Leg.draw(win)
    return Leg

#Right Leg code here
def Right_Leg():
    Leg = Oval(Point(375, 450), Point(415, 480))
    Leg.setWidth(3)
    Leg.setFill("yellowgreen")
    Leg.draw(win)
    return Leg

#Left Arm code here

def Left_Arm():
    Arm = Line(Point(310, 265), Point(375, 275))
    Arm.setWidth(3)
    Arm.draw(win)
    return Arm


#Right Arm code here
def Right_Arm():
    Arm = Line(Point(440, 265), Point(375, 275))
    Arm.setWidth(3)
    Arm.draw(win)
    return Arm
    

def start():
    result = ""
    for letter in word:
        result = result + letter + " "
    word_letters = result.split()
    return word_letters

def display(letter, word):
    result = ""
    for each_letter in word:
        if each_letter in letter:
            each_letter = each_letter
        else:
            each_letter = "_ "
        result = result + str(each_letter)
    global result
    global result_on_screen
    result_on_screen = text(Point(400, 650), result)
    return result

def clear():
    for each_item in win.items[:]:
        each_item.undraw()
    win.update()
    
count = 1
def guess():
    inputBoxguess = Entry(Point (500, 600), 20)
    inputBoxguess.draw(win)
    guess_old_text = "Guess a letter:"
    guess_old_appear = text(Point(260, 600), guess_old_text)
    cont_box(guess_old_appear)
    guess_old = inputBoxguess.getText()
    guess = guess_old.lower()
    inputBoxguess.undraw()
    if guess in user_has_guessed:
        samenumber = text(Point(400, 800), "Don't guess the same number twice!!")
        time.sleep(1)
        samenumber.undraw()
    if guess in word:
        user_has_guessed.append(guess)
    if guess not in word and guess not in user_has_guessed:
        user_has_guessed.append(guess)
        sorry = text(Point(400,800), "Nope, try again!")
        time.sleep(1)
        sorry.undraw()
        global count
        count = count + 1
        count1(count)
    return user_has_guessed

def text(coordinates, text):
    printedtext = Text(coordinates, text)
    printedtext.setSize(15)
    printedtext.setStyle("bold")
    printedtext.setTextColor("turquoise")
    printedtext.draw(win)
    return printedtext

def textsmall(coordinates, text):
    printedtext = Text(coordinates, text)
    printedtext.setSize(11)
    printedtext.setStyle("bold")
    printedtext.setTextColor("turquoise")
    printedtext.draw(win)
    return printedtext

bodyparts = []
def count1(count):
    if count == 2:
            face = Face()
            eyeshape = EyeShape()
            pupil = Pupil()
            mouth = Mouth()
            bodyparts.append(face)
            bodyparts.append(eyeshape)
            bodyparts.append(pupil)
            bodyparts.append(mouth)
    elif count == 3:
            torso = Torso()
            bodyparts.append(torso)
    elif count == 4:
            left_arm = Left_Arm()
            bodyparts.append(left_arm)
    elif count == 5:
            right_arm = Right_Arm()
            bodyparts.append(right_arm)
    elif count == 6:
            left_leg = Left_Leg()
            bodyparts.append(left_leg)
    elif count == 7:
            right_leg = Right_Leg()
            bodyparts.append(right_leg)

def cont_box(thing):
    rect = Rectangle(Point (365, 740), Point(435, 760))
    continue_text = Text(Point(400, 750), "Continue")
    rect.setFill("skyblue")
    rect.draw(win)
    continue_text.draw(win)
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    if x <= 435 and x >= 365 and y<=760 and y>=740:
        thing.undraw()
    else:
        cont_box(thing)       

## text:
title = Text(Point(400, 50), "HANGMAN!")
title.setSize(30)
title.setStyle("bold")
title.setTextColor("turquoise")
title.draw(win)
Scaffold()
## defining variables for first run through
player_1_points = 0
player_2_points = 0
play_again = 'Yes'
## starting program for the first time. Saved player names and correct word.

while play_again == 'Yes':
    bodyparts = []
    user_has_guessed = []
    count = 1
    welcome = text(Point (400, 565), "Welcome to Hangman!!")
    inputBox = Entry(Point (500, 600), 20)
    inputBox.draw(win)
    player_1_text = "What is player 1's name?"
    player_1_name = text(Point(260, 600), player_1_text)
    cont_box(player_1_name)
    player_1 = inputBox.getText()
    inputBox.undraw()
    inputBox2 = Entry(Point (500, 600), 20)
    inputBox2.draw(win)
    player_2_text = "What is player 2's name?"
    player_2_name = text(Point(260, 600), player_2_text)
    cont_box(player_2_name)
    player_2 = inputBox2.getText()
    inputBox2.undraw()
    time.sleep(0.3)
    hello1 = text(Point(400, 600), "Hello " + player_1 + "!")
    hello2 = text(Point(400, 620), "Hello " + player_2 + "!")
    cont_box(hello1)
    hello2.undraw()
    inputBox3 = Entry(Point (600, 600), 20)
    inputBox3.draw(win)
    word_text = player_1 + ", please choose a word. Make sure " + player_2 + " isn't looking!"
    word_text_appear = textsmall(Point(260, 600), word_text)
    cont_box(word_text_appear)
    correct_word = inputBox3.getText()
    print inputBox3.getText()
    inputBox3.undraw()
    word = correct_word.lower()
    start_guessing = text(Point (400, 600), "Now it's time for " + player_2 + " to start guessing! You have 6 lives.")
    cont_box(start_guessing)

## making the list for the letters in the correct word and running through my functions
    first_guess = True
    while first_guess == True:
        word = start()
        letter = guess()
        global display_word
        display_word = display(letter, word)
        letters_guessed = text(Point(550, 100), "Letters Guessed:")
        actual_letters = text(Point (550, 130), user_has_guessed)
        first_guess = False
    ## ending the game/restarting the game if second player guesses correctly
        if "_ " not in result:
            congrats = text(Point (400, 700), "Congrats, " + player_2 + " ! You win!!")
            player_2_points = player_2_points + 1
            scoreboard = text(Point(400, 720), "SCOREBOARD~ Player 1: " + str(player_1_points) + "   Player 2: " + str(player_2_points))
            yesnobox = Entry(Point (500, 600), 20)
            yesnobox.draw(win)
            gameoverquestion = "Would you like to play again? (Yes or No)"
            gameoverquestionappear = text(Point(260, 600), gameoverquestion)
            cont_box(gameoverquestionappear)
            play_again = yesnobox.getText()
            yesnobox.undraw()
            congrats.undraw()
            scoreboard.undraw()
            result_on_screen.undraw()
            for each_part in bodyparts:
                each_part.undraw()
            break
        
    while count<=6 and first_guess == False:
        word = start()
        letter = guess()
        result_on_screen.undraw()
        display_word = display(letter, word)
        actual_letters.undraw()
        actual_letters = text(Point (550, 130), user_has_guessed)
        global actual_letters
    ## ending the game/restarting the game if second player guesses correctly
        if "_ " not in result:
            congrats = text(Point (400, 700), "Congrats, " + player_2 + " ! You win!!")
            player_2_points = player_2_points + 1
            scoreboard = text(Point(400, 720), "SCOREBOARD~ Player 1: " + str(player_1_points) + "   Player 2: " + str(player_2_points))
            yesnobox = Entry(Point (500, 600), 20)
            yesnobox.draw(win)
            gameoverquestion = "Would you like to play again? (Yes or No)"
            gameoverquestionappear = textsmall(Point(250, 600), gameoverquestion)
            cont_box(gameoverquestionappear)
            play_again = yesnobox.getText()
            yesnobox.undraw()
            congrats.undraw()
            scoreboard.undraw()
            result_on_screen.undraw()
            actual_letters.undraw()
            for each_part in bodyparts:
                each_part.undraw()
            break

## ending the game/restarting the game if player 2 never gets the word
        if count > 6:
            boohoo = text(Point (400, 700), "Sorry, " + player_2 + " you lose!")
            player_1_points = player_1_points + 1
            scoreboard = text(Point(400, 720), "SCOREBOARD~ Player 1: " + str(player_1_points) + "   Player 2: " + str(player_2_points))
            yesnobox = Entry(Point (500, 600), 20)
            yesnobox.draw(win)
            gameoverquestion = "Would you like to play again? (Yes or No)"
            gameoverquestionappear = textsmall(Point(250, 600), gameoverquestion)
            cont_box(gameoverquestionappear)
            play_again = yesnobox.getText()
            yesnobox.undraw()
            boohoo.undraw()
            scoreboard.undraw()
            result_on_screen.undraw()
            actual_letters.undraw()
            for each_part in bodyparts:
                each_part.undraw()
            break

win.mainloop()

## sorry didn't have time to figure out how to undraw the letters guessed and the body parts after restarting.
