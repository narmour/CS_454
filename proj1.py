# make a DFA that accepts strings over {a,b,c} such that eveyr substring
# of length 4 has at least one occurence of each letter a,b,c.




# how to make DFA
# hardest part is -  how do i do the transition function
# create a dictionary. key = state_name + inputsymbol  the element is state_name to switch to
# once i have the dictionary, i create an array of state_name 

from sys import stdin
import numpy as np

# STATE class
class st:
	def __init__(self, name, accept):
		self.name = name
		self.accept = accept

# Scott's state class
class state:
	def __init__(self, name, parent=None, final=False):
		"""
		Constructor
		:param name: States name
		:param parent: The parent of the current state
		:param final: if it's a final state
		"""
		self.name = name
		self.transition_list = dict() # Empty map to append to later. Pretty much a map of state transitions
		self.parent = parent # Parent state
		self.parent_transition = None # Keep track of the number we transitioned on
		self.final = final
	def add_transition(self, char, to_state):
		"""
		Add transition to current states transition map. Basically delta function
		:param char: The character you transition on
		:param to_state: The state that character goes to
		:return:
		"""
		self.transition_list[char] = to_state

def build_dfa(K, S):
	"""
	:param K: The positive integer we're finding multiples of, using numbers containing only the digits in the set S (see below)
	:param S: Subset of digits {0-9}. Alphabet for the DFA
	:return: DFA Transition Table/Matrix
	"""
	S = list(set(S)) # Remove duplicates and put in order
	states = K+1 # K remainders + start state = rows
	matrix = [state('S')] # Special 'start' state
	matrix += [state(s) for s in range(states-1)] # 0 to K-1 states

	#print("Building DFA for K =",K, "and S =",S) # Debug
	# Build DFA Matrix
	for row in matrix:
		if row.name == 'S' or row.name == 0: # S and 0 are always the same
			if row.name == 0: row.final = True # Remainder of 0 which means its the final state
			[row.add_transition(i, i % K) for i in S]
		else:
			next_state = int(str(row.name) + str(S[0])) % K # Concat row and col into int and % K. example: K = 7, row = 1, col = 1, 11 % 7 = 4, so 4 is next state
			row.add_transition(S[0],next_state) # Add a transition to row dictionary. Kind of like the delta function d(character, state to go to)
			col = 0 # Keep track of previous column
			for c in S[1:]:
				next_state = (next_state + (c - S[col])) # Example K = 7, S = [1,5], say next state is 4 (from prev col S[0] = 1) so, 4 + (current_col = S[1] = 5 - prev_col = S[col] = S[0] = 1) = 4+(5-1) = 8
				if next_state >= K: next_state -= K # If next_state >= K, (above) we got 8 so 8-7 = 1
				elif next_state < 0: next_state += K # If next_state < K - Probably could do mod above but mod is cubic while add/sub are linear
				row.add_transition(c, next_state) # Add the transition of current col to next_state
				col += 1

	return matrix

def find_string(dfa):
	"""
	:param dfa: The DFA to perform BFS on
	:return: The smallest integer of the given multiple K
	"""
	S = set()
	Q = list()
	S.add(dfa[0].name)
	Q.append(dfa[0])
	curr = None
	while Q:
		curr = Q.pop(0)
		if curr.final:
			break
		for key,value in curr.transition_list.items():
			if value not in S:
				S.add(value)
				Q.append(dfa[value+1])
				dfa[value+1].parent = curr
				dfa[value+1].parent_transition = str(key)

	if not curr.final or curr is None:
		return None # No possible integer, example: K = 4, S = [1,3,5]
	else:
		number = ""
		while curr.parent is not None:
			number += curr.parent_transition
			curr = curr.parent
		return number[::-1] # Reverse

