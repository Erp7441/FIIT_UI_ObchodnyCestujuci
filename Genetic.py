import random
from utils.Calc import calculate_fitness

# TODO:: stop algo after certain amount of generations
# TODO:: add mutation probability
# TODO:: add elitism


class Genetic:
    def __init__(self, num_cities=20, map_size=200):
        self.num_cities = num_cities
        self.map_size = map_size
        self.cities = [(random.randint(0, map_size), random.randint(0, map_size)) for _ in range(num_cities)]

    @staticmethod
    def initialize(num_individuals, num_cities):
        population = [list(range(num_cities)) for _ in range(num_individuals)]
        for individual in population:
            random.shuffle(individual)
        return population

    # Roulette selection
    def select_parents(self, population, num_parents):
        parents = []
        fitness_values = [calculate_fitness(ind, self.cities) for ind in population]
        total_fitness = sum(fitness_values)
        for _ in range(num_parents):
            rand_val = random.uniform(0, total_fitness)
            cumulative_fitness = 0
            for ind, fitness_val in zip(population, fitness_values):
                cumulative_fitness += fitness_val
                if cumulative_fitness >= rand_val:
                    parents.append(ind)
                    break
        return parents

    # Two-point crossover
    @staticmethod
    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [-1] * len(parent1)
        for i in range(start, end + 1):
            child[i] = parent1[i]
        remaining = [item for item in parent2 if item not in child]
        for i in range(len(parent1)):
            if child[i] == -1:
                child[i] = remaining.pop(0)
        return child

    # Mutation by swapping two places in solution
    @staticmethod
    def mutate(individual):
        index1, index2 = random.sample(range(len(individual)), 2)
        # TODO:: Add probability condiiton
        individual[index1], individual[index2] = individual[index2], individual[index1]

    def start(self, num_generations, num_individuals):
        population = Genetic.initialize(num_individuals, len(self.cities))

        for _ in range(num_generations):
            parents = self.select_parents(population, num_individuals)
            children = []
            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1 = Genetic.crossover(parent1, parent2)
                child2 = Genetic.crossover(parent2, parent1)
                Genetic.mutate(child1)
                Genetic.mutate(child2)
                children.extend([child1, child2])
            population = children

        best_individual = max(population, key=lambda ind: calculate_fitness(ind, self.cities))
        best_distance = 1 / calculate_fitness(best_individual, self.cities)

        return best_individual, best_distance
