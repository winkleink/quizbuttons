#! /usr/bin/python

# Written by winkleink 2013 - winkleink.blogspot.com
# use at your own risk - I never claim to know what I'm doing.
# Quiz system with lockout and scoring system

# this is a very rough bunch of code so there may be strange things that do not work as expected

# To make this work there are a number of associated files needed that need to
# be in the same folder this python script
# players.txt
#     Text to appear at the top of the screen
#     Number of players
#     Players Names
#     Player Buzzer Sounds
#     Key Players press to answer
#     Key to add points to their Score
#     Key to remove points from their score
# Obviously there has to be the relevant sound files in ogg format in the folder also

# The program is set to run full screen so it can be used as a full display
# Press 'q' (lowr case q) to quit the program

# When run the program sets up the screen with the names and the 'lights' all set to black.
# When a player presses their relevant key it changes their light to red and plays the defined sound.

# Then all players are locked out and cannot buzz in.
# While in this state the quiz master can press the relevant defined buttons to either add or remove points from the players.
# Then once finished the quiz master presses [return] to reset the board and allow the players buttons
# to work again

# at any time the quiz master can press [return] to lock out the players and an X will appear in the top right corner.

  

# Import a library of functions called 'pygame'
import pygame
from pygame.locals import * #need this for 'FULLSCREEN' value
 
# Initialize the game engine
pygame.init()
# Initialize the sound mixer
pygame.mixer.init
pygame.mixer.get_init

# declare and array for player names, player sounds, key player presses to answer key to increase score and key to reduce score
playerNames = []
playerSounds = []
playerKeys = []
playerScore = []
scoreKey = []
scoreKeyminus = []

# Define the colours used in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
red = [255, 0, 0]

# read details from the file into a string
f = open("players.txt", "r")
playersText = f.read()
print playersText

# do the parsing of the file for the relevant information
# each entry needs to be in quare brackets as these are used as as the start and end markers
# see players.txt provided for an example layout for 5 players

# start position of 1st entry for label text
numberPlayersS = playersText.find("[")

# end position of entry for players
numberPlayersE = playersText.find("]")
# read substring for number of players and convert to an integer so it's a number
quizText = playersText[numberPlayersS+1:numberPlayersE]
print quizText

# set numberPlayersS to be after Quiz text 
startNames = numberPlayersE +1

# start poistion of 1st entry for the number of players
numberPlayersS = playersText.find("[",startNames)
# end position of entry for players
numberPlayersE = playersText.find("]",numberPlayersS+1)
# read substring for number of players and convert to an integer so it's a number
numberPlayers = int(playersText[numberPlayersS+1:numberPlayersE])
print numberPlayers

# move 1 place beyond the end of the number of players.
startNames= numberPlayersE +1

# get the names of the players
for n in range(0,numberPlayers):
    numberPlayersS = playersText.find("[",startNames)
    numberPlayersE = playersText.find("]",numberPlayersS+1)
    playerNames.append(playersText[numberPlayersS+1:numberPlayersE])
    startNames = numberPlayersE+1
    print playerNames[n]

# get the sounds for the players
for n in range(0,numberPlayers):
    numberPlayersS = playersText.find("[",startNames)
    numberPlayersE = playersText.find("]",numberPlayersS+1)
    playerSounds.append(playersText[numberPlayersS+1:numberPlayersE])
    startNames = numberPlayersE+1
    print playerSounds[n]

# get the Key for the players
for n in range(0,numberPlayers):
    numberPlayersS = playersText.find("[",startNames)
    numberPlayersE = playersText.find("]",numberPlayersS+1)
    playerKeys.append(playersText[numberPlayersS+1:numberPlayersE])
    startNames = numberPlayersE+1
    print playerKeys[n]

# get the Key for Score the players
for n in range(0,numberPlayers):
    numberPlayersS = playersText.find("[",startNames)
    numberPlayersE = playersText.find("]",numberPlayersS+1)
    scoreKey.append(playersText[numberPlayersS+1:numberPlayersE])
    startNames = numberPlayersE+1
    print scoreKey[n]

# get the Key for Minus Score the players
for n in range(0,numberPlayers):
    numberPlayersS = playersText.find("[",startNames)
    numberPlayersE = playersText.find("]",numberPlayersS+1)
    scoreKeyminus .append(playersText[numberPlayersS+1:numberPlayersE])
    startNames = numberPlayersE+1
    print scoreKeyminus[n]  

# set playerScore to zero (0) for each player.
for n in range(0,numberPlayers):
    playerScore.append(0)
    print (playerScore[n])

# Set the height and width of the screen
# size=[800,600]
# set thedisplay mode to the window size set above - useful for seeing what's happening
# screen=pygame.display.set_mode(size)

# set the screen the highest resolution for this display
modes = pygame.display.list_modes(16)
screen=pygame.display.set_mode(modes[0], FULLSCREEN)
# Get the width and height of the screen as we don't know it for fullscreen
screenx, screeny = screen.get_size()

