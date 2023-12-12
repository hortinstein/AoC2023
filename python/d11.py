#read input file
f = open("../src/d11/p1input", "r")

def expand_galaxy(galaxy, expand_rows, expand_columns):
    # Convert each row to a list of characters for column expansion
    galaxy = [list(row) for row in galaxy]

    for i in expand_columns:
        # Insert a column of '.' at the specified index
        for row in galaxy:
            row.insert(i, '.')

    # Convert each row back to a string after column expansion
    galaxy = [''.join(row) for row in galaxy]

    for i in expand_rows:
        # Create a row of '.' of the same length as other rows
        dot_row = '.' * len(galaxy[0])
        # Insert the row at the specified index
        galaxy.insert(i, dot_row)
    
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
    print (line)

expand_rows, expand_columns = find_dots_only_rows_and_columns(galaxy)
print (expand_galaxy(galaxy,expand_rows,expand_columns))