def build_map():
	transition_mappings = dict(
		[("empty", st("empty", 0)), ("emptya", st("a", 0)), ("emptyb", st("b", 0)), ("emptyc", st("c", 0))
			, ("aa", st("aa", 0)), ("ab", st("ab", 0)), ("ac", st("ac", 0)), ("ba", st("ba", 0)), ("bb", st("bb", 0))
			, ("bc", st("bc", 0)), ("ca", st("ca", 0)), ("cb", st("cb", 0)), ("cc", st("cc", 0)),
		 ("aaa", st("reject", 0))
			, ("aab", st("aab", 0)), ("aac", st("aac", 0)), ("aba", st("aba", 0)), ("abb", st("abb", 0)),
		 ("abc", st("abc", 0))
			, ("aca", st("aca", 0)), ("acb", st("acb", 0)), ("acc", st("acc", 0)), ("baa", st("baa", 0)),
		 ("bab", st("bab", 0))
			, ("bac", st("bac", 0)), ("bba", st("bba", 0)), ("bbb", st("reject", 0)), ("bbc", st("bbc", 0)),
		 ("bca", st("bca", 0))
			, ("bcb", st("bcb", 0)), ("bcc", st("bcc", 0)), ("caa", st("caa", 0)), ("cab", st("cab", 0)),
		 ("cac", st("cac", 0)), ("cba", st("cba", 0))
			, ("cbb", st("cbb", 0)), ("cbc", st("cbc", 0)), ("cca", st("cca", 0)), ("ccb", st("ccb", 0)),
		 ("ccc", st("reject", 0))
			, ("aaaa", st("reject", 0)), ("aaab", st("reject", 0)), ("aaac", st("reject", 0)), ("aaba", st("reject", 0))
			, ("aabb", st("reject", 0)), ("aabc", st("abc", 1)), ("aaca", st("reject", 0)), ("aacb", st("acb", 1)),
		 ("aacc", st("reject", 0))
			, ("abaa", st("reject", 0)), ("abab", st("reject", 0)), ("abac", st("bac", 1)), ("abba", st("reject", 0)),
		 ("abbb", st("reject", 0))
			, ("abbc", st("bbc", 1)), ("abca", st("bca", 1)), ("abcb", st("bcb", 1)), ("abcc", st("bcc", 1)),
		 ("acaa", st("reject", 0))
			, ("acab", st("cab", 1)), ("acac", st("reject", 0)), ("acba", st("cba", 1)), ("acbb", st("cbb", 1)),
		 ("acbc", st("cbc", 1))
			, ("acca", st("reject", 0)), ("accb", st("ccb", 1)), ("accc", st("reject", 0)), ("baaa", st("reject", 0)),
		 ("baab", st("reject", 0))
			, ("baac", st("aac", 1)), ("baba", st("reject", 0)), ("babb", st("reject", 0)), ("babc", st("abc", 1)),
		 ("baca", st("aca", 1))
			, ("bacb", st("acb", 1)), ("bacc", st("acc", 1)), ("bbaa", st("reject", 0)), ("bbab", st("reject", 0)),
		 ("bbac", st("bac", 1))
			, ("bbba", st("reject", 0)), ("bbbb", st("reject", 0)), ("bbbc", st("reject", 0)), ("bbca", st("bca", 1)),
		 ("bbcb", st("reject", 0))
			, ("bbcc", st("reject", 0)), ("bcaa", st("caa", 1)), ("bcab", st("cab", 1)), ("bcac", st("cac", 1)),
		 ("bcba", st("cba", 1))
			, ("bcbb", st("reject", 0)), ("bcbc", st("reject", 0)), ("bcca", st("cca", 1)), ("bccb", st("reject", 0)),
		 ("bccc", st("reject", 0))
			, ("caaa", st("reject", 0)), ("caab", st("aab", 1)), ("caac", st("reject", 0)), ("caba", st("aba", 1)),
		 ("cabb", st("abb", 1))
			, ("cabc", st("abc", 1)), ("caca", st("reject", 0)), ("cacb", st("acb", 1)), ("cacc", st("reject", 0)),
		 ("cbaa", st("baa", 1))
			, ("cbab", st("bab", 1)), ("cbac", st("bac", 1)), ("cbba", st("bba", 1)), ("cbbb", st("reject", 0)),
		 ("cbbc", st("reject", 0))
			, ("cbca", st("bca", 1)), ("cbcb", st("reject", 0)), ("cbcc", st("reject", 0)), ("ccaa", st("reject", 0)),
		 ("ccab", st("cab", 1))
			, ("ccac", st("reject", 0)), ("ccba", st("cba", 1)), ("ccbb", st("reject", 0)), ("ccbc", st("reject", 0)),
		 ("ccca", st("reject", 0))
			, ("cccb", st("reject", 0)), ("cccc", st("reject", 0)), ("rejecta", st("reject", 0)),
		 ("rejectb", st("reject", 0))
			, ("rejectc", st("reject", 0))

		 ])  # set comprehension since i only want the unique states in my dfa
	return transition_mappings


def create_transition_matrix(mapping, states):
	# create transition matrix
	# i know this can be done in a simple list comprehension
	transition_matrix = []
	for i_state in states:
		transition_matrix.append([])
		for j_state in states:
			row = transition_matrix[-1]  # last element
			count = 0
			for c in ['a', 'b', 'c']:
				if mapping[i_state + c].name == j_state:
					count = count + 1
			row.append(count)
	return transition_matrix

def create_final_vector(transition_mappings, states):
	# create final_vector
	# this should also be a list comprehension
	final_vector = [1 if transition_mappings[s+'a'].accept or transition_mappings[s+'b'].accept or transition_mappings[s+'c'].accept else 0 for s in states]
	return final_vector

def count(n):
	transition_mappings = build_map()

	states = list({state.name for name, state in transition_mappings.items() if
				   state.name not in ["aaa", "bbb", "ccc", "rejecta", "rejectb", "rejectc"]})

	transition_matrix = create_transition_matrix(transition_mappings, states)

	# create start_matrix
	start_vector = [1 if s == "empty" else 0 for s in states]
	# Final vector
	final_vector = create_final_vector(transition_mappings, states)
	# Possible number of string with length n. u*(A^n)*v
	x = np.dot(np.array(start_vector, dtype=object), np.linalg.matrix_power(np.array(transition_matrix, dtype=object), n))

	return np.dot(x, np.array(final_vector))

def main():
	n = int(input("Length = "))
	print(count(n))

	# Problem 2
	K = int(input("K = ")) # 13
	S = input("S = ")# Enter input like S = 2 5 (separated by spaces)
	S = S.split()
	S = [int(x) for x in S]
	dfa = build_dfa(K, S) # K = 13 and S = 2 5 gives us 52 (correct according to ravi)
	print(find_string(dfa))


main()
