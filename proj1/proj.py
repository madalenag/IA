'''
AI Project 2018/19
Grupo 11
Taissa Ribeiro - 86514
Madalena Galrinho - 87546
'''


from search import *
from utils import *
import copy

# ______________________________________________________________________________


#TAI Content:
def c_peg ():
	return "O"
def c_empty():
	return "_"
def c_blocked():
	return "X"
def is_empty(e):
	return e == c_empty()
def is_peg(e):
	return e == c_peg()
def is_blocked(e):
	return e == c_blocked()


#TAI Pos
#Tuplo (l, c)
def make_pos(l, c):
	return (l, c)
def pos_l (pos):
	return pos[0]
def pos_c (pos):
	return pos[1]


#TAI move
#Lista [p_inicial, p_final]
def make_move (i,f):
	return [i,f]
def move_initial (move):
	return move[0]
def move_final (move):
	return move[1]

# ______________________________________________________________________________

#Board Operations

def is_move(board, l, c, dl, dc):
	return is_peg(board[l+dl][c+dc]) and is_empty(board[l+(2*dl)][c+(2*dc)])



def board_moves(board):
    poss = []
    board_lines = len(board)
    board_columns = len(board[0])

    for l in range(board_lines):
        for c in range(board_columns):

        	if is_peg(board[l][c]):
		        
		        if c >= 2 and is_move(board, l, c, 0, -1):
		                poss.append(make_move(make_pos(l,c),make_pos(l,c-2)))
		       
		        if c <= board_columns-3 and is_move(board, l, c, 0, 1):
		                poss.append(make_move(make_pos(l,c),make_pos(l,c+2)))
		    
		        if l >= 2 and is_move(board, l, c, -1, 0):
		                poss.append(make_move(make_pos(l,c),make_pos(l-2,c)))
		     
		        if l <= board_lines-3 and is_move(board, l, c, 1, 0):
		                poss.append(make_move(make_pos(l,c),make_pos(l+2,c)))
    return poss



def board_perform_move(board, move):
	new_board = copy.deepcopy(board)

	ini_col = pos_c(move_initial(move))
	ini_line = pos_l(move_initial(move))
	final_col = pos_c(move_final(move))
	final_line = pos_l(move_final(move))
	middle_col= (ini_col + final_col)//2
	middle_line = (ini_line + final_line)//2

	new_board[ini_line][ini_col] = c_empty()
	new_board[middle_line][middle_col] = c_empty()
	new_board[final_line][final_col] = c_peg()

	return new_board


def count_pegs(board):
	board_lines = len(board)
	board_columns = len(board[0])

	counter = 0

	for l in range(board_lines):
		counter += board[l].count(c_peg())

	return counter



def count_corners(board):
	cont = 0
	lines = len(board)
	columns = len(board[0])

	if is_peg(board[0][0]):
		cont += 1
	if is_peg(board[0][columns-1]):
		cont +=1
	if is_peg(board[lines-1][0]):
		cont +=1
	if is_peg(board[lines-1][columns-1]):
		cont +=1

	return cont


def movable_pegs(board):
    initial = []
    board_lines = len(board)
    board_columns = len(board[0])

    for l in range(board_lines):
        for c in range(board_columns):

        	movable_peg = False

        	if is_peg(board[l][c]):
		        
		        if c >= 2 and is_move(board, l, c, 0, -1):
		                movable_peg = True

		        if c <= board_columns-3 and is_move(board, l, c, 0, 1):
		                movable_peg = True
		    
		        if l >= 2 and is_move(board, l, c, -1, 0):
		                movable_peg = True
		     
		        if l <= board_lines-3 and is_move(board, l, c, 1, 0):
		                movable_peg = True

		        if movable_peg:
		            initial.append(make_pos(l,c))

    return len(initial)


# ______________________________________________________________________________


class sol_state:

	def __init__(self, board):
		self.board = board
		self.n_pegs = count_pegs(board)

	def __lt__(self, other_sol_state):
		return self.n_pegs > other_sol_state.n_pegs


# ______________________________________________________________________________

class solitaire(Problem):

	def __init__(self, board):
		self.initial = sol_state(board)

	def actions(self, state):
		return board_moves(state.board)

	def result(self, state, action):
		return sol_state(board_perform_move(state.board, action))

	def goal_test(self, state):
		return state.n_pegs == 1

	def path_cost(self, c, state1, action, state2):
		return c + 1

	def h(self, node):
		pegs = node.state.n_pegs

		if pegs == 1:
			return 0

		unmovable_pegs = pegs - movable_pegs(node.state.board)
		corners = count_corners(node.state.board)

		return pegs + corners + unmovable_pegs
