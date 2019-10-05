# Author: Pranav Minasandram
# 355 Final Project - DFA Properties
# Determines if a given DFA's language is infinite/finite and empty/nonempty 
#
# Usage: python3 my_properties.py dfa_input_file
# 
# dfa_input_file example:
# 
# Number of states: 5
# Accepting states: 1 4
# Alphabet: 01
# 0 1
# 2 3
# 4 0
# 1 2



import simulator
import sys
import queue

def has_walk_to_final(state):
    """Does a BFS on a state to see if it has a walk to a final state"""
    if state in simulator.final_states:
        return True
    bfs_visited = [False] * simulator.num_states
    queue = []
    queue.append(state)
    bfs_visited[state] = True

    while queue:
        state = queue.pop(0)

        bfs_adjacent_states = list(dict.fromkeys(simulator.transition_table[state]))
        bfs_adjacent_states.sort()
        for i in bfs_adjacent_states:
            if i in simulator.final_states:
                return True
            if bfs_visited[i] == False:
                queue.append(i)
                bfs_visited[i] = True
    return False


def DFS(v, visited, stack):
    """Does a DFS on a node to find any cycles"""
    visited[v] = True
    stack[v] = True


    adjacent_states = list(dict.fromkeys(simulator.transition_table[v]))
    adjacent_states.sort()
    for state in adjacent_states:
        if visited[state] == False:
            if DFS(state, visited, stack):
                return True
        
        # if the state is in a cycle, it must also have a walk to the final state to make the language infinite
        elif stack[state] == True and has_walk_to_final(state):
            return True
    stack[v] = False
    return False

def DFShelper(v):
    visited = [False] * simulator.num_states
    stack = [False] * simulator.num_states
    
    adjacent_states = list(dict.fromkeys(simulator.transition_table[v]))
    adjacent_states.sort()
    
    for state in adjacent_states:
        if visited[state] == False:
            if DFS(state, visited, stack):
                return True
    return False


if __name__ == '__main__':
    input_dfa_filename = sys.argv[1]
    simulator.take_input_dfa(input_dfa_filename)
    empty = "empty"
    finite = "finite"

    if has_walk_to_final(0):
        empty = "nonempty"
    
    if DFShelper(0) and empty == "nonempty":
        finite = "infinite"
    print(empty, finite)
