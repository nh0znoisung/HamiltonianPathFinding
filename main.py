#-----------------
#Importing modules
#-----------------
import pygame
import time
from pygame.locals import *
import os
from datetime import date, datetime
#---------------------
#Global variables
#---------------------
width = 600 # horizontal
height = 800 # vertical

WHITE = (255,255,255) # no
BLACK = (0,0,0) # background
RED = (255,0,0) # end
BLUE = (0, 0, 255) #line
PINK = (204, 0, 255) # start
GREEN = (0, 255, 140) # node
BLUE_LIGHT = (40, 53, 88) # menu
YELLOW = (255, 255, 0) # title
YELLOW_LIGHT = (255,255,51)
RED_LIGHT = (150, 0, 0)
GRAY_LIGHT = (211,211,211)
GREEN_DARK = (0, 255, 0)
BROWN = (210,105,30)
ORANGE = '#ff631c'

scale = 0.05

x_amount, y_amount = 3, 4 # from 1 to 99
x_delta, y_delta = width/y_amount, height/x_amount
x_offset, y_offset = x_delta/2, y_delta/2
radius = min(x_delta, y_delta)/4

board = [[0 for i in range(y_amount)] for j in range(x_amount)] # string to int
visited = [[False if i == 1 else False for i in row] for row in board]

done = False
edges = []
count = 0
all_1 = False
all_2 = False
empty_obstacle = True
mute = False # mute or unmute
flag = 1
step = 1
start_point = []
end_point = []
board_rect = []
obstacle_list = []
accepted = []
pass_it = 1
time_took = 0
tic = 0
toc = 0

def reset_variable():
	global x_amount, y_amount, x_delta, y_delta, x_offset, y_offset, radius, board, visited, done, edges, count, all_1, all_2, empty_obstacle, mute, flag, step, start_point, end_point, board_rect, obstacle_list, accepted, pass_it, tic, toc, time_took
	x_amount, y_amount = 3, 4 # from 1 to 99
	x_delta, y_delta = width/y_amount, height/x_amount
	x_offset, y_offset = x_delta/2, y_delta/2
	radius = min(x_delta, y_delta)/4
	board = [[0 for i in range(y_amount)] for j in range(x_amount)] # string to int
	visited = [[False if i == 1 else False for i in row] for row in board]

	done = False
	edges = []
	count = 0
	all_1 = False
	all_2 = False
	empty_obstacle = True
	mute = False # mute or unmute
	flag = 1
	step = 1
	start_point = []
	end_point = []
	board_rect = []
	obstacle_list = []
	accepted = []
	pass_it = 1
	time_took = 0
	tic = 0
	toc = 0



def reset_data():
	global x_amount, y_amount, x_delta, y_delta, x_offset, y_offset, radius, board, visited
	x_delta, y_delta = width/y_amount, height/x_amount
	x_offset, y_offset = x_delta/2, y_delta/2
	radius = min(x_delta, y_delta)/4
	board = [[0 for i in range(y_amount)] for j in range(x_amount)] # string to int
	visited = [[False if i == 1 else False for i in row] for row in board]

# board_str = '010-000-000-000' # use this for obstacle



#---------------------
#Initializing the game
#---------------------
pygame.init()
surface = pygame.display.set_mode((1000,800))
pygame.display.set_caption("5x5 puzzle")
font = pygame.font.SysFont('calibri', 20)

up_arrow = pygame.image.load("Assets/up_arrow.png")
up_arrow = pygame.transform.scale(up_arrow, (20, 20))

down_arrow = pygame.image.load("Assets/down_arrow.png")
down_arrow = pygame.transform.scale(down_arrow, (20, 20))

#144, 60

start_button = pygame.image.load("Assets/start.png")
start_button = pygame.transform.scale(start_button, (144, 60))

refresh_button = pygame.image.load("Assets/refresh.png")
refresh_button = pygame.transform.scale(refresh_button, (144, 60))

pick_button = pygame.image.load("Assets/choose.png")
pick_button = pygame.transform.scale(pick_button, (105, 43))

