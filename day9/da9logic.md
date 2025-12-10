problem here;
    find the largest rectangle area  possible

read all red tile coords into a list
trye every pair of red tiles as opposite corners
for each pair, compute area 
keep track of maximum area 

create empty list RED_TILES
    split line by "," into [x_str, y_str]
    x = integer value of x_str 
    y = int_value of y_str
    append (x,y) into red tiles

# find max area 
max_area =  0
best_corner_1 = null
best_corner_2 = null

N = length of RED_TILES

for i from 0 to N-1:
    (x1, y1) = RED_TILES[i]

    for j from i+1 to N-1:
    (x2, y2) = RED_TILES[j]

    width = absolute_value(x1 - x2)
    height = absolute_value(y1 - y2)

    area = width * height 

    if area > max_area:
        max_area = area
        best_corner_1 = (x1, y1)
        best_corner_2 = (x2, y2)

    output max_area