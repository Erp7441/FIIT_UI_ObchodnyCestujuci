import random

from utils.Calc import calculate_fitness
from utils.ParentType import ParentType
from utils.Constants import PROBABILITY_OF_MUTATION


class Genetic:
    def __init__(self, p_type: ParentType, num_cities=20, map_size=200, probability=None, num_of_same_gens=5, cities=None, num_elites=None):
        self.probability = PROBABILITY_OF_MUTATION if probability is None else probability
        self.map_size = map_size

        if cities is None:
            self.num_cities = num_cities
            self.cities = [(random.randint(0, map_size), random.randint(0, map_size)) for _ in range(num_cities)]
        else:
            self.cities = cities
            self.num_cities = len(self.cities)

        self.p_type = p_type
        self.num_elites = num_elites if p_type is ParentType.ELITIST else None
        self.num_of_same_gens = num_of_same_gens

    @staticmethod
    def initialize_population(num_individuals, num_cities):
        population = [list(range(num_cities)) for _ in range(num_individuals)]
        for individual in population:
            random.shuffle(individual)
        return population

    def select_parents(self, population, num_parents):
        if self.p_type == ParentType.ROULETTE:
            return self.roulette_select_parents(population, num_parents)
        elif self.p_type == ParentType.ELITIST:
            return self.elitist_select_parents(population, num_parents)

    def elitist_select_parents(self, population, num_parents):
        if len(population) < num_parents:
            return population

        num_elites = 4 if self.num_elites is None else self.num_elites

        # Sorting by fitness value (Best individuals at the beginning)
        population.sort(key=lambda ind: calculate_fitness(ind, self.cities), reverse=True)

        # Choosing elite parents
        elite_parents = population[:num_elites]

        # Rest is chosen via roulette
        remaining_parents = self.roulette_select_parents(population, num_parents - num_elites)

        return elite_parents + remaining_parents

    def roulette_select_parents(self, population, num_parents):
        if len(population) < num_parents:
            return population

        parents = []
        fitness_values = [calculate_fitness(ind, self.cities) for ind in population]
        total_fitness = sum(fitness_values)

        for _ in range(num_parents):
            # Generating random value between 0 and total fitness of the population
            rand_val = random.uniform(0, total_fitness)

            # Finding the first individual whose fitness value is greater than or equal to the random value
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
    def mutate(self, individual):
        if random.random() > self.probability:
            return

        index1, index2 = random.sample(range(len(individual)), 2)
        individual[index1], individual[index2] = individual[index2], individual[index1]

    def start(self, num_generations, num_individuals):
        population = Genetic.initialize_population(num_individuals, len(self.cities))
        no_evolve_counter = 0

        for _ in range(num_generations):
            if no_evolve_counter == self.num_of_same_gens:
                break

            parents = self.select_parents(population, num_individuals)
            children = []

            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                child1 = Genetic.crossover(parent1, parent2)
                child2 = Genetic.crossover(parent2, parent1)
                self.mutate(child1)
                self.mutate(child2)
                children.extend([child1, child2])

                if population == children:
                    no_evolve_counter += 1

            population = children

        best_individual = max(population, key=lambda ind: calculate_fitness(ind, self.cities))
        best_distance = 1 / calculate_fitness(best_individual, self.cities)

        return best_individual, best_distance