# skip_button = pygame.image.load("skip.png")
# skip_button = pygame.transform.scale(skip_button, (105, 43))
red_pink = pygame.image.load("Assets/red_pink.png")

exit_button = pygame.image.load("Assets/exit.png")
exit_button = pygame.transform.scale(exit_button, (180, 54))

continue_button = pygame.image.load("Assets/continue.png")
continue_button = pygame.transform.scale(continue_button, (180, 54))
# 3.03

mute_button = pygame.image.load("Assets/mute.png")
mute_button = pygame.transform.scale(mute_button, (45, 45))

unmute_button = pygame.image.load("Assets/unmute.png")
unmute_button = pygame.transform.scale(unmute_button, (45, 45))

icon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icon)

save_icon = pygame.image.load("Assets/save_icon.png")
save_icon = pygame.transform.scale(save_icon, (35, 35))
#----------------
#Making the fonts
#----------------
menuFont = pygame.font.SysFont("CopperPlate Gothic", 80, bold = True)  
gridFont = pygame.font.SysFont("Calibri", 50, bold = True)              
rowFont = pygame.font.SysFont("Comic Sans MS", 60, bold = True)          
colFont = pygame.font.SysFont("Comic Sans MS", 60, bold = True)         
xFont = pygame.font.SysFont("CopperPlate Gothic", 50, bold = True) 

helpFont = pygame.font.SysFont("Comic Sans MS", 25)            

statusFont = pygame.font.SysFont("CopperPlate Gothic",25)    
# msgFont = pygame.font.SysFont("CopperPlate Gothic",25)        
buttonFont = pygame.font.SysFont("CopperPlate Gothic", 18, bold = True)          

#-----------------
#Making the sound
mouse_click_sound = pygame.mixer.Sound("Assets/mouse_click.mp3")
mouse_click_sound.set_volume(0.35)
blue_switch_sound = pygame.mixer.Sound("Assets/blue_switch.mp3")
blue_switch_sound.set_volume(0.275)
# error_sound = pygame.mixer.Sound("Assets/error.mp3")
#-----------------

def click_menu():
	pygame.mixer.Sound.play(mouse_click_sound)
	pygame.mixer.music.stop()

def click_board():
	pygame.mixer.Sound.play(blue_switch_sound)
	pygame.mixer.music.stop()

# def click_error():
# 	pygame.mixer.Sound.play(blue_switch_sound)
# 	pygame.mixer.music.stop()

#-----------------
#Setting the icon
#-----------------
# pygame.display.set_icon(icon)

#---------
#The Clock
#---------
clock =  pygame.time.Clock()	
FPS = 30
FPS_RUN = 10


def display_title():
    menuText = menuFont.render("MENU", True, ORANGE)
    surface.blit(menuText, [600 + 70, 0 + 20])



def check_one_digit(n):
	if len(str(n)) == 1:
		return True
	return False

def display_row_num(f = False):
	# Check if 2 digits
	if f == False:
		rowText = rowFont.render(f"{x_amount}", True, GRAY_LIGHT)
		if check_one_digit(x_amount):
			surface.blit(rowText, [600 + 30, 0 + 150])
		else:
			surface.blit(rowText, [600 + 10, 0 + 150])
	else:
		rowText = rowFont.render(f"{x_amount}", True, RED)
		if check_one_digit(x_amount):
			surface.blit(rowText, [600 + 80, 0 + 150])
		else:
			surface.blit(rowText, [600 + 60, 0 + 150])


up_arrow_row = Rect(600 + 85, 0 + 170, 20, 20)
down_arrow_row = Rect(600 + 85, 0 + 205, 20, 20)

up_arrow_col = Rect(600 + 255, 0 + 170, 20, 20)
down_arrow_col = Rect(600 + 255, 0 + 205, 20, 20)

def display_up_arrow_row():
	surface.blit(up_arrow, [600 + 85, 0 + 170])

def display_down_arrow_row():
	surface.blit(down_arrow, [600 + 85, 0 + 205])

