total = 0

for each range in input:
    start, end = parse range

    for id from start to end:
        s = str(id)

        if length of s is odd: continue

        mid = len(s) / 2
        first = s[0:mid]
        second = s[mid:end]

        if first == second:
            total += id
