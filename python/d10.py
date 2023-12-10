# thank you reddit; https://old.reddit.com/r/adventofcode/comments/18ez6d0/2023_day_10_visualization_with_simple_symbol_remap/
symbols = {
    "|": "\u2503",
    "-": "\u2501",
    "L": "\u2517",
    "J": "\u251B",
    "7": "\u2513",
    "F": "\u250F",
}

rules = {
    # | is a vertical pipe connecting north and south.
    "\u2503": "NS",
    # - is a horizontal pipe connecting east and west.
    "\u2501": "EW",
    # L is a 90-degree bend connecting north and east.
    "\u2517": "NE",
    # J is a 90-degree bend connecting north and west.
    "\u251B": "NW",
    # 7 is a 90-degree bend connecting south and west.
    "\u2513": "SW",
    # F is a 90-degree bend connecting south and east.
    "\u250F": "SE",
    # . is ground; there is no pipe in this tile.
    ".": "",
    "S":"NSWE"
}

#read input file
f = open("../src/d10/p1input", "r")

pipes = []
start_x,start_y = 0,0
for i,line in enumerate(f):
    
    if "S" in line:
        start_y = i
        start_x = line.index("S")
        print ("S found:(",start_x,",",start_y,")")
    # Replace the symbols in the string
    for old, new in symbols.items():
        line = line.replace(old, new)
    
    pipes.append(line.strip())

for line in pipes:
    print (line)


def next_move(x,y,last):
    print (x,y,last)
    if ((x-1,y) != last and "E" in rules[pipes[y][x-1]]):
        return x-1,y,(x,y)
    if ((x+1,y) != last and "W" in rules[pipes[y][x+1]]):
        return x+1,y,(x,y)
    if ((x,y+1) != last and "N" in rules[pipes[y+1][x]]):
        return x,y+1,(x,y)
    if ((x,y-1) != last and "S" in rules[pipes[y-1][x]]):
        return x,y-1,(x,y)
    return x,y

i_x,i_y,i_count,i_last = start_x,start_y-1,0,(start_x,start_y)
j_x,j_y,j_count,j_last = start_x,start_y+1,0,(start_x,start_y)
    
while (i_x,i_y) != (j_x,j_y):
    
    i_x,i_y,i_last = next_move(i_x,i_y,i_last)
    i_count+=1

    j_x,j_y,j_last = next_move(j_x,j_y,j_last)
    j_count+=1