def display_col_num(f = False):
	# Check if 2 digits
	if f == False:
		rowText = rowFont.render(f"{y_amount}", True, GRAY_LIGHT)
		if check_one_digit(y_amount):
			surface.blit(rowText, [600 + 200, 0 + 150])
		else:
			surface.blit(rowText, [600 + 180, 0 + 150])
	else:
		rowText = rowFont.render(f"{y_amount}", True, RED)
		if check_one_digit(y_amount):
			surface.blit(rowText, [600 + 270, 0 + 150])
		else:
			surface.blit(rowText, [600 + 250, 0 + 150])	



def display_up_arrow_col():
	surface.blit(up_arrow, [600 + 255, 0 + 170])

def display_down_arrow_col():
	surface.blit(down_arrow, [600 + 255, 0 + 205])

def display_x(f = False):
	if f == False:
		xText = xFont.render("X", True, RED)
		surface.blit(xText, [600 + 127, 0 + 170])
	else:
		xText = xFont.render("X", True, GREEN)
		surface.blit(xText, [600 + 177, 0 + 170])


pick_rect = Rect(600 + 290, 0 + 175, 105, 43)

def display_pick_button():
	surface.blit(pick_button, [600 + 290, 0 + 175])

refresh_rect = Rect(600 + 220, 0 + 440, 144, 60)
start_rect = Rect(600 + 25, 0 + 440, 144, 60)
def display_start_button():
	surface.blit(start_button, [600 + 25, 0 + 440])

def display_refresh_button():
	surface.blit(refresh_button, [600 + 220, 0 + 440])


exit_rect = Rect(600 + 205, 0 + 695, 180, 54)
continue_rect = Rect(600 + 10, 0 + 695, 180, 54)
mute_rect = Rect(600 + 335, 0 + 755, 45, 45)
save_rect = Rect(600 + 350, 0 + 585, 35, 35)

def display_continue_button():
	surface.blit(continue_button, [600 + 10, 0 + 695])

def display_exit_button():
	surface.blit(exit_button, [600 + 205, 0 + 695])

def display_mute_button(done = 0):
	# 0: unmute, 1: mute
	if done == 0:
		surface.blit(unmute_button, [600 + 335, 0 + 755])
	else:
		surface.blit(mute_button, [600 + 335, 0 + 755])

def display_save_icon():
	surface.blit(save_icon, [600 + 350, 0 + 585])


def display_step_1(color = RED):
	step1Text = helpFont.render("1. Choose your grid", True, color)
	surface.blit(step1Text, [600 + 10, 0 + 120])

def display_step_2(color = RED):
	step2Text = helpFont.render("2. Choose the start point", True, color)
	surface.blit(step2Text, [600 + 10, 0 + 245])

def display_step_3(color = RED):
	step3Text = helpFont.render("3. Choose the end point", True, color)
	surface.blit(step3Text, [600 + 10, 0 + 295])

def display_step_4(color = RED):
	step4Text = helpFont.render("4. Choose the obstacles", True, color)
	surface.blit(step4Text, [600 + 10, 0 + 345])

def display_step_5(color = RED):
	step5Text = helpFont.render("5. Start algorithm or Refresh ", True, color)
	surface.blit(step5Text, [600 + 10, 0 + 395])

def display_step_6(color = RED):
	step6Text = helpFont.render("6. Result", True, color)
	surface.blit(step6Text, [600 + 10, 0 + 510])

def display_step_7(color = RED):
	step7Text = helpFont.render("7. Continue or Exit", True, color)
	surface.blit(step7Text, [600 + 10, 0 + 650])

def display_result_frame(color = BROWN):
	statusText = helpFont.render("Status:", True, color)
	attemptedText = helpFont.render("Attempted:", True, color)
	timeText = helpFont.render("Time: ", True, color)
	surface.blit(statusText, [600 + 60, 0 + 550])
	surface.blit(attemptedText, [600 + 60, 0 + 580])
	surface.blit(timeText, [600 + 60, 0 + 610])

