'''
MAZE RACE
v1.k 
working board render
needs conditional movment
'''
import random

'''
SETUP GLOBALS
'''
size = 10
board = [[0 for x in xrange(size)] for y in xrange(size)]



'''
INITIALIZE A PLAYABLE BOARD
v1.2
'''
def init_board(size):
	
	for x in xrange(size):
		for y in xrange(size):
			board[x][y] = [random.choice([0,1]),'u']	# RANDOM CHOICE and UNEXPLORED ='u'
	board[size-1][size-1] = [2,'u']
	return board




def search(x, y):
	if board[x][y][0] == 2:
		return True
	elif board[x][y][0] == 1:
		return False
	elif board[x][y][0] == 3:
		return False
		
	# mark as visited
	board[x][y][0] = 3
	
	# explore neighbors clockwise starting on the right
	if ((x < len(board) -1 and search(x+1, y))
		or (y > 0 and search(x, y-1))
		or (x > 0 and search(x-1, y))
		or (y < len(board)-1 and search(x, y+1))):
		return True
	return False
	
good_board = False

while good_board == False:
	init_board(size)
	if search(0,0) == True:
		good_board = True
	

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
			'w':[-1,0],
			'a':[0,-1],
			's':[1,0],
			'd':[0,1]
			}	
		
		move = raw_input('\nMOVE : ',)
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
RENDER FOG OF WAR MAZE
'''
def render_board(board,player_pos):
	
	for x in xrange(size-1):
		print '\n'
		for y in xrange(size-1):
			if 	[x,y] == player_pos:
				print '+',
			elif board[x][y][1] == 'e':
				print board[x][y][0],
			else:
				print '-',
			


'''
MAIN LOOP
prototype v0.1
'''

wilder = player()


board = init_board(size)
WIN = False
while WIN == False:
	render_board(board,wilder.position)
	wilder.player_move()
	if board[wilder.position[0]][wilder.position[1]]== 2:
		WIN = True
		print 'You found the exit! You won a Maze Race!'
	
	
	
	
	
