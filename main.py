from Genetic import Genetic
from Tabu import Tabu
from utils.Graph import Graph
from utils.ParentType import ParentType
from utils.Timer import Timer
from utils.Calc import generate_cities
from utils.Args import Args


def main():
    args = Args()

    if args.default_tests:
        run_default_tests()
        return

    if args.gen_run:
        if args.p_type == "ALL":
            start_gen(ParentType.ROULETTE, args.num_generations, args.num_individuals, args.num_cities, args.map_size, args.cities, args.num_elites)
            start_gen(ParentType.ELITIST, args.num_generations, args.num_individuals, args.num_cities, args.map_size,  args.cities, args.num_elites)

        start_gen(args.p_type, args.num_generations, args.num_individuals, args.num_cities, args.map_size, args.cities, args.num_elites)

    if args.tabu_run:
        start_tabu(args.num_iterations, args.num_neighbors, args.num_cities, args.map_size, args.cities)


def run_default_tests():
    ####################################################
    # Random set of cities each time
    ####################################################

    print('####################################################')
    print('Random set of cities each time')
    print('####################################################')
    start_gen(ParentType.ROULETTE)
    start_gen(ParentType.ELITIST)
    start_tabu()

    ####################################################
    # Random set of cities each time (with bounderies)
    ####################################################

    print('\n\n####################################################')
    print("Random set of cities each time (with bounderies)")
    print('####################################################')
    start_gen(ParentType.ROULETTE, num_generations=2000, num_individuals=100, num_cities=30)
    start_gen(ParentType.ELITIST, num_generations=2000, num_individuals=100, num_cities=30, num_elites=10)
    start_tabu(num_iterations=2000, num_neighbors=20, num_cities=30)

    ####################################################
    # Specific set of cities
    ####################################################

    print('\n\n####################################################')
    print("Specific set of cities")
    print('####################################################')
    map_size = 200
    cities = generate_cities(20, map_size)

    start_gen(ParentType.ROULETTE, map_size=map_size, cities=cities)
    start_gen(ParentType.ELITIST, map_size=map_size, cities=cities)
    start_tabu(map_size=map_size, cities=cities)


def start_gen(p_type: ParentType, num_generations=None, num_individuals=None, num_cities=None, map_size=None, cities=None, num_elites=None):
    ####################################################
    # Default arguments values
    ####################################################
    if num_generations is None:
        num_generations = 1000
    if num_individuals is None:
        num_individuals = 50
    if num_cities is None and cities is None:
        num_cities = 20
    if map_size is None:
        map_size = 200
    if num_elites is None:
        num_elites = 4
    if p_type is None or p_type not in ParentType:
        p_type = ParentType.ELITIST


    ####################################################
    # Main execution
    ####################################################
    title = "\nGenetic algorithm ({})".format(p_type.name)
    timer = Timer()

    print(title)

    if cities:
        gen = Genetic(p_type, map_size=map_size, cities=cities, num_elites=num_elites)
    else:
        gen = Genetic(p_type, num_cities=num_cities, map_size=map_size, num_elites=num_elites)

    timer.start()
    best_path, best_distance = gen.start(num_generations, num_individuals)
    timer.stop()

    print('Map size:', gen.map_size)
    print('Number of cities:', gen.num_cities)
    print('Number of individuals:', num_individuals)
    print('Number of generations:', num_generations)
    print('Number of same generations:', gen.num_of_same_gens)

    if p_type == ParentType.ELITIST:
        print('Number of elites:', gen.num_elites)

    print("Best path:", best_path)
    print("Path length:", best_distance)
    print("Time:", str(timer.elapsed_time) + "s")

    graph_gen = Graph(best_path, gen.cities, title)
    graph_gen.plot()


def start_tabu(num_iterations=None, num_neighbors=None, num_cities=None, map_size=None, cities=None):

    ####################################################
    # Default arguments values
    ####################################################
    if num_iterations is None:
        num_iterations = 1000
    if num_neighbors is None:
        num_neighbors = 10
    if num_cities is None and cities is None:
        num_cities = 20
    if map_size is None:
        map_size = 200

    ####################################################
    # Main execution
    ####################################################
    timer = Timer()
    print("\nTabu search algorithm")

    if cities:
        tabu = Tabu(map_size=map_size, cities=cities)
    else:
        tabu = Tabu(num_cities=num_cities, map_size=map_size)

    timer.start()
    best_path, best_distance = tabu.start(num_iterations, num_neighbors)
    timer.stop()

    print('Map size:', tabu.map_size)
    print('Number of cities:', tabu.num_cities)
    print('Number of iterations:', num_iterations)
    print('Number of neighbors:', num_neighbors)
    print("Best path:", best_path)
    print("Path length:", best_distance)
    print("Time:", str(timer.elapsed_time) + "s")

    graph_tabu = Graph(best_path, tabu.cities, "Tabu search algorithm")
    graph_tabu.plot()


if __name__ == "__main__":
    main()