def display_result_text(status = -1, attempted = '', time = 0):
	# status: 0 = Finding..., 1: No solution, 2: Successful
	# attempted: How many times does it reach end point
	# Time: tic-toc
	status_str = ""
	if status == -1:
		status_str = ""
		status_col = YELLOW
	if status == 0:
		status_str = "Finding . . ."
		status_col = (255,255,51)
	elif status == 1:
		status_str = "No solution"
		status_col = RED
	elif status == 2:
		status_str = "Successful"
		status_col = GREEN_DARK
	statusText = statusFont.render(f"{status_str}", True, status_col)
	attemptedText = helpFont.render(f"{attempted}", True, GREEN_DARK)


	timeText = helpFont.render("{:0.5f} s".format(time), True, GREEN_DARK)
	surface.blit(statusText, [600 + 185, 0 + 555])
	surface.blit(attemptedText, [600 + 230, 0 + 580])
	surface.blit(timeText, [600 + 190, 0 + 610])


def display_skip_button(type = 0, done = 0):
	# Type 0: if obstacle =0 
	if type == 0:
		if done == 0:
			pygame.draw.rect(surface, GRAY_LIGHT, pygame.Rect(600 + 298, 0 + 345, 98, 43),  0, 3)
			step7Text = buttonFont.render("SKIP IT ?", True, BLACK)
			surface.blit(step7Text, [600 + 303, 0 + 354])
		else:
			pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 302, 0 + 345, 98, 43),  0, 3)
			step7Text = buttonFont.render("SKIPPED", True, ORANGE)
			surface.blit(step7Text, [600 + 306, 0 + 354])
	else:
		if done == 0:
			pygame.draw.rect(surface, GRAY_LIGHT, pygame.Rect(600 + 300, 0 + 345, 98, 43),  0, 3)
			step7Text = buttonFont.render("PICK IT ?", True, BROWN)
			surface.blit(step7Text, [600 + 304, 0 + 354])
		else:
			pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 308, 0 + 345, 90, 43),  0, 3)
			step7Text = buttonFont.render("PICKED", True, GRAY_LIGHT)
			surface.blit(step7Text, [600 + 315, 0 + 354])
	pygame.display.flip()


skip_rect = Rect(600 + 290, 0 + 345, 105, 43)
all_1_rect = Rect(600 + 315, 0 + 245, 80, 43)
all_2_rect = Rect(600 + 315, 0 + 295, 80, 43)

def display_all_button(step = 1, type = 0, done = 0):
	# step = 1 or 2. 1 is step 2, 2 is step 3
	# type = 0: not choose All, type = 1: Choose All
	if step == 1:
		if type == 0:
			if done == 1:
				pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 310, 0 + 245, 88, 43),  0, 3)
				step7Text = buttonFont.render("PICKED", True, PINK)
				surface.blit(step7Text, [600 + 317, 0 + 254])
		else:
			if done == 0:
				pygame.draw.rect(surface, GRAY_LIGHT, pygame.Rect(600 + 315, 0 + 245, 80, 43),  0, 3)
				step7Text = buttonFont.render("ALL ?", True, BLACK)
				surface.blit(step7Text, [600 + 325, 0 + 254])
			else:
				pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 315, 0 + 245, 80, 43),  0, 3)
				step7Text = buttonFont.render("ALL", True, GREEN_DARK)
				surface.blit(step7Text, [600 + 330, 0 + 254])
	else:
		if type == 0:
			if done == 1:
				pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 310, 0 + 295, 88, 43),  0, 3)
				step7Text = buttonFont.render("PICKED", True, RED)
				surface.blit(step7Text, [600 + 317, 0 + 304])
		else:
			if done == 0:
				pygame.draw.rect(surface, GRAY_LIGHT, pygame.Rect(600 + 315, 0 + 295, 80, 43),  0, 3)
				step7Text = buttonFont.render("ALL ?", True, BLACK)
				surface.blit(step7Text, [600 + 325, 0 + 304])
			else:
				pygame.draw.rect(surface, BLACK, pygame.Rect(600 + 315, 0 + 295, 80, 43),  0, 3)
				step7Text = buttonFont.render("ALL", True, GREEN_DARK)
				surface.blit(step7Text, [600 + 330, 0 + 304])
	pygame.display.flip()




####################
#Set-up Rectangle
####################


def display_step_1_content(f = True):
	if f == False:
		display_row_num()
		display_up_arrow_row()
		display_down_arrow_row()
		display_x()
		display_col_num()
		display_up_arrow_col()
		display_down_arrow_col()
		display_pick_button()
	else:
		display_row_num(True)
		display_x(True)
		display_col_num(True)


def draw_menu():
	global x_amount, y_amount, step, end_point, start_point, empty_obstacle, all_2, all_1, obstacle_list, time_took, accepted, tic, toc, mute
	pygame.draw.rect(surface, BLUE_LIGHT, [600, 0, 1000, 800])
	display_title()
	if mute:
		display_mute_button(1)
	else:
		display_mute_button()

	if step == 1:
		display_step_1_content(False)

		display_step_1(YELLOW) 
		display_step_2()
		display_step_3()
		display_step_4()
		display_step_5()
		display_step_6()
		display_step_7()


	if step == 2:
		display_step_1_content()

		display_step_1(GREEN_DARK) 
		display_step_2(YELLOW)
		display_step_3()
		display_step_4()
		display_step_5()
		display_step_6()
		display_step_7()

		display_all_button(1, 1, 0)

	if step == 3:
		display_step_1_content()
		display_step_1(GREEN_DARK) 
		display_step_2(GREEN_DARK)
		display_step_3(YELLOW)
		display_step_4()
		display_step_5()
		display_step_6()
		display_step_7()

		if all_1:
			display_all_button(1, 1, 1)
		else:
			display_all_button(1, 0, 1)

		display_all_button(2, 1, 0)
	if step == 4:
		display_step_1_content()
		display_step_1(GREEN_DARK) 
		display_step_2(GREEN_DARK)
		display_step_3(GREEN_DARK)
		display_step_4(YELLOW)
		display_step_5()
		display_step_6()
		display_step_7()

		if all_1:
			display_all_button(1, 1, 1)
		else:
			display_all_button(1, 0, 1)
		
		if all_2:
			display_all_button(2, 1, 1)
		else:
			display_all_button(2, 0, 1)

		if len(obstacle_list) == 0:
			display_skip_button(0,0)
		else:
			display_skip_button(1,0)
	if step == 5:
		display_step_1_content()
		display_step_1(GREEN_DARK) 
		display_step_2(GREEN_DARK)
		display_step_3(GREEN_DARK)
		display_step_4(GREEN_DARK)
		display_step_5(YELLOW)
		display_step_6()
		display_step_7()


		if all_1:
			display_all_button(1, 1, 1)
		else:
			display_all_button(1, 0, 1)
		
		if all_2:
			display_all_button(2, 1, 1)
		else:
			display_all_button(2, 0, 1)

		if empty_obstacle:
			display_skip_button(0, 1)
		else:
			display_skip_button(1, 1)

	if step == 6:
		display_step_1_content()
		display_step_1(GREEN_DARK) 
		display_step_2(GREEN_DARK)
		display_step_3(GREEN_DARK)
		display_step_4(GREEN_DARK)
		display_step_5(GREEN_DARK)
		display_step_6(YELLOW)
		display_step_7()

		if all_1:
			display_all_button(1, 1, 1)
		else:
			display_all_button(1, 0, 1)
		
		if all_2:
			display_all_button(2, 1, 1)
		else:
			display_all_button(2, 0, 1)

		if empty_obstacle:
			display_skip_button(0, 1)
		else:
			display_skip_button(1, 1)

		toc = time.time()
		time_took = toc - tic
		display_result_text(0, count, time_took) # status, attempted, time

	if step == 7:
		display_step_1_content()
		display_step_1(GREEN_DARK) 
		display_step_2(GREEN_DARK)
		display_step_3(GREEN_DARK)
		display_step_4(GREEN_DARK)
		display_step_5(GREEN_DARK)
		display_step_6(GREEN_DARK)
		display_step_7(YELLOW)

		if all_1:
			display_all_button(1, 1, 1)
		else:
			display_all_button(1, 0, 1)
		
		if all_2:
			display_all_button(2, 1, 1)
		else:
			display_all_button(2, 0, 1)

		if empty_obstacle:
			display_skip_button(0, 1)
		else:
			display_skip_button(1, 1)

		if len(accepted) == 0:
			display_result_text(1, count, time_took)
		else:
			display_result_text(2, count, time_took)
			display_save_icon()
	
	display_result_frame() 

	display_refresh_button()
	display_start_button()

	display_exit_button()
	display_continue_button()


	pygame.display.update()


