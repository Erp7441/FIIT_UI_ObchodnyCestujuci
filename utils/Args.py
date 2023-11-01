import os
import signal
from ast import literal_eval
from utils.ArgsParser import ArgsParser


class Args:

    def __init__(self):
        # Parsing arguments
        self.parser = ArgsParser(
            description="UI Traveling merchant by Martin Szabo",

        )

        tabu_group = self.parser.add_argument_group("Tabu search algorithm")
        tabu_group.add_argument("--tabu", action="store_true", dest="tabu_run", help="Run tabu search algorithm")
        tabu_group.add_argument("--num-iterations", type=int, dest="num_iterations", help="Number of iterations",  metavar="INTEGER")
        tabu_group.add_argument("--num-neighbors", type=int, dest="num_neighbors", help="Number of neighbors",  metavar="INTEGER")

        gen_group = self.parser.add_argument_group("Genetic algorithm")
        gen_group.add_argument("--gen", action="store_true", dest="gen_run", help="Run genetic algorithm")
        gen_group.add_argument("--parent-type", type=str, dest="p_type", help="Type of parent selection to use", choices=["ELITIST", "ROULETTE", "ALL"])
        gen_group.add_argument("--num-generations", type=int, dest="num_generations", help="Number of generations per run", metavar="INTEGER")
        gen_group.add_argument("--num-individuals", type=int, dest="num_individuals", help="Number of individuals per generation", metavar="INTEGER")
        gen_group.add_argument("--num-elites", type=int, dest="num_elites", help="Number of elite parents to choose", metavar="INTEGER")

        self.parser.add_argument("--num-cities", type=int, dest="num_cities", help="Number of cities", metavar="INTEGER")
        self.parser.add_argument("--map-size", type=int, dest="map_size", help="Map size", metavar="INTEGER")
        self.parser.add_argument("--cities", type=str, dest="cities", help="List of tuples containing coordinates", metavar="LIST OF TUPLES")
        self.parser.add_argument("--generate-cities", action="store_true", dest="generate_cities", help="Generate same cities dataset for all algorithms")

        tests_group = self.parser.add_argument_group("Tests")
        tests_group.add_argument("--run-default-tests", action="store_true", dest="default_tests", help="Run default tests")

        args_dict = self.parser.parse_args().__dict__

        for k, v in args_dict.items():
            setattr(self, k, v)

        if self.cities is not None:
            self.cities = literal_eval(self.cities)

    def parse_int(self, arg, default_value):
        value = self.__convert_arg_to_int(arg)
        value = value if value is not None else default_value
        return value

    def __convert_arg_to_int(self, arg):
        if arg is not None:
            try:
                return int(arg)
            except ValueError:
                print("Could not convert argument value \"{}\" to integer value!".format(arg))
                if not self.__get_confirmation():
                    pid = os.getpid()
                    os.kill(pid, signal.SIGTERM)
                print("Using default value...\n")
                return None

    @staticmethod
    def __get_confirmation():
        response = ''
        while response != 'Y' and response != 'N':
            print("Do you wish to continue? (y/n): ", end='')
            response = input().upper()
        return response == 'Y'