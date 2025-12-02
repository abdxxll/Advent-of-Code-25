def solve_part2():
    position = 50
    count_zero = 0

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == 'R':
                step = 1
            elif direction == 'L':
                step = -1
            else:
                raise ValueError(f"Invalid direction: {direction}")

            # Move one click at a time
            for _ in range(distance):
                position = (position + step) % 100
                if position == 0:
                    count_zero += 1

    return count_zero


if __name__ == "__main__":
    result = solve_part2()
    print("Password (method 0x434C49434B):", result)