def take_screenshot():
	global x_amount, y_amount, start_point, end_point
	today = date.today()
	now = datetime.now()
	d = today.strftime("%Y%m%d")
	current_time = now.strftime("%H%M%S")

	rect = pygame.Rect(0, 0, 600, 800)
	sub = surface.subsurface(rect)
	if not os.path.exists("Screenshots"):
		os.mkdir("Screenshots")

	pygame.image.save(sub, "Screenshots/{}_{}_{}x{}_({},{})_({},{}).png".format(d, current_time, x_amount, y_amount, start_point[0], start_point[1], end_point[0], end_point[1]))


def main():
	global done, flag, x_amount, y_amount, step, start_point, end_point, skip, all_1, all_2, visited, obstacle_list, empty_obstacle, mute
	while True:
		clock.tick(FPS_RUN)
		for event in pygame.event.get():
			keys_pressed = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys_pressed[pygame.K_q]:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				
		        # Set the x, y postions of the mouse click
				x, y = event.pos
				if mute_rect.collidepoint(x,y):
					if mute == 0:
						mute = 1
						flag = 1
					else: 
						mute = 0
						flag = 1
				if mute == 0:
					if x < 600:
						click_board()
					else:
						click_menu()


				if step == 1:
					if up_arrow_row.collidepoint(x, y):
						if x_amount < 99:
							x_amount += 1
							reset_data()
							flag = 1
					if down_arrow_row.collidepoint(x, y):
						if x_amount > 1:
							x_amount -= 1
							reset_data()
							flag = 1
					if up_arrow_col.collidepoint(x,y):
						if y_amount < 99:
							y_amount += 1
							reset_data()
							flag = 1
					if down_arrow_col.collidepoint(x,y):
						if y_amount > 1:
							y_amount -=1
							reset_data()					
							flag = 1
					if pick_rect.collidepoint(x,y):
						step = 2
						flag = 1
				
				if step == 2:
					if x < 600:
						if check_board_rect(x,y) != []:
							flag = 1
							[i,j] = check_board_rect(x,y)
							start_point = [i, j]
							step = 3
							continue
					else:
						if all_1_rect.collidepoint(x,y):
							flag = 1
							all_1 = True
							step = 3
							continue
				
				if step == 3:
					if x < 600:
						if check_board_rect(x,y) != []:
							[i,j] = check_board_rect(x,y)
							end_point = [i, j]
							flag = 1
							step = 4
							continue
					else:
						if all_2_rect.collidepoint(x,y):							
							all_2 = True
							flag = 1
							step = 4
							continue
				
				if step == 4:
					if x < 600:
						if check_board_rect(x,y) != []:
							[i,j] = check_board_rect(x,y)
							if [i,j] == start_point or [i,j] == end_point:
								continue
								#Warning sound
							else:
								if [i,j] in obstacle_list:
									obstacle_list.remove([i,j])
								else:
									obstacle_list.append([i,j])
								flag = 1
								continue
					else:
						if skip_rect.collidepoint(x,y):
							if len(obstacle_list) == 0:
								empty_obstacle = True
							else:
								empty_obstacle = False
							flag = 1
							step = 5
							continue

				if step == 5:
					if refresh_rect.collidepoint(x,y):
						reset_variable()
						flag = 1

					if start_rect.collidepoint(x,y):
						flag = 1
						step = 6
						flag = 1
						run(all_1, all_2)
						flag = 1
						step = 7
						flag = 1
						flag = 1
						flag = 1


				if step == 7:
					if save_rect.collidepoint(x,y):
						take_screenshot()
						flag = 1
					if exit_rect.collidepoint(x,y):
						pygame.quit()
						flag = 1
					if continue_rect.collidepoint(x,y):
						reset_variable()		
						flag = 1
		

		if flag:
			draw_board()
			flag = 0
	pygame.quit()



