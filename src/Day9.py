import re


class Day9:
    def day9(self, stream):
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

    def sanitise_stream(self, stream):
        sanitised_stream = re.sub(r'!.', '', stream)
        sanitised_stream = re.sub(r'<.*?>', '', sanitised_stream)
        sanitised_stream = re.sub(r',', '', sanitised_stream)
        return sanitised_stream