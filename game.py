import pygame,sys
import random

#basic step
pygame.init()
screen=pygame.display.set_mode((850,750))
pygame.display.set_caption("Memory Game")
icon = pygame.image.load('Assets/one.png')
pygame.display.set_icon(icon)

#time
current_time=0
clock=pygame.time.Clock()

#this is initial input from user in interface
user_input_num = ''
#Saved output from game
num_string = ''
#user output for game
user_input_string = ''
#basic font
font= pygame.font.Font("Snap.ttf",65)
#score
score=0
#global state
state=0

class Rand_nums():
    def __init__(self):
        # falling numbers design
        # basic font
        font = pygame.font.Font("Snap.ttf", 50)

        self.numbers = [
            [-10, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-100, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-200, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-300, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-400, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-500, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-600, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-700, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-800, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))],
            [-900, random.randint(30, 790), font.render(str(random.randint(0, 9)), True, pygame.Color('white'))]
        ]

        # fallign speed
        self.fall_speed = 1

    def fall(self):
        # falling numbers 10 numbers at a time
        for i, number in enumerate(self.numbers):
            if number[0] > 750:
                self.change_num(i)
            screen.blit(number[2], (number[1], number[0]))
            number[0] += self.fall_speed

    def change_num(self,i):
        self.numbers[i][0]=i*-30
        self.numbers[i][1]=random.randint(30,800)
        self.numbers[i][2]=font.render(str(random.randint(0,9)), True, pygame.Color('white'))

class Interface():
    def __init__(self):
        # start button
        self.start_button = pygame.Rect(300, 330, 230, 80)
        self.start_color = pygame.Color('white')

        #text rect
        self.text_rect = pygame.Rect(300, 430, 230, 80)

        #check if text box is selected
        self.can_write=False

        #rand nums
        self.rand_nums=Rand_nums()

        #input error bool variable
        self.input_error = False

    def draw(self):

        #game title
        self.title()

        pygame.draw.rect(screen, self.start_color, self.start_button)
        pygame.draw.rect(screen, pygame.Color('white'), self.text_rect, 2)

        text_start = font.render("Start", True, pygame.Color('black'))
        text_input = font.render(user_input_num, True, pygame.Color('white'))

        screen.blit(text_start, (self.start_button.x + 5, self.start_button.y + 5))
        screen.blit(text_input, (self.text_rect.x + 5, self.text_rect.y + 5))

        self.rand_nums.fall()

        if self.input_error:
            self.error()
        else:
            self.help()


    def title(self):

        font = pygame.font.Font("Snap.ttf", 80)

        title_1 = font.render("Remember", True, pygame.Color('white'))
        title_2 = font.render("The", True, pygame.Color('white'))
        title_3 = font.render("Number", True, pygame.Color('white'))

        screen.blit(title_1, (90, 50))
        screen.blit(title_2, (270, 130))
        screen.blit(title_3, (330, 210))

    def help(self):
        font_new = pygame.font.Font("Snap.ttf", 30)
        text_help = font_new.render("Enter the initial size of the pattern!", True, pygame.Color('white'))
        text_note = font_new.render("Note: can only be numbers of 3 digits", True, pygame.Color('white'))
        screen.blit(text_help, (self.text_rect.x - 220, self.text_rect.y + 140))
        screen.blit(text_note, (self.text_rect.x - 220, self.text_rect.y + 200))

    def error(self):
        font_new = pygame.font.Font("Snap.ttf", 30)
        text_error = font_new.render("You have to input a logical number to start", True, pygame.Color('red'))
        text_error2 = font_new.render("the game!", True, pygame.Color('red'))
        screen.blit(text_error, (self.text_rect.x - 270, self.text_rect.y + 140))
        screen.blit(text_error2, (self.text_rect.x + 10, self.text_rect.y + 200))

