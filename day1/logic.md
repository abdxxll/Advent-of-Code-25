# day 1 - safe dial rotation logic 

## part 1 
- dial has numbers 0-99 
- starts at position 0
- instructions are either L98 or R67
- left means position decreases, right means increases
- wrap around using modulo 100
- after each rotation, if final position == 0, count +1 

## part 2
- same dial and rotation, but every click counts 
- move one click at a time 
- each click is updated by +1 or -1 with wraparound 
- count every time the position passes 0 

pseudocode: 
position = 50
count = 0 
step = +1 if R or -1 if L
repeat distance times;
position == (position + step) mod 100
if position == 0: count += 1
return total count
