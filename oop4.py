import pygame
import math
import random
# import os

#Setup display
pygame.init()
WIDTH, HEIGHT = 800, 500 #All caps represents as constants (good practice)
win = pygame.display.set_mode((WIDTH, HEIGHT)) #Set display(Dimensions) to the width and height
pygame.display.set_caption("Hangmen Game!") #Just the title / A little title label on the top bar of the game

#Load Images
images = []
for i in range(7):
    #Load a single image / pixels(surface) are stored in the variable image
    image = pygame.image.load("images/hangman" + str(i) + ".png") 
    images.append(image) #append the single image to the array(images)

#Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (RADIUS * 2 + GAP))
    letters.append([x, y, chr(A + i), True])

#Fonts
FONT_SIZE = 40
WORD_FONT = pygame.font.SysFont('comicsans', 60)
LETTER_FONT = pygame.font.SysFont('comicsans', FONT_SIZE)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#Game variables
hangman_status = 0 #Which picture(image)
words = ["HELLO", "PYTHON", "PYGAME"]
word = random.choice(words)
guessed = [] #represents what letters guessed so far

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#Setup game loop - to constantly run the game until the user quits that ends the loop
FPS = 60 #max fps
clock = pygame.time.Clock() #Create a clock object
run = True #Controls the game loop


def draw():
    win.fill(WHITE) #RGB values / the background color

    # pygame.draw.rect(win, BLACK, (startx, 370, 50, 50), 3)

    #Title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    #Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))   

    #Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2,y - text.get_height()/2))
    
    # pygame.draw.circle(win, BLACK, (WIDTH / 2, 400), RADIUS, 3)
    win.blit(images[hangman_status], (150,100)) #blit(draw surface) - display the image then the coordinates in the display
    pygame.display.update() #required to manually tell pygame to update when there is changes to the display

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() / 2, HEIGHT/2 - text.get_width() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

#Note: while loops in a function only access local variables
# test1 = True
# test2 = True
# while test1:
#     print("Test 1 " + str(test1))
#     test1 = False

# def test_loop():
#     print("Test 2 " + str(test2))
#     # while test2:
#     #     print("Test 2 " + str(test2))
#     #     test2 = False
# test_loop()  

while run: #Starts the loop of the game while run is True 
    #Note: this while loop, loops 60 times per second
    clock.tick(FPS) #controls the speed of the loop/ in this case 60fps per tick(60 loops per sec)

    #Events - every interaction the user to the game an event is triggered(ex. mouse click)
    #You can get the event in the pygame.event / looping through all the events
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #If the user clicks the close button
            run = False #Stops the loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() #get_pos - position(x/y position of the mouse)
            # print(mouse_x, mouse_y)
            for letter in letters:
                x, y, ltr, visible = letter

                if visible:
                    dis = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2) #pythagorean - distance between 2 points 
                    if dis < RADIUS:
                        # print(ltr)
                        guessed.append(ltr)

                        if ltr not in word: #If Wrong
                            hangman_status += 1
                            # if hangman_status < 6:
                            #     hangman_status += 1
                            # else:
                            #     print("GAME OVER!")
                        letter[3] = False #letter[3] is the index of the visible variable 
    draw() #It will execute 60 times per second

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        print("You Won!")
        display_message("You Won!")
        break
    
    if hangman_status == 6:
        print("You lost!")
        display_message("You Lost!")
        break

pygame.quit() #close the window
