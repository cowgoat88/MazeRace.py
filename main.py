'''
MAZE RACE
'''

import random

'''
SETUP GLOBALS
'''
size = 10
board = [[0 for x in xrange(size)] for y in xrange(size)]


def init_board(size):
	
	for x in xrange(size):
		for y in xrange(size):
			board[x][y] = random.choice([0,1])
	board[0][size] = 2
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
	


