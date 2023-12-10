from termcolor import colored
import math 
rm_blnks = lambda n: [i for i in n if i]


#read input file
f = open("../src/d8/p1input", "r")


input_string = f.read().split("\n\n")
instructions,turns = input_string[0],input_string[1].split("\n")

turns_dict ={}

for turn in turns:
    dest = turn[0:3]
    dest_left = turn[7:10]
    dest_right = turn[12:15]
    turns_dict[dest] = (dest_left,dest_right)


def solver(turns_dict,position):
    steps = 0
    while position[-1] != "Z":
        for i in instructions:
            # print (position)
            steps+=1
            if i == "L":
                position = turns_dict[position][0]
            elif i == "R":
                position = turns_dict[position][1]
            if position == "ZZZ": 
                break
    return (steps)

print (colored(solver(turns_dict,"AAA"),"yellow"))

# help from: https://advent-of-code.xavd.id/writeups/2023/day/8/
starts = [k for k in turns_dict.keys() if k[-1] == "A"]

lmc_input = [solver(turns_dict,s) for s in starts]

print (lmc_input)

print (math.lcm(*lmc_input))


