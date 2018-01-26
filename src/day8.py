import os
from typing import List


def day8(instructions: List[str]) -> int:
    register = {}
    for instruction in instructions:
        instruction_parts = instruction.split(" ")
        name = instruction_parts[0]
        call = instruction_parts[1]
        quantity = int(instruction_parts[2])
        check_name = instruction_parts[4]
        check_condition = instruction_parts[5]
        check_quantity = int(instruction_parts[6])

        if name not in register:
            register[name] = 0
        if check_name not in register:
            register[check_name] = 0

        if check_condition == ">":
            check_is_valid = register[check_name] > check_quantity
        elif check_condition == "<":
            check_is_valid = register[check_name] < check_quantity
        elif check_condition == "==":
            check_is_valid = register[check_name] == check_quantity
        elif check_condition == "!=":
            check_is_valid = register[check_name] != check_quantity
        elif check_condition == ">=":
            check_is_valid = register[check_name] >= check_quantity
        elif check_condition == "<=":
            check_is_valid = register[check_name] <= check_quantity

        if check_is_valid:
            register[name] += quantity * (-1 if call == "dec" else 1)

    return max([register[key] for key in register])


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day8_inputs.txt")
    with open(path) as file:
        lines = [l.strip() for l in file]
    print(day8(lines))
