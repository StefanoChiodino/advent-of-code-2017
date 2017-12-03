import math


def day3(input):
    side_of_memory_square = (math.ceil((math.sqrt(input) - 1) / 2) * 2) + 1
    side_of_memory_square_minus_center = side_of_memory_square - 1
    circles_away_from_center = math.ceil(side_of_memory_square_minus_center / 2)

    max_on_perimeter = math.pow(side_of_memory_square, 2)
    side_centers = [(max_on_perimeter - circles_away_from_center) - (circles_away_from_center * 2 * x) for x in range(0, 4)]
    min_distance_from_center_of_side = min([abs(input - c) for c in side_centers])

    distance = min_distance_from_center_of_side + circles_away_from_center

    return distance


if __name__ == "__main__":
    myInput = 312051
    print(day3(myInput))
