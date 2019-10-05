# Author: Pranav Minasandram
# 355 Final Project - DFA Simulator
# 
# Usage: python3 simulator.py dfa_input_file test_strings_file
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
# 3 4

import sys

def take_input_dfa(input_dfa_filename):
  """Takes in DFA data from a given filename and constructs transition table"""
  
  # Variables to set so they can be used outside of this scope
  global num_states
  global final_states
  global str_alphabet
  global transition_table

  # Context manager for opening input dfa
  with open(input_dfa_filename) as dfa:
     lines = dfa.readlines()

     # Take in input data
     num_states = int(lines[0].strip().split(" ")[3])                     # Take 4th word of first line
     final_states = list(map(int, lines[1].strip().split(" ")[2:]))       # Take everything after first two words of second line, and convert to an int list
     str_alphabet = lines[2][10:]                                         # Take everything after 'Alphabet: '
     
     
     # Transition table is accessed as such: transition_table[curr_state][input_char] -> new_state
     transition_table = [[]*len(str_alphabet)]*num_states
     
     # Converts the given transition table from text to a 2d list (num_states * length of alphabet)
     for i in range(num_states):
       transition_table[i] = list(map(int, lines[3+i].split(" ")))

def simulate_dfa(input_string):
    """ Takes in an input string and prints whether it is accepted or rejected"""
    current_state = 0
    for c in input_string:
        if(c == '\n'):
            break
        symbol_index = str_alphabet.index(c)
        current_state = transition_table[current_state][symbol_index]
    if current_state in final_states:
        print("accept")
    else:
        print("reject")

def take_input_strings(input_strings_filename):
    """Takes the lines from the input_strings file and runs them through the DFA"""
    with open(input_strings_filename) as strings:
       for line in strings:
         simulate_dfa(line)

if __name__ == "__main__":
  input_dfa_filename = sys.argv[1]
  input_strings_filename = sys.argv[2]
  take_input_dfa(input_dfa_filename)
  take_input_strings(input_strings_filename)
  
