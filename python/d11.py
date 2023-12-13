from math import dist

#read input file
f = open("../src/d11/p1input", "r")

def replace_symbols(galaxy):
    s = 1
    for i,line in enumerate(galaxy):
        for j,star in enumerate(line):
            if star == "#":
                galaxy[i] = galaxy[i][:j] + str(s) + galaxy[i][j+1:]
                s += 1
    return galaxy

def expand_galaxy(galaxy, expand_rows, expand_columns):
    # Convert each row to a list of characters for column expansion
    galaxy = [list(row) for row in galaxy]
    print ("expand_rows:",expand_rows,"expand_columns:",expand_columns)
    for i,n in enumerate(expand_columns):
        # Insert a column of '.' at the specified index
        for row in galaxy:
            # print("expand_columns:",n)
            row.insert(n+i, '.')

    # Convert each row back to a string after column expansion
    galaxy = [''.join(row) for row in galaxy]

    for i,n in enumerate(expand_rows):
        # print("expand_rows:",i)
        # Create a row of '.' of the same length as other rows
        dot_row = '.' * len(galaxy[0])
        # Insert the row at the specified index
        galaxy.insert(n+i, dot_row)
    
    return galaxy


def find_dots_only_rows_and_columns(array):
    # Convert string to 2D array
    array = galaxy

    # Initialize lists to store indices of rows and columns with only dots
    rows_with_only_dots = []
    columns_with_only_dots = []

    # Check rows
    for i, row in enumerate(array):
        if all(char == '.' for char in row):
            rows_with_only_dots.append(i)

    # Check columns
    for j in range(len(array[0])):
        if all(array[i][j] == '.' for i in range(len(array))):
            columns_with_only_dots.append(j)

    return rows_with_only_dots, columns_with_only_dots

galaxy = []
for line in f:
    galaxy.append(line.strip())
    print (line,end='')
print("")
expand_rows, expand_columns = find_dots_only_rows_and_columns(galaxy)


def build_location_dictionary(galaxy):
    location_dictionary = {}
    s = 1
    for row,line in enumerate(galaxy):
        for column,c in enumerate(line):
            if c == "#":
                location_dictionary[s] = (row,column)
                s += 1
    return location_dictionary

def distance_between_stars(galaxy,start,goal):
    # print (start,goal)
    
    #taxi cab distance works
    dist = abs(location_dictionary[start][0]-location_dictionary[goal][0]) + abs(location_dictionary[start][1]-location_dictionary[goal][1])
    print ("between galaxy {} and galaxy {}: {}".format(start,goal,dist))

    #euclidean distance for comparison
    # return dist(location_dictionary[start],location_dictionary[goal])

    return dist

expanded_galaxy = expand_galaxy(galaxy,expand_rows,expand_columns)
# expanded_galaxy = replace_symbols(expanded_galaxy)
for line in expanded_galaxy:
    print (line)

location_dictionary = build_location_dictionary(expanded_galaxy)
print (location_dictionary)
# assert 15 == distance_between_stars(expanded_galaxy,1,7)
# assert 17 == distance_between_stars(expanded_galaxy,3,6)
# assert 5 == distance_between_stars(expanded_galaxy,8,9)

# for all pairs of stars in location dictionary, find the distance between them

from itertools import combinations

def find_minimum_distances(galaxy, location_dictionary, distance_func):
    min_distances = {key: float('inf') for key in location_dictionary.keys()}
    total_distance = 0
    # Iterate over each combination of two keys
    for key1, key2 in combinations(location_dictionary.keys(), 2):
        distance = distance_func(galaxy, key1, key2)
        total_distance+=distance
        # Update the minimum distances for each key
        min_distances[key1] = min(min_distances[key1], distance)
        min_distances[key2] = min(min_distances[key2], distance)
    print (total_distance)
    return min_distances

# Example usage
min_distances = find_minimum_distances(expanded_galaxy, location_dictionary, distance_between_stars)
print(min_distances)
