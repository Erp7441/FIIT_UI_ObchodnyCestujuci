from Genetic import Genetic
from Tabu import Tabu
from utils.Graph import Graph
from utils.ParentType import ParentType
from utils.Timer import Timer
from utils.Calc import generate_cities, calculate_path_value
from utils.Args import Args
from utils.Constants import ROUNDING_PRECISION


def main():
    args = Args()
    runs = []

    if args.default_tests:
        run_default_tests()
        return

    if args.generate_cities and args.cities is None:
        try:
            args.cities = generate_cities(args.num_cities, args.map_size)
        except Exception as e:
            print("\033[91mERROR: Failed generating cities check \"num_cities\" and \"map_size\" args\033[0m")
            raise e

    if args.gen_run:
        if args.p_type == "ALL":
            runs.append(start_gen(ParentType.ROULETTE, args.num_generations, args.num_individuals, args.num_cities, args.map_size, args.cities, args.num_elites))
            runs.append(start_gen(ParentType.ELITIST, args.num_generations, args.num_individuals, args.num_cities, args.map_size,  args.cities, args.num_elites))
        else:
            runs.append(start_gen(args.p_type, args.num_generations, args.num_individuals, args.num_cities, args.map_size, args.cities, args.num_elites))

    if args.tabu_run:
        runs.append(start_tabu(args.num_iterations, args.num_neighbors, args.num_cities, args.map_size, args.cities))

    print_runs(runs)


def print_runs(runs: list):
    evaluate_best_runs(runs)

    for i, run in enumerate(runs):
        print(str(i+1) + ':', "\033[93m" + run.get("name") + "\033[0m")
        print('Map size:', run.get("map_size"))
        print('Number of cities:', run.get("num_cities"))

        # Specific to genetic algorithm
        if run.get("num_individuals") is not None:
            print('Number of individuals:', run.get("num_individuals"))
        if run.get("num_generations") is not None:
            print('Number of generations:', run.get("num_generations"))
        if run.get("num_of_same_gens") is not None:
            print('Number of same generations:', run.get("num_of_same_gens"))

        # Specific to genetic algorithm elite parents selection
        if run.get("num_elites") is not None:
            print('Number of elites:', run.get("num_elites"))

        # Specific to tabu algorithm
        if run.get("num_iterations") is not None:
            print('Number of iterations:', run.get("num_iterations"))
        if run.get("num_neighbors") is not None:
            print('Number of neighbors:', run.get("num_neighbors"))

        print('Best path:', run.get("best_path"))
        print('Path length:', run.get("path_length"))
        print('Time:', run.get("time").replace('\033[0m', 's\033[0m'))
        print('\n', end='')

        run.get('graph').plot()


def evaluate_best_runs(runs: list):
    best_path_length_index = None
    best_time_index = None
    best_path_index = None

    for i, run in enumerate(runs):
        if best_path_length_index is None or run.get("path_length") < runs[best_path_length_index].get("path_length"):
            best_path_length_index = i
        if best_time_index is None or run.get("time") < runs[best_time_index].get("time"):
            best_time_index = i
        if best_path_index is None or calculate_path_value(run) < calculate_path_value(runs[best_path_index]):
            best_path_index = i

    for i, run in enumerate(runs):
        if i != best_path_length_index:
            run["path_length"] = "\033[91m" + str(run.get("path_length")) + "\033[0m"
        else:
            run["path_length"] = "\033[92m" + str(run.get("path_length")) + "\033[0m"
        if i != best_time_index:
            run["time"] = "\033[91m" + str(run.get("time")) + "\033[0m"
        else:
            run["time"] = "\033[92m" + str(run.get("time")) + "\033[0m"
        if i != best_path_index:
            run["best_path"] = "\033[91m" + str(run.get("best_path")) + "\033[0m"
        else:
            run["best_path"] = "\033[92m" + str(run.get("best_path")) + "\033[0m"


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
    # Random set of cities each time (with boundaries)
    ####################################################

    print('\n\n####################################################')
    print("Random set of cities each time (with boundaries)")
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
    title = "Genetic algorithm ({})".format(p_type.name)
    timer = Timer()

    if cities:
        gen = Genetic(p_type, map_size=map_size, cities=cities, num_elites=num_elites)
    else:
        gen = Genetic(p_type, num_cities=num_cities, map_size=map_size, num_elites=num_elites)

    timer.start()
    best_path, best_distance = gen.start(num_generations, num_individuals)
    timer.stop()

    stats = {
        "name": title,
        "map_size": gen.map_size,
        "num_cities": gen.num_cities,
        "cities": gen.cities,
        "num_individuals": num_individuals,
        "num_generations": num_generations,
        "num_of_same_gens": gen.num_of_same_gens,
        "best_path": best_path,
        "path_length": round(best_distance, ROUNDING_PRECISION),
        "time": timer.elapsed_time,
        "graph": Graph(best_path, gen.cities, title)
    }

    if p_type == ParentType.ELITIST:
        stats["num_elites"] = gen.num_elites

    return stats


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

    if cities:
        tabu = Tabu(map_size=map_size, cities=cities)
    else:
        tabu = Tabu(num_cities=num_cities, map_size=map_size)

    timer.start()
    best_path, best_distance = tabu.start(num_iterations, num_neighbors)
    timer.stop()

    stats = {
        "name": "Tabu search algorithm",
        "map_size": tabu.map_size,
        "num_cities": tabu.num_cities,
        "cities": tabu.cities,
        "num_iterations": num_iterations,
        "num_neighbors": num_neighbors,
        "best_path": best_path,
        "path_length": round(best_distance, ROUNDING_PRECISION),
        "time": timer.elapsed_time,
        "graph": Graph(best_path, tabu.cities, "Tabu search algorithm")
    }

    return stats


if __name__ == "__main__":
    main()
