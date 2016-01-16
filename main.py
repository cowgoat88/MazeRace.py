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
	return board


board = init_board(size)
for x in board:
	print x

			

