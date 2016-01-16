'''
MAZE RACE
v1.1
'''

import random

'''
SETUP GLOBALS
v1.0
'''
SIZE = 10
board = [[0 for x in xrange(SIZE)] for y in xrange(SIZE)]
moves = {
		'w':[-1,0],
		'a':[0,-1],
		's':[1,0],
		'd':[0,1]
		}


'''
INITIALIZE A PLAYABLE BOARD
v1.4
'''
def init_board(SIZE):
	
	for x in xrange(SIZE):
		for y in xrange(SIZE):
			board[x][y] = [random.choice([0,1]),'u']	# RANDOM CHOICE and UNEXPLORED ='u'
	board[SIZE-1][SIZE-1] = [2,'u']
	return board

def reformat_board(board):
	
	for x in xrange(SIZE):
		for y in xrange(SIZE):
			if board[x][y][0] == 3:
				board[x][y][0] = 0
	return board


def search(x, y):
	if board[x][y][0] == 2:
		return True
	elif board[x][y][0] == 1:
		return False
	elif board[x][y][0] == 3:
		return False
		
	board[x][y][0] = 3 	# mark as visited

	# explore neighbors clockwise starting on the right
	if ((x < len(board) -1 and search(x+1, y)) 	

		or (y > 0 and search(x, y-1))
		or (x > 0 and search(x-1, y))
		or (y < len(board)-1 and search(x, y+1))):
		return True
	return False
	

'''
CLASS "PLAYER" PLAYS THROUGH BOARD TO FINISH CONDITION
v0.1
'''			
class player():
	
	def __init__(self):
		self.position = [0,0] # Start position.	
		
	def position(self):
		return self.position
	
	def is_valid_move(self,move): 	# Validation for moves

		
		
		pos = [sum(x) for x in zip(self.position,moves[move])]
		
		board[pos[0]][pos[1]][1] = 'e' 		# Mark as explored for rendering fog of war

		
		if pos[0] <= SIZE-1 and pos[0] >= 0: 		# Test if position is in the board

			pass
		else:
			return False
		if pos[1] <= SIZE-1 and pos[1] >= 0:
			pass
		else:
			return False
		
		if board[pos[0]][pos[1]][0] == 1: 		# Check if wall or not

			return False
		return True 		# If all conditions met, return True 

	
	def player_move(self):
		render_board(board,wilder.position)
		move = raw_input('\nMOVE : ',)
		try:
			if self.is_valid_move(move) == True: # Check if valid move and change position
				self.position = [sum(x) for x in zip(self.position,moves[move])]
			else:
				print 'Invalid MOVE!',
				self.player_move()
		
		except KeyError:
			print 'Invalid KEY!',
			self.player_move()
			
	
	
		
		
'''
RENDER FOG OF WAR MAZE MAP
v1.0
'''
def render_board(board,player_pos):
	
	for x in xrange(SIZE):
		print '\n'
		for y in xrange(SIZE):
			if 	[x,y] == player_pos:
				print '+',
			elif board[x][y][1] == 'e':
				print board[x][y][0],
			else:
				print '-',
			


'''
MAIN LOOP
prototype v0.3
'''
# Loop for generating a valid map
good_board = False
while good_board == False:
	init_board(SIZE)
	if search(0,0) == True:
		good_board = True
board = reformat_board(board)


wilder = player()
WIN = False
while WIN == False:
	wilder.player_move()
	if board[wilder.position[0]][wilder.position[1]][0]== 2:
		WIN = True
		render_board(board,wilder.position)
		print 'You found the exit! You won a Maze Race!'
	
	
	
	
	
