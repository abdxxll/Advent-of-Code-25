fresh_count = 0 

for each id in ids_to_check:
    fresh = false 

for each (start,end) in ranges:
    if start <= id <=end:
    fresh = true
    break

if fresh:
    fresh_count += 1

print (fresh_count)