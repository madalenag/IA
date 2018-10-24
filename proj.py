"""
AI Project 2018/19
Taissa Ribeiro - 86514
Madalena Galrinho - 87546
"""

from search import *
from utils import *
import copy

# ______________________________________________________________________________


#TAI Content
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

# Board Operations

def num_columns(board):
	return len(board[0])

def num_lines(board):
	return len(board)


def is_move(board, l, c, dl, dc):
	return is_peg(board[l+dl][c+dc]) and is_empty(board[l+(2*dl)][c+(2*dc)])


def board_moves (board):	
	board_lines = num_lines(board)
	board_columns = num_columns(board)

	poss = []
    
	for l in range(board_lines):
		for c in range(board_columns):

			if is_peg(board[l][c]): 
			#find pegs because the number of pegs decrease with the game

				if c <= board_lines-3 and is_move(board, l, c, 0, 1):
					poss.append(make_move(make_pos(l,c),make_pos(l,c+2)))

				if c >= 2 and is_move(board, l, c, 0, -1):
					poss.append(make_move(make_pos(l,c),make_pos(l,c-2)))

				if l <= board_lines-3 and is_move(board, l, c, 1, 0):
					poss.append(make_move(make_pos(l,c),make_pos(l+2,c))) 

				if l >= 2 and is_move(board, l, c, -1, 0):
					poss.append(make_move(make_pos(l,c),make_pos(l-2,c)))
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
	board_lines = num_lines(board)
	board_columns = num_columns(board)
	counter = 0

	for l in range(board_lines):
		for c in range(board_columns):
			if is_peg(board[l][c]): 
				counter += 1
	return counter


# ______________________________________________________________________________

class sol_state:

	def __init__(self, board):
		self.board = board
		self.n_pegs = counter(board)


	def __lt__(self, other_sol_state):
		return self.board < other_sol_state.board



# ______________________________________________________________________________

class solitaire(Problem):

	def __init__(self, board):
		initial = sol_state(board)

	
	def actions(self, state):
		return board_moves(state.board)
	
	
	def result(self, state, action):
		#se n for emtpy action -1 n_pegs
		return sol_state(board_perform_move(state.board, action))
	
	
	def goal_test(self, state):
		return state.n_pegs == 1
	
	
	def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
		state1 via action."""
		#num de movimentos
		return 1


	def h(self, node):
		return 1
		#num pegs que estao no board que n estao isoladas
		#possiveis moves


"""

b1 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"],
["O","_","O","_","_"], ["_","O","_","_","_"]]

x = count_pegs(b1)
print(x)


lst = board_moves(b1)
print(lst)
ls1 = board_perform_move(b1, [(0, 2), (0, 0)])
print(ls1)
"""