def center_point(X):
	# X: Tuple or list
	return ((X[1] * x_delta) + x_offset, (X[0] * y_delta) + y_offset)


def check_board_rect(x,y):
	global board_rect, x_amount, y_amount
	for i in range(x_amount):
		for j in range(y_amount):
			if board_rect[i][j].collidepoint(x,y):
				return [i,j]
	return []


def draw_board():
	global x_amount, y_amount, board_rect, start_point, end_point, red_pink, obstacle_list, visited

	board_rect = []
	pygame.draw.rect(surface, BLACK, [0, 0, 600, 800])
	
	draw_menu()
	if start_point == end_point:
		same = 1
	for i in range(x_amount):
		row_rect = []
		for j in range(y_amount):
			if [i,j] == start_point:
				color = PINK
			elif [i,j] == end_point:
				color = RED # red
			else:
				color = GREEN

			cell_rect = pygame.draw.circle(surface, color, center_point((i, j)), radius)
			row_rect.append(cell_rect)
		board_rect.append(row_rect)
	
	# start_point not identical end_point
	if start_point != [] and end_point != []:
		if start_point == end_point:
			[i, j] = start_point
			same_rect = board_rect[i][j]
			red_pink = pygame.transform.scale(red_pink, (same_rect.w, same_rect.h))
			surface.blit(red_pink, [same_rect.x, same_rect.y])

	# Draw obstacle
	for point in obstacle_list:
		pygame.draw.circle(surface, GRAY_LIGHT, center_point(point), radius)

	draw_edges(edges)
	pygame.display.flip()




def draw_line(X, Y, color = BLUE):
	pygame.draw.line(surface, color, center_point(X), center_point(Y), width = 10)

	if X[0] == Y[0]:
		# Horizontal
		if Y[1] > X[1]:
			up = (Y[0] - scale, Y[1] - scale)
			down = (Y[0] + scale, Y[1] - scale)

		else:
			up = (Y[0] - scale, Y[1] + scale)
			down = (Y[0] + scale, Y[1] + scale)

	if X[1] == Y[1]:
		if Y[0] > X[0]:
			up = (Y[0] - scale, Y[1] + scale)
			down = (Y[0] - scale, Y[1] - scale)
		else:
			up = (Y[0] + scale, Y[1] + scale)
			down = (Y[0] + scale, Y[1] - scale)

	pygame.draw.line(surface, color, center_point(Y), center_point(up), width = 10)
	pygame.draw.line(surface, color, center_point(Y), center_point(down), width = 10)
	pygame.display.flip()


def draw_edges(EDGES = edges):
	n = len(EDGES)
	if n < 2:
		return
	for i in range(n-1):
		draw_line(EDGES[i], EDGES[i+1])
	pygame.display.flip()



def reset_visited():
	visited = [[False if i == 1 else False for i in row] for row in board]


def check_visited():
	for i in range(x_amount):
		for j in range(y_amount):
			if visited[i][j] == False:
				return False
	return True

def is_safe():
	global end_point, visited
	[i,j] = end_point
	l = []
	if i > 0:
		l.append([i-1, j])
	if i < x_amount -1:
		l.append([i+1, j])
	if j > 0:
		l.append([i, j-1])
	if j < y_amount - 1:
		l.append([i, j+1])

	for [a,b] in l:
		if visited[a][b] == False:
			return True
	return False
	