class Answer(Interface):
    def __init__(self):
        super().__init__()

        # start button
        self.check_button = pygame.Rect(300, 230, 230, 80)
        self.text_rect.y=330
        self.check_color = pygame.Color('white')

        self.text_rect.h = 50

        #variable to check if answer is correct or not
        self.wrong=False
        self.correct=False

        self.exit_rect= pygame.Rect(self.text_rect.x + 50,self.text_rect.y + 200, 230,80)
        self.reset_rect = pygame.Rect(self.text_rect.x  ,self.text_rect.y + 100, 230,80)

    def draw(self):
        
        font_2 = pygame.font.Font("Snap.ttf", 35)
        #fallign numbers
        self.rand_nums.fall()
        #start text
        check_text= font.render("Check",True,pygame.Color('black'))
        #input text
        input_text= font_2.render(user_input_string,True,pygame.Color('white'))

        #for flexible text box size
        self.text_rect.w=max(230,input_text.get_width())
        #drawing
        pygame.draw.rect(screen, self.check_color, self.check_button)
        pygame.draw.rect(screen, pygame.Color('white'), self.text_rect, 2)
        screen.blit(check_text, (self.check_button.x + 5, self.check_button.y + 5))
        screen.blit(input_text, (self.text_rect.x + 5, self.text_rect.y + 5))

        if self.input_error:
            self.error()

        if self.wrong==True:
            self.wrong_ans()

        if self.correct==True:
            correct_ans()

    def error(self):
        font_new = pygame.font.Font("Snap.ttf", 40)
        text_error = font_new.render("You have to input a number to", True,
                                        pygame.Color('red'))
        text_error2 = font_new.render("check your answer!", True,pygame.Color('red'))
        screen.blit(text_error, (self.text_rect.x - 230, self.text_rect.y + 140))
        screen.blit(text_error2, (self.text_rect.x - 110, self.text_rect.y + 180))

    def wrong_ans(self):

        font= pygame.font.Font("Snap.ttf",40)

        text_1 = font.render("Exit", True, pygame.Color('black'))
        text_2 = font.render("Play again", True, pygame.Color('black'))
        text_3 = font.render("Wrong Answer", True, pygame.Color('red'))

        self.exit_rect.w = text_1.get_width() + 10
        self.reset_rect.w=text_2.get_width() + 10

        pygame.draw.rect(screen, pygame.Color('white'), self.reset_rect)
        pygame.draw.rect(screen, pygame.Color('white'), self.exit_rect)
        screen.blit(text_2, (self.reset_rect.x + 5, self.reset_rect.y + 5))
        screen.blit(text_1, (self.exit_rect.x + 5, self.exit_rect.y + 5))
        screen.blit(text_3, (self.check_button.x - 20, self.check_button.y - 100))

def correct_ans():

    if current_time - main.time > 2000:
        main.state=2
    font = pygame.font.Font("Snap.ttf", 40)
    text = font.render("Correct Answer", True, pygame.Color('Green'))
    screen.blit(text, (main.answer.reset_rect.x - 25, main.answer.reset_rect.y + 5))
class Main():
    def __init__(self):

        #game state
        self.state=0
        self.time=0

        #Interface at state = 0
        self.interface=Interface()

        #Count down at state = 1
        self.count=1
        #Game at state = 2
        self.repeat = 0
        self.rand_num = random.randint(1, 9)
        self.rand_x = random.randint(50, 750)
        self.rand_y = random.randint(50, 600)
        #Answer check at state = 3
        self.answer=Answer()

    def draw(self):
        global user_input_string
        global num_string

        if self.state==0: #Interface
            self.interface.draw()
        elif self.state==1: #Count down
            self.count_down()
        elif self.state==2: #Game start
            if self.answer.correct:
                self.answer.correct=False
                user_input_string=''
                num_string=''
            self.game_start()
        elif self.state==3:
            self.answer.draw()

    def count_down(self):
        if self.count == 3 and current_time - self.time > 1000:
            self.count=1
            self.state=2
            return

        if current_time - self.time > 1000:
            self.count+=1
            self.time=current_time

        font = pygame.font.Font("Snap.ttf", 80)
        if self.count ==3:
            text = font.render(f"{self.count}...GO!", True, pygame.Color('red'))
            screen.blit(text, (310, 300))
        else:
            text = font.render(str(self.count), True, pygame.Color('white'))
            screen.blit(text, (400, 300))

    def game_start(self):
        global user_input_num
        global num_string
        if self.repeat == int(user_input_num) and current_time - self.time > 1200:
            self.repeat=0
            user_input_num= str( int(user_input_num) + 1)
            self.state = 3
            self.time=current_time
            return

        if current_time - self.time > 1200 and self.repeat!= int(user_input_num):
            self.rand_num=random.randint(0,9)
            self.rand_x = random.randint(50,750)
            self.rand_y = random.randint(50,600)
            self.time= current_time
            num_string += str(self.rand_num)
            self.repeat+=1

        #Show rand num
        font = pygame.font.Font("Snap.ttf", 70)
        text = font.render(str(self.rand_num), True, pygame.Color('white'))
        if self.repeat :
        	screen.blit(text, (self.rand_x, self.rand_y))
        # Show score
        font = pygame.font.Font("Snap.ttf", 30)
        text = font.render(f"Score: {score}", True, pygame.Color('white'))
        screen.blit(text, (5, 0))

    def reset(self):
        self.__init__()


