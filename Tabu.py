import random

from utils.Calc import calculate_fitness, generate_cities


class Tabu:
    def __init__(self, num_cities=20, map_size=200, cities=None):
        self.map_size = map_size

        if cities is None:
            self.num_cities = num_cities
            self.cities = generate_cities(num_cities, map_size)
        else:
            self.cities = cities
            self.num_cities = len(cities)

        self.solution = self.initialize(self.num_cities)
        self.best_solution = self.solution[:]  # Initial solution, the best solution so far
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
            # Swap the current element with all subsequent elements
            for j in range(i + 1, len(solution)):
                # Create a neighbor solution by swapping elements and add them to a list
                neighbor = solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def start(self, num_iterations, num_neighbors):
        for _ in range(num_iterations):
            # Generate neighbor solutions and sort them by fitness in descending order
            neighbors = Tabu.generate_neighbors(self.solution)
            neighbors.sort(key=lambda x: -calculate_fitness(x, self.cities))
            found = False

            # Finding the best neighbor
            for neighbor in neighbors:

                # If the neighbor is better than the current best solution and it is not in the tabu list
                # or if it has a higher fitness than the best solution found so far
                if neighbor not in self.tabu_list or calculate_fitness(neighbor, self.cities) > calculate_fitness(
                        self.best_solution, self.cities):
                    # Update the best solution
                    self.solution = neighbor
                    # Add it to the tabu list
                    self.tabu_list.append(neighbor)

                    # If length of tabu list is greater than max length of tabu list
                    if len(self.tabu_list) > num_neighbors:
                        # Remove the first element
                        self.tabu_list.pop(0)

                    found = True
                    break

            # If no better solution was found in this iteration, exit the loop
            if not found:
                break

            # If a better solution was found, update the best solution
            if calculate_fitness(self.solution, self.cities) > calculate_fitness(self.best_solution, self.cities):
                self.best_solution = self.solution[:]

        return self.best_solution, (1 / calculate_fitness(self.best_solution, self.cities))
