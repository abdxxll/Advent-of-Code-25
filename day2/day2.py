# ---------------------------
#  Day 2 – Invalid Product IDs
#  (self-contained version)
# ---------------------------

# Paste your AoC input *here* as one long string.
INPUT = "2157315-2351307,9277418835-9277548385,4316210399-4316270469,5108-10166,872858020-872881548,537939-575851,712-1001,326613-416466,53866-90153,907856-1011878,145-267,806649-874324,6161532344-6161720341,1-19,543444404-543597493,35316486-35418695,20-38,84775309-84908167,197736-309460,112892-187377,336-552,4789179-4964962,726183-793532,595834-656619,1838-3473,3529-5102,48-84,92914229-92940627,65847714-65945664,64090783-64286175,419838-474093,85-113,34939-52753,14849-30381"


def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    # Pattern must repeat at least twice, so max pattern length is half the string
    for i in range(1, length // 2 + 1):

        # Pattern length must divide the whole string evenly
        if length % i != 0:
            continue

        pattern = s[:i]
        repeat_count = length // i

        if pattern * repeat_count == s:
            return True

    return False


def sum_invalid_ids_from_line(line: str) -> int:
    total = 0

    # Remove spaces/newlines in case they exist
    line = line.replace(" ", "").replace("\n", "").strip()

    for part in line.split(","):
        if not part:
            continue

        start, end = map(int, part.split("-"))
        for value in range(start, end + 1):
            if is_invalid_id(value):
                total += value

    return total


def main():
    answer = sum_invalid_ids_from_line(INPUT)
    print("Answer:", answer)


if __name__ == "__main__":
    main()