# Algorithm: Backtracking
def dfs(point):
	global accepted, count, pass_it, visited

	[i,j] = point
	draw_board()
	clock.tick(FPS)
	if point == end_point:
		if pass_it:
			count += 1
			if check_visited() == True:
				# successfully
				# print("Successfully")
				accepted.append(edges)				
				return True
			else:
				return False
		else:
			pass_it = 1

	if is_safe() == False:
		if end_point not in [[i-1, j], [i+1, j], [i, j+1], [i, j-1]]:
			return False


	if i > 0 and visited[i-1][j] == False:
		visited[i-1][j] = True
		edges.append([i-1, j])
		if dfs([i-1,j]):
			return True
		edges.pop()
		visited[i-1][j] = False

	if j > 0 and visited[i][j-1] == False:
		visited[i][j-1] = True
		edges.append([i, j-1])
		if dfs([i,j-1]):
			return True
		edges.pop()
		visited[i][j-1] = False

	if i < x_amount - 1 and visited[i + 1][j] == False:
		visited[i+1][j] = True
		edges.append([i+1, j])
		if dfs([i+1,j]):
			return True
		edges.pop()
		visited[i+1][j] = False

	if j < y_amount - 1 and visited[i][j + 1] == False:
		visited[i][j+1] = True
		edges.append([i, j+1])
		if dfs([i,j+1]):
			return True
		edges.pop()
		visited[i][j+1] = False
	return False



def run(start_all = 0, end_all = 0):
	global visited, edges, start_point, end_point, pass_it, obstacle_list, time_took, tic, toc
	tic = time.time()
	for [i,j] in obstacle_list:
		visited[i][j] = True

	if start_all == 0 and end_all == 0:
		if start_point != end_point:
			visited[start_point[0]][start_point[1]] = True
			edges.append(start_point)
			dfs(start_point)
			visited[start_point[0]][start_point[1]] = False
		else:
			# find circuit
			pass_it = 0
			edges.append(start_point)
			dfs(start_point)

	elif start_all == 1 and end_all == 0:
		# Do circuit
		start_point = end_point
		pass_it = 0
		edges = []
		edges.append(start_point)
		res = dfs(start_point)
		
		if res == 0:
			pass_it = 1
			for i in range(x_amount * y_amount):
				if int_to_list(i) in obstacle_list:
					continue
				if end_point != int_to_list(i):
					start_point = int_to_list(i)
					visited[start_point[0]][start_point[1]] = True
					edges = []
					edges.append(start_point)
					ok = dfs(start_point)
					visited[start_point[0]][start_point[1]] = False
					if ok:
						break
	elif start_all == 0 and end_all == 1:
		# Do circuit
		end_point = start_point
		pass_it = 0
		edges = []
		edges.append(start_point)
		res = dfs(start_point)

		if res == 0:
			pass_it = 1
			for i in range(x_amount * y_amount):
				if int_to_list(i) in obstacle_list:
					continue
				if start_point != int_to_list(i):
					end_point = int_to_list(i)
					visited[start_point[0]][start_point[1]] = True
					edges = []
					edges.append(start_point)
					ok = dfs(start_point)
					visited[start_point[0]][start_point[1]] = False
					if ok:
						break

	elif start_all == 1 and end_all == 1:
		# Do only one circuit: do [0][0]
		start_point = [0,0]
		end_point = [0,0]
		pass_it = 0
		edges.append(start_point)
		res =  dfs(start_point)
		if res == 0:
			pass_it = 1
			for i in range(x_amount * y_amount):
				ok = 0
				if int_to_list(i) in obstacle_list:
					continue
				for j in range(i + 1, x_amount * y_amount):
					if int_to_list(j) in obstacle_list:
						continue
					print('{},{}'.format(i, j))
					start_point = int_to_list(i)
					end_point = int_to_list(j)
					visited[start_point[0]][start_point[1]] = True
					edges = []
					edges.append(start_point)
					ok = dfs(start_point)
					visited[start_point[0]][start_point[1]] = False
					if ok:
						break
				if ok:
					break

	toc = time.time()
	time_took = toc - tic

def int_to_list(n):
	global y_amount
	return [int(n/y_amount), n%y_amount]



main()



