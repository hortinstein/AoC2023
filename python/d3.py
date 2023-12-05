from termcolor import colored

#read input file
f = open("../src/d3/p1input", "r")


symbols = '!@#$%^/\&*()_+=-~`/\\'
    

#build 2d representation
data_structure = []
for line in f:
    data_structure.append(line.strip('\r\n'))
def check_for_symbols(data_structure,x_coord,y_coord):
    # print("STES",data_structure[y_coord][x_coord])
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if (x >= 0 and x < len(data_structure)) and (y >= 0 and y < len(data_structure[0])):
            if data_structure[y][x] in symbols:
                return True
    return False

total = 0
total_gears = 0

## PART 1
for y,line in enumerate(data_structure):
    digit = ''
    touching = False
    
    print('')
    for x,c in enumerate(line):
        if c.isdigit() and (x == 139 or line[x+1] in (symbols+'.')):
            digit+=c
            touching = touching or check_for_symbols(data_structure,x,y)
            if len(digit) > 0 and touching:
                print (digit,end='')
                total += int(digit)
            elif len(digit) > 0 and not touching:
                print (colored(digit,"red"),end='')
            touching = False
            continue
        if c.isdigit() and line[x+1].isdigit():
            digit+=c
            touching = touching or check_for_symbols(data_structure,x,y)
            continue
        if c == '.':
            digit = ""
            print(c,end='')
            touching = False
            continue
        else: 
            print(c,end='')
            digit = ""

def number_lim(data_structure,x,y):
    fullnum = ''
    i = x
    while (i>=0 and data_structure[y][i].isdigit()):
        fullnum=data_structure[y][i]+ fullnum
        i-=1
    i = x+1
    while (i< len(data_structure[0]) and data_structure[y][i].isdigit()):
        fullnum=fullnum+data_structure[y][i]
        i+=1
    return fullnum

def return_numbers_around(data_structure,x_coord,y_coord):
    numbers_around = []
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if (x >= 0 and x < len(data_structure)) and (y >= 0 and y < len(data_structure[0])):
            if data_structure[y][x].isdigit():
                numbers_around.append(number_lim(data_structure,x,y))
    
    #prolly need to guard against a shitty edge case here
    deduped= list(set(numbers_around))
    if len(deduped) == 2:
        return int(deduped[0])*int(deduped[1])
    
    return 0

for y,line in enumerate(data_structure):
    for x,c in enumerate(line):     
        if c == "*":
            total_gears += return_numbers_around(data_structure,x,y)

print (colored("total:"+ str(total),"green"))
print (colored("total gears:"+ str(total_gears),"green"))