import os

def read_red_tiles():
    red_tiles = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "day9input.txt")
    with open(input_path, "r") as f:   
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x = int(x_str)
            y = int(y_str)
            red_tiles.append((x, y))
    return red_tiles


def largest_rectangle_area(red_tiles):
    max_area = 0
    best_pair = None

    n = len(red_tiles)
    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]

            # +1 because coordinates are inclusive: number of tiles between x1 and x2
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height

            if area > max_area:
                max_area = area
                best_pair = ((x1, y1), (x2, y2))

    return max_area, best_pair


if __name__ == "__main__":
    red_tiles = read_red_tiles()
    max_area, best_pair = largest_rectangle_area(red_tiles)

    print("Largest rectangle area:", max_area)
    if best_pair is not None:
        print("Corners used:", best_pair[0], "and", best_pair[1])