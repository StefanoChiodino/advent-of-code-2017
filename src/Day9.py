import re

import os


class Day9:
    def day9(self, stream: str) -> int:
        stream = self.sanitise_stream(stream)
        score = 0
        level = 0
        for c in stream:
            if c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
        return score

    def sanitise_stream(self, stream: str) -> str:
        sanitised_stream = re.sub(r'!.', '', stream)
        sanitised_stream = re.sub(r'<.*?>', '', sanitised_stream)
        sanitised_stream = re.sub(r',', '', sanitised_stream)
        return sanitised_stream


if __name__ == "__main__":
    path = os.path.join("..", "inputs", "day9_inputs.txt")
    lines = open(path)
    line = lines.readline()
    print(Day9().day9(line))
