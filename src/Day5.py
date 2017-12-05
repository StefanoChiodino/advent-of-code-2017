import os


class Day5():
    @staticmethod
    def execute(jump_offsets):
        i = 0
        steps = 0
        while 0 <= i < len(jump_offsets):
            next_jump= jump_offsets[i]
            jump_offsets[i] += 1
            i += next_jump
            steps += 1
        return steps


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day5_inputs.txt")
    jump_offsets = [int(l) for l in open(path)]
    print(Day5.execute(jump_offsets))