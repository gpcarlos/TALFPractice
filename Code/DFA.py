DFA = ((1, 2), # Transition table
       (1, 3),
       (0, 2),
       (0, 4),
       (4, 4))

file = open("inputTestCases.txt","r")

for line in file:
    state = 0
    for char in line:
        if ord(char)!=10: # To avoid the 'enter'
            if char=='0': c=0
            else: c=1
            state = DFA[state][c]

    if state==0:
        print(line," Accept")
    else:
        print(line," Reject")
