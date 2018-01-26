import os
import re


def solve(stream: str) -> int:
    sanitised_stream = re.sub(r'!.', '', stream)
    garbage = re.findall(r'<(.*?)>', sanitised_stream)
    lengths = [len(g) for g in garbage]
    score = sum(lengths)
    return score


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day9_inputs.txt")
    with open(path) as lines:
        line = lines.readline()
    print(solve(line))
