grid = list of strings fronm input
H = number of rows in grid 
L = number of columns in grid 

# find start S
for r in 0..H-1:
    for c in 0..W-1:
        if grid [r][c] == "S"
            start_row = r 
            start_col = c

split count = 0

#beams[c] == true means beam is entering row r from above at column c 
beams = array[0..W-1] of bool initialized to false