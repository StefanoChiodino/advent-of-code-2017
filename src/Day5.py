import os
from typing import List


def day5a(jump_offsets: List[int]) -> int:
    i = 0
    steps = 0
    while 0 <= i < len(jump_offsets):
        next_jump= jump_offsets[i]
        jump_offsets[i] += 1
        i += next_jump
        steps += 1
    return steps


def day5b(jump_offsets: List[int]) -> int:
    i = 0
    steps = 0
    while 0 <= i < len(jump_offsets):
        next_jump = jump_offsets[i]
        jump_offsets[i] += 1 if next_jump < 3 else -1
        i += next_jump
        steps += 1
    return steps


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day5_inputs.txt")
    with open(path) as file:
        jump_offsets = [int(l) for l in file]
    print(day5a(jump_offsets))
    print(day5b(jump_offsets))
