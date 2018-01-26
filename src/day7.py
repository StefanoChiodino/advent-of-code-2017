import re

import os
from typing import List


def day7(instructions: List[str]) -> str:
    discs = []
    for match in [re.match(r"(\w*)\s?\((\d*)\)?\s?-?>?\s?((\w*,?\s?)*)", instruction) for instruction in instructions]:
        disc = Disc()
        disc.name = match.group(1)
        disc.weight = match.group(2)
        disc.children = match.group(3).split(", ") if match.group(3) is not None else None
        discs.append(disc)

    all_discs_names = [d.name for d in discs]
    for disc in [d for d in discs if d.children is not None]:
        for children_disc in disc.children:
            if children_disc in all_discs_names:
                all_discs_names.remove(children_disc)
    return all_discs_names[0]


class Disc:
    pass


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day7_inputs.txt")
    with open(path) as file:
        lines = [l.strip() for l in file]
    print(day7(lines))
