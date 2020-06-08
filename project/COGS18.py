from tkinter import * 
import pygame
import random
class UtilityBelt:
    def chat_with_me(self):
        chat = 'continute'
        while(True):
            chat = input('How are you feeling today? \n')
            if(str(chat)=='Exit'):
                break
            if('sad'in str(chat)):
                chat = input('what about your situation is making you sad? \n')
                chat = input('I am sorry to hear that, have you felt this way in the past? \n')
                if(str(chat)== 'yes'):
                    chat = input('What do you think could be the cause of your currernt situaion? \n')
                    if("I don't know" in str(chat)):
                        chat = input('Maybe we could try starting from your earliest memory of this case. Would that be okay with you? \n')
                        if('yes' in str(chat)):
                            chat = input('Thank you for opening yourself up to me. After all I am just a program. When did you begin feeling this way? \n')
                            chat = input('I see. Perhaps it would be helpful to write about it and dont let me interupt. Just try writing everything you can. \n')
                            print('Thank you for sharing that with me!')
                            chat = input('Anthing else I could do for you? \n')
                    else:
                        chat = input('I understand. Life could be very confusing at times but you will get through it! Would you like to continue? \n')
                        if('yes' in str(chat)):
                            chat = input('What other feelings are you currently having? \n')
                            if('happy'in str(chat)):
                                chat = input('What about the situation is making you feel happy? \n')
                                chat = input('That is great! We need some positivity in our life. Even computer programs understand the importance of happiness. \n')
                                if(str(chat)=='Exit'):
                                    break
                        if('no' in str(chat)):
                            break
                if(str(chat)=='Exit'):
                    break
            if('happy' in str(chat)):
                chat = input('I am happy to hear that, What things are making you happy? \n')
                chat = input('I am happy to hear that! Things seem to be looking up huh? \n')
                chat = input('Would you like to continue? \n')
                if('yes' in str(chat)):
                    chat = input('What more would you like to say to me? \n')
                    chat = input('Intersting! Thank for sharing. Any more stories for me?')
                    if('yes' in str(chat)):
                        print('Thank you for sharing that with me! You have made a computer very happy!')
                        break
                    if('no' in str(chat)):
                        print('Thank you! Have a great day!')
                        break
            if('meh'in str(chat)):
                chat = input('Maybe a joke could make you feel better? Would you like to hear one? \n')
                if('yes' in str(chat)):
                    chat = input('What do you call a Mexican in a low car? \n')
                    chat = input('Close enough. Carlos')
                    chat = input('Want another? ')
                    if('yes' in str(chat)):
                        chat = input('What does a Mirmade use to wash her fins? \n')
                        chat = input('close. Tide. 01101000 01100001 (computer laughter, ie. ha)')
                        chat = input('Want more? \n')
                        if('yes' in str(chat)):
                            chat = input('Why did the picture go to jail? \n')
                            print('Because it was framed. 01101000 01100001')
                            chat = input('Continue?')
                            if('yes' in str(chat)):
                                chat = input('You heard the rumor about the butter?')
                                chat = input("Nvm, I shoudn't spread it. 01101000 01100001")
                                chat = input("Oh these are good. I shouldn't have to ask since I predicted you want more but you want more? \n")
                                if('yes' in str(chat)):
                                    chat = input('What do you call a person who doesnt toot in public? \n')
                                    print('A private tooter. 01101000 01100001')
                                    chat = input('More?!?!?!?!?!')
                                    if('yes' in str(chat)):
                                        chat = input('What did the buffalo say to his son when he left for college?')
                                        print('Bison. 01101000 01100001')
                                        chat = ('laughter cures many things. Youre welcome. ')
                                        break

            else:
                chat = input('what else could I do for you? \n')
                if(str(chat)=='Exit'):
                    break

    def calculator(self):
        operation = input('Select an operation ie.(*,+,/,^,%,Avr): ')
        if(operation == '+'):
            x = input('Enter number to add: ')
            y = input('Enter second number to add: ')
            a = int(x) + int(y)
            print(a)
        elif(operation == '-'):
            ###promt to choose what numbers to subtract
            x = input('Enter number to subtract: ')
            y = input('Enter number to subtract: ')
            a = int(x) - int(y)
            print(a) 
        elif(operation == '*'):
            ###promt to choose what numbers to multiply
            x = input('Enter number to multiply: ')
            y = input('Enter 2nd number to multiply: ')
            a = int(x)*int(y)
            print(a) 
        elif(operation == '/'):
            ###promt to choose what numbers to divide
            x = input('Enter number to divide(numerator): ')
            y = input('Enter number to divide(denominator): ')
            a = int(x)/int(y)
            print(a)
        elif(operation == '%'):
            ###promt to choose what numbers to get the remainder for
            x = input('Enter number to find its remainder: ')
            y = input('Enter remaider value: ')
            a = int(x)%int(y)
            print(a)
        elif(operation == '^'):
            ###promt to choose what numbers to power
            x = input('Enter number to square: ')
            y = input('Enter exponent: ')
            a = int(x)**int(y)
            print(a)
        elif(operation == 'Avr'):
            x = int(input('Enter amount of values in list: '))
            counter = 0
            summation = 0
            for i in range(0,x):
                average = int(input('Enter number: '))
                summation += average 
            print('The average of entered numbers is: ' + str(summation/x))
        else:
            print('Not part of the options')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Classes


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Set the player x position to the mouse x position
        self.rect.x = pos[0]


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3

interact = input('Welcome to my utility belt class. You could choose between chat_with_me, calculator \n')
if(str(interact)=='chat_with_me'):
    Attempt = UtilityBelt()
    Attempt.chat_with_me()
if(str(interact) == 'calculator'):
    attempt = UtilityBelt()
    attempt.calculator()
if(str(interact)=='game'):
    # --- Create the window

    # Initialize Pygame
    pygame.init()

    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])

    # --- Sprite lists

    # This is a list of every sprite. All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    # List of each block in the game
    block_list = pygame.sprite.Group()

    # List of each bullet
    bullet_list = pygame.sprite.Group()

    # --- Create the sprites

    for i in range(50):
        # This represents a block
        block = Block(BLUE)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(350)

        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

    # Create a red player block
    player = Player()
    all_sprites_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    score = 0
    player.rect.y = 370

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        # --- Game logic

        # Call the update() method on all the sprites
        all_sprites_list.update()

        # Calculate mechanics for each bullet
        for bullet in bullet_list:

            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)

            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

        # --- Draw a frame

        # Clear the screen
        screen.fill(WHITE)

        # Draw all the spites
        all_sprites_list.draw(screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 20 frames per second
        clock.tick(60)

    pygame.quit()