def Zaid():
	font=pygame.font.Font("Snap.ttf",25)
	text1=font.render("Zaid Ibaisi",True,pygame.Color('yellow'))
	text2=font.render("19290199",True,pygame.Color('yellow'))
	screen.blit(text1,(3,680))
	screen.blit(text2,(3,710))
#main game
main=Main()

#running status
running = True

#Game loop
while running:

    for event in pygame.event.get():
        #Mouse position
        pos= pygame.mouse.get_pos()

        #to quit
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        #MOUSE PRESSING
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if you select text box for interface
            if main.interface.text_rect.collidepoint(pos):
                main.interface.can_write=True
            else:
                main.interface.can_write = False
            #select text box for answer page
            if main.answer.text_rect.collidepoint(pos):
                main.answer.can_write=True
            else:
                main.answer.can_write = False

            #if you press on start button
            if main.interface.start_button.collidepoint(pos) and main.state==0:
                if user_input_num=='' or user_input_num[0]=='0':
                    main.interface.input_error = True
                    main.interface.start_color=pygame.Color('red')
                else:
                    main.interface.input_error = False
                    main.time = current_time
                    main.state=1
            #press on answer button
            if main.answer.check_button.collidepoint(pos) and main.state==3 and main.answer.correct==False and main.answer.wrong==False:
                if user_input_string=='':
                    main.answer.input_error = True
                    main.answer.check_color=pygame.Color('red')
                else:
                    main.answer.input_error = False
                    if user_input_string == num_string:
                        score+=1
                        main.time=current_time
                        main.answer.correct= True
                        main.answer.time = current_time
                    else:
                        main.answer.wrong=True

            #play again
            if main.answer.reset_rect.collidepoint(pos) and main.answer.wrong and main.state==3:
                main.reset()
                user_input_string = ''
                user_input_num = ''
                num_string = ''
                score = 0

            #exit
            if main.answer.exit_rect.collidepoint(pos) and main.answer.wrong and main.state==3:
                running=False
                sys.exit()

        # MOUSE HOVERING
        if event.type == pygame.MOUSEMOTION:
            #if you hover over start button
            if main.interface.start_button.collidepoint(pos):
                main.interface.start_color=pygame.Color('grey')
            else:
                main.interface.start_color = pygame.Color('white')
            # if you hover over check button
            if main.answer.check_button.collidepoint(pos):
                main.answer.check_color=pygame.Color('grey')
            else:
                main.answer.check_color = pygame.Color('white')

        # Pressing keys
        if event.type == pygame.KEYDOWN:
            #writing in a text box
            if main.interface.can_write and main.state==0:
                #check if its numbers only
                if event.unicode.isnumeric():
                    #cant be more than 3 numbers
                    if len(user_input_num)<3:
                        user_input_num+=event.unicode
                #back spacing
                if event.key==pygame.K_BACKSPACE:
                    user_input_num=user_input_num[0:-1]
                #enter button: same as pressing with mouse
                if event.key==pygame.K_RETURN:
                    if user_input_num == '' or user_input_num[0]=='0':
                        main.interface.input_error=True
                        main.interface.start_color = pygame.Color('red')
                    else:
                        main.time=current_time
                        main.interface.input_error = False
                        main.state=1

            #writing in answer text box
            if main.answer.can_write and main.state==3 and main.answer.correct==False and main.answer.wrong==False:
                if event.unicode.isnumeric():
                    user_input_string+=event.unicode
                if event.key==pygame.K_BACKSPACE:
                    user_input_string=user_input_string[0:-1]
                if event.key==pygame.K_RETURN:
                        if user_input_string == '':
                            main.answer.input_error = True
                            main.answer.check_color = pygame.Color('red')
                        else:
                            main.answer.input_error = False
                            if user_input_string == num_string:
                                score+=1
                                main.answer.correct = True
                                main.time=current_time
                            else:
                                main.answer.wrong = True


    current_time = pygame.time.get_ticks()
    screen.fill((0,0,0))
    Zaid()
    main.draw()
    pygame.display.update()
    clock.tick(60)




