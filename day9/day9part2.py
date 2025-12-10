from shapely.geometry import Polygon, box
import os

def read_red_tiles():
    tiles = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "day9input.txt")
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            tiles.append((x, y))
    return tiles

def largest_rectangle_using_polygon(red_tiles):
    # Build polygon from the loop of red tiles.
    # The puzzle guarantees:
    # - each pair of consecutive tiles is axis-aligned
    # - the path wraps around to form a closed loop.
    poly = Polygon(red_tiles)

    max_area = 0
    best_pair = None

    n = len(red_tiles)
    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]

            # Opposite corners of axis-aligned rectangle
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            ymax = max(y1, y2)

            # Tile area: coordinates are tile indices, inclusive
            width = xmax - xmin + 1
            height = ymax - ymin + 1
            tile_area = width * height

            # Prune: if this can't beat current max, skip
            if tile_area <= max_area:
                continue

            # Geometric rectangle in the same coordinate space.
            # Using continuous [xmin, xmax] x [ymin, ymax].
            rect = box(xmin, ymin, xmax, ymax)

            # Check whether the rectangle is fully inside or on the boundary
            # of the red+green loop polygon.
            # `covers` allows boundary-touching rectangles.
            if poly.covers(rect):
                max_area = tile_area
                best_pair = ((x1, y1), (x2, y2))

    return max_area, best_pair

if __name__ == "__main__":
    red_tiles = read_red_tiles()
    max_area, best_pair = largest_rectangle_using_polygon(red_tiles)

    print("Largest rectangle area (Part 2):", max_area)
    if best_pair is not None:
        print("Corners used:", best_pair[0], "and", best_pair[1])
