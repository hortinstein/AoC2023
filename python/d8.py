from termcolor import colored

rm_blnks = lambda n: [i for i in n if i]


#read input file
f = open("../src/d8/p1input", "r")


input_string = f.read().split("\n\n")
instructions,turns = input_string[0],input_string[1].split("\n")
print(instructions,turns)

turns_dict ={}

for turn in turns:
    dest = turn[0:3]
    dest_left = turn[7:10]
    dest_right = turn[12:15]
    turns_dict[dest] = (dest_left,dest_right)
steps = 0
position = "AAA"
while position != "ZZZ":
    for i in instructions:
        print (position)
        steps+=1
        if i == "L":
            position = turns_dict[position][0]
        elif i == "R":
            position = turns_dict[position][1]
        if position == "ZZZ": 
            break
print (steps)