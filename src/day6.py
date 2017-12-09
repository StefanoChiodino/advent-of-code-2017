from copy import copy


def day6(memory_blocks):
    previous_states = []
    rebalances = 0
    while memory_blocks not in previous_states:
        previous_states += [copy(memory_blocks)]
        rebalances += 1
        rebalance(memory_blocks)
    return rebalances


def rebalance(memory_blocks):
    max_blocks = max(memory_blocks)
    index = memory_blocks.index(max_blocks)
    memory_blocks[index] = 0
    for _ in range(0, max_blocks):
        index += 1
        if index >= len(memory_blocks):
            index = 0
        memory_blocks[index] += 1


if __name__ == "__main__":
    print(day6([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]))
