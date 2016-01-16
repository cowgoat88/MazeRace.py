'''
MAZE RACE
'''

import random

'''
SETUP GLOBALS
'''
size = 10
board = [[0 for x in xrange(size)] for y in xrange(size)]



'''
INITIALIZE A PLAYABLE BOARD
v1.0
'''
def init_board(size):
	
	for x in xrange(size):
		for y in xrange(size):
			board[x][y] = random.choice([0,0,0,1])	# RANDOM CHOICE FROM 
	board[size-1][size-1] = 2
	return board


board = init_board(size)
for x in board:
	print x


def search(x, y):
	if board[x][y] == 2:
		print 'found at %d, %d' % (x, y)
		return True
	elif board[x][y] == 1:
		print 'wall at %d, %d' % (x, y)
		return False
	elif board[x][y] == 3:
		print 'visited %d, %d' % (x, y)
		return False
	
	print 'visiting %d, %d' % (x, y)
	
	# mark as visited
	board [x][y] = 3
	
	# explore neighbors clockwise starting on the right
	if ((x < len(board) -1 and search(x+1, y))
		or (y > 0 and search(x, y-1))
		or (x > 0 and search(x-1, y))
		or (y < len(board)-1 and search(x, y+1))):
		return True
	return False
	


'''
CLASS "PLAYER" PLAYS THROUGH BOARD TO FINISH CONDITION
v0.0
'''			
class player():
	
	def __init__(self):
		self.position = [0,0] # Start position.
		
	moves = {
		'w':[0,1],
		'a':[-1,0],
		's':[0,-1],
		'd':[1,0]
		}	
		
	def player_move(self):
		
		moves = {
			'w':[0,1],
			'a':[-1,0],
			's':[0,-1],
			'd':[1,0]
			}	
		
		move = raw_input('MOVE : ',)
		try:
			self.position = [sum(x) for x in zip(self.position,moves[move])]
			if self.position <= size:
				pass
			else:
				print 'EDGE!'
		except KeyError:
			print 'Invalid KEY!'
			self.player_move()
			
	
	def position(self):
		return self.position
		
		
		

'''
INITIALIZE PLAYER
'''
wilder = player()

'''
MAIN LOOP
prototype v0.0
'''
WIN = False
while WIN == False:

	wilder.player_move()
	print wilder.position
	if board[wilder.position[0]][wilder.position[1]]== 2:
		WIN = True
		print 'You found the exit! You won a Maze Race!'
	
