### Foundations of Computation - Final Project
This project consists of two parts. The first part is a simple dfa simulator (simulator.py) which accepts a text file of the format

```
Number of states: 5
Accepting states: 1 4
Alphabet: 01
0 1
2 3
4 0
1 2
3 4
teststring1
teststring2
...
teststringN
```

Where the columns correspond the the characters of the alphabet in the order they are given, and the rows correspond to the states (0-indexed). It then runs the teststrings on the dfa and outputs either "accept" or "reject" if they are accepted or rejected by the given dfa. 

The second part is my_properties.py, which takes in a DFA in the same format as simulator.py without the teststrings and outputs if the set defined by the DFA is empty/nonempty and finite/infinite using DFS and BFS. 

## DISCLAIMER
I do not endorse the use of this code to be used by students who are currently in Foundations of Computation. Do the right thing and do it on your own. You'll thank yourself in the future, trust me. You also add the risk of multiple students trying to use my code and get caught by MOSS. Don't do it.
https://www.youtube.com/watch?v=hMloyp6NI4E
