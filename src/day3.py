import math


def day3a(input: int) -> int:
    # Forces the square to have an odd number as side length.
    side_of_memory_square = (math.ceil((math.sqrt(input) - 1) / 2) * 2) + 1
    side_of_memory_square_minus_center = side_of_memory_square - 1
    circles_away_from_center = side_of_memory_square_minus_center / 2

    max_on_perimeter = math.pow(side_of_memory_square, 2)
    highest_side_center = max_on_perimeter - circles_away_from_center
    distance_between_side_centers = circles_away_from_center * 2
    side_centers = [highest_side_center - (distance_between_side_centers * x) for x in range(0, 4)]
    distance_from_side_centers = [abs(input - c) for c in side_centers]
    min_distance_from_center_of_side = min(distance_from_side_centers)

    distance = min_distance_from_center_of_side + circles_away_from_center

    return distance


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # def __cmp__(self, other):

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


def calculate_value_for_position(current_coordinates: (int, int), map: {Point, int}) -> int:
    value = get_or_default(map, current_coordinates + Point(1, 0), 0) \
          + get_or_default(map, current_coordinates + Point(1, 1), 0) \
          + get_or_default(map, current_coordinates + Point(1, -1), 0) \
          + get_or_default(map, current_coordinates + Point(0, 1), 0) \
          + get_or_default(map, current_coordinates + Point(0, -1), 0) \
          + get_or_default(map, current_coordinates + Point(-1, 0), 0) \
          + get_or_default(map, current_coordinates + Point(-1, 1), 0) \
          + get_or_default(map, current_coordinates + Point(-1, -1), 0)
    return value


def get_or_default(map: {Point, int}, key: Point, default: int) -> int:
    return map[key] if key in map.keys() else default


def day3b(input: int) -> int:
    current_coordinates = Point(0, 0)
    value = 1
    map = {current_coordinates: value}
    current_side_length = 1
    directions = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]
    while value <= input:
        for current_direction in directions:
            for _ in range(0, int(current_side_length)):
                current_coordinates += current_direction
                value = calculate_value_for_position(current_coordinates, map)
                if value > input:
                    return value
                map[current_coordinates] = value
            current_side_length += 0.5


if __name__ == "__main__":
    myInput = 312051
    print(day3a(myInput))
    print(day3b(myInput))
