import math


def day3(input):
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


if __name__ == "__main__":
    myInput = 312051
    print(day3(myInput))
