input lines into a list grid

rows = number of lines in grid
cols = length of first line

directions = 8 adjacent spaces 
    up down left right diagonals 

set accessible count = 0 

for r from 0 to rows-1:
    for c from 0 to cols-1:
        if grid[r][c] != '@':
            continue

        adj_count = 0

        for (dr, dc) in directions:
            nr = r + dr
            nc = c + dc

            if nr is outside [0, rows-1]:
                continue
            if nc is outside [0, cols-1]:
                continue

            if grid[nr][nc] == '@':
                adj_count += 1

        if adj_count < 4:
            accessible_count += 1

print accessible_count