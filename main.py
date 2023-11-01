from Genetic import Genetic
from Tabu import Tabu
from utils.Graph import Graph
from utils.ParentType import ParentType


def main():

    # TODO:: Add running on a single set of cities
    # TODO:: Add timer
    start_gen()
    start_tabu()


def start_gen():
    print("Genetic algorithm (Elitist)")
    gen = Genetic(ParentType.ELITIST)
    best_path, best_distance = gen.start(num_generations=1000, num_individuals=50)
    print("Best path:", best_path)
    print("Path length:", best_distance)

    graph_gen = Graph(best_path, gen.cities, "Genetic algorithm (Elitist)")
    graph_gen.plot()

    print("\nGenetic algorithm (Roulette)")
    gen = Genetic(ParentType.ROULETTE)
    best_path, best_distance = gen.start(num_generations=1000, num_individuals=50)
    print("Best path:", best_path)
    print("Path length:", best_distance)

    graph_gen = Graph(best_path, gen.cities, "Genetic algorithm (Roulette)")
    graph_gen.plot()


def start_tabu():
    print("\nTabu search")
    tabu = Tabu()
    best_path, best_distance = tabu.start(num_iterations=1000, num_neighbors=10)
    print("Best path:", best_path)
    print("Path length:", best_distance)

    graph_tabu = Graph(best_path, tabu.cities, "Tabu search")
    graph_tabu.plot()


if __name__ == "__main__":
    main()
