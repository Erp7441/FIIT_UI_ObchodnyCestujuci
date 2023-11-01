import random

from utils.Calc import calculate_fitness


class Tabu:
    def __init__(self, num_cities=20, map_size=200, cities=None):
        self.map_size = map_size

        if cities is None:
            self.num_cities = num_cities
            self.cities = [(random.randint(0, map_size), random.randint(0, map_size)) for _ in range(num_cities)]
        else:
            self.cities = cities
            self.num_cities = len(cities)

        self.solution = self.initialize(num_cities)
        self.best_solution = self.solution[:]
        self.tabu_list = [self.solution[:]]  # First permutation is in tabu list

    @staticmethod
    def initialize(num_cities):
        solution = list(range(num_cities))
        random.shuffle(solution)
        return solution

    # Generating neighbor solutions
    @staticmethod
    def generate_neighbors(solution):
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbor = solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def start(self, num_iterations, num_neighbors):
        for _ in range(num_iterations):
            neighbors = Tabu.generate_neighbors(self.solution)
            neighbors.sort(key=lambda x: -calculate_fitness(x, self.cities))
            found = False

            for neighbor in neighbors:
                if neighbor not in self.tabu_list or calculate_fitness(neighbor, self.cities) > calculate_fitness(
                        self.best_solution, self.cities):
                    self.solution = neighbor
                    self.tabu_list.append(neighbor)
                    if len(self.tabu_list) > num_neighbors:
                        self.tabu_list.pop(0)
                    found = True
                    break

            if not found:
                break
            if calculate_fitness(self.solution, self.cities) > calculate_fitness(self.best_solution, self.cities):
                self.best_solution = self.solution[:]

        return self.best_solution, (1 / calculate_fitness(self.best_solution, self.cities))
