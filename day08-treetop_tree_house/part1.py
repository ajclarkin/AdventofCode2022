# Day 8 - Treetop Tree House, part 1

input = [[int(char) for char in row] for row in open('input.txt').read().split('\n')]


row_length = len(input[0])
col_length = len(input)
tree_positions = set()


# Rows
total_trees = 0

for row_no, row in enumerate(input[1:-1], 1):
    high_point = -1

    prev_height = -1
    for col_no, char in enumerate(row):        
        if char > prev_height:
            prev_height = char
            high_point = col_no
            if (col_no != 0) and (col_no != row_length-1):
                tree_positions.add((row_no, col_no))

    prev_height = -1
    for back_row_pos, char in enumerate(reversed(row)):
        col_no = len(row) - (back_row_pos + 1)        
        if col_no == high_point:
            break

        if (char > prev_height) and (col_no != high_point):
            prev_height = char

            if (col_no != 0) and (col_no != row_length-1):
                tree_positions.add((row_no, col_no))



# Columns
for col_no in range(1, row_length-1):
    # Go down the column...
    high_point = -1
    prev_height = -1

    for row_no in range(col_length):

        char = input[row_no][col_no]
        if char > prev_height:
            prev_height = char
            high_point = row_no

            if (row_no != 0) and (row_no != col_length-1):
                tree_positions.add((row_no, col_no))


    # ... Then back up the column
    prev_height = -1
    for row_no in range(col_length-1, -1, -1):
        char = input[row_no][col_no]
        
        if row_no == high_point:
            break

        if (char > prev_height) and (row_no != high_point):
            prev_height = char
            high_point = row_no

            if (row_no != 0) and (row_no != col_length-1):
                tree_positions.add((row_no, col_no))


# Add the perimeter
perimeter = (row_length * 2) + ((col_length - 2) *2)
print(f'Total trees = {perimeter + len(tree_positions)}')

