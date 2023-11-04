from math import sqrt
from random import randint
from utils.Constants import PATH_WEIGHT, TIME_WEIGHT


# Euclidean distance (Pythagorean Theorem)
def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# Inverse distance function (Manhattan distance)
def calculate_fitness(individual, cities):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += calculate_distance(cities[individual[i]], cities[individual[i + 1]])
    return 1 / total_distance


# Generating random cities list, vector of X and Y coordinates
def generate_cities(num_cities, map_size):
    return [(randint(0, map_size), randint(0, map_size)) for _ in range(num_cities)]


# Calculate path value based on path length and time it took to generate
def calculate_path_value(entry):
    return (entry.get("path_length") * PATH_WEIGHT) + (entry.get("time") * TIME_WEIGHT)