# starting with a gap of 20 on the left and 20 on the right figure out the location for the squares.
availablex = screenx-60
squarewidth = int(availablex/numberPlayers)
squaresize = int(squarewidth/5*4)
print squarewidth
print squaresize


# Fill the screen White
screen.fill(white)
# Put something in the application Bar
pygame.display.set_caption("Testing key presses")

# Set the font for the text. Windows computer so usd Ariel
myfont = pygame.font.SysFont("Ariel", 30)
# set font for score
scorefont = pygame.font.SysFont("Ariel", 60)

# Created Variable for the text on the screen
label = myfont.render(quizText, 1, black)
lockout = myfont.render("X", 1, black)
# put the text on the screen
screen.blit(label, (10, 10))

# put the players names on the screen
for n in range (0, numberPlayers):
    screen.blit(myfont.render(playerNames[n],1,black),(20+(n*squarewidth),150))                
    
# Draw the 4 empty rectangles for the players
for n in range (0, numberPlayers):
    pygame.draw.rect(screen, black, (20+(n*squarewidth),200,squaresize,squaresize), 0)

# Put the player Scores on the Screen
for n in range (0, numberPlayers):
    screen.blit(scorefont.render(str(playerScore[n]),1,black),(20+(n*squarewidth),200+squaresize+70))                


# show the whole thing
pygame.display.flip()

done=False # used to allow exit when you click close on the window
first = 0 # used to signify the first key pressed and stops other being used
waitReset = 0 # Reset section for the while loop

while done==False: # keep going unless I exit application

    # Stay in the loop until one of the 'button' keys is pressed
    while first==0 and done==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
         
            # User pressed down on a key and it is not the first one
            if event.type == pygame.KEYDOWN and first==0:

                # finding a way to check for any number of keys
                keypressed = pygame.key.name(event.key)
                print (keypressed)

                # also use q to quit (useful for full screen)
                if keypressed == "q":
                    done=True

                # allow quiz master to enter lockout mode at any time
                if event.key == pygame.K_RETURN:
                    first = 1
                    
                for n in range (0,numberPlayers):
                    if keypressed == playerKeys[n] and first==0:
                        print(playerNames[0]) # Print to console
                        pygame.draw.rect(screen, red, (20+(squarewidth*n),200,squaresize,squaresize), 0) # colour rectangle red
                        first=1 # set first to 1 so no other key presses will count
                        pygame.mixer.Sound(playerSounds[n]).play(0,0,0)
                    
                pygame.display.flip()
                # a 'button' was pressed and shown on screen
                # now go to the reset code

    # loop waiting until the 'button' are reset
    waitReset=0
    # put an x on the screen to show it is in lockout mode
    screen.blit(scorefont.render("X",1,black),(screenx-40, 10))
    pygame.display.flip()

    while waitReset==0 and done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True

                # User pressed down on a key
                if event.type == pygame.KEYDOWN:
                    keypressed = pygame.key.name(event.key)
                    print (keypressed)

                    # also use q to quit (useful for full screen)
                    if keypressed == "q":
                        done=True
                    
                    # Check if Key Pressed to increase score
                    for n in range (0,numberPlayers):
                        if keypressed == scoreKey[n]:
                            # blank out where the current score is
                            pygame.draw.rect(screen, white, (20+(n*squarewidth),200+squaresize+70, 100, 70), 0)
                            # screen.blit(scorefont.render(str(playerScore[n]),1,white),(20+(n*squarewidth),200+squaresize+70))    
                            playerScore[n] = playerScore[n] + 1
                            screen.blit(scorefont.render(str(playerScore[n]),1,black),(20+(n*squarewidth),200+squaresize+70))
                            pygame.display.flip()

                    # Check if Key Pressed to reduce score
                    for n in range (0,numberPlayers):
                        if keypressed == scoreKeyminus[n]:
                            # blank out where the current score is
                            pygame.draw.rect(screen, white, (20+(n*squarewidth),200+squaresize+70, 100, 70), 0)
                            # screen.blit(scorefont.render(str(playerScore[n]),1,white),(20+(n*squarewidth),200+squaresize+70))    
                            playerScore[n] = playerScore[n] - 1
                            screen.blit(scorefont.render(str(playerScore[n]),1,black),(20+(n*squarewidth),200+squaresize+70))
                            pygame.display.flip()
                    
                # Pressed Return Key which does a reset
                    if event.key == pygame.K_RETURN:
                        print("reset.")
                       # Draw the 4 empty rectangles for the players
                        for n in range (0, numberPlayers):
                            pygame.draw.rect(screen, black, (20+(n*squarewidth),200,squaresize,squaresize), 0)   
                        first=0
                        waitReset=1
                        # set the X back to white
                        pygame.draw.rect(screen, white, (screenx-40,10,40,40), 0)  

                        #update the screen                                                
                        pygame.display.flip()
            
            
# Quit in a clean way when done=True
pygame.quit ()
