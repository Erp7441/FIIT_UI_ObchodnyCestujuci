from argparse import ArgumentParser


class ArgsParser(ArgumentParser):
    def format_help(self):
        default_help = super().format_help()
        custom_help = """\n
Default values:

- General:
  num_cities = 20
  map_size = 200
  cities = None
  generate_cities = False

- Genetic algorithm:
  num_generations = 1000
  num_individuals = 50
  cities = None
  num_elites = 4
  parent_type = ELITIST

- Tabu search algorithm:
  num_iterations = 1000
  num_neighbors = 10
  
  
Examples of use:

1. Genetic algorithm:
main.py --gen

2. Tabu algorithm:
main.py --tabu

3. Both algorithms:
main.py --gen --tabu

4. Genetic algorithm with 30 cities:
main.py --gen --num-cities 30

5. Both algorithms with 30 cities and 20 neighbors and tabu with 20 neighbors, 2000 iterations, and genetic algorithm with ELITIST parent selection type:
main.py --gen --tabu --num-cities 30 --num-neighbors 20 --num-iterations 2000 --parent-type ELITIST

6. Both algorithms with 30 cities and 20 neighbors, 2000 iterations, genetic algorithm with ELITIST parent selection type, and 10 elites:
main.py --gen --tabu --num-cities 30 --num-neighbors 20 --num-iterations 2000 --parent-type ELITIST --num-elites 10

7. Genetic algorithm with ELITIST parent selection, 18 elites, 1000 generations, and 100 individuals:
main.py --gen --parent-type ELITIST --num-elites 18 --num-generations 1000 --num-individuals 100

8. Tabu algorithm with 500 iterations and 10 neighbors:
main.py --tabu --num-iterations 500 --num-neighbors 10

9. Genetic algorithm with ROULETTE parent selection, 500 generations, and 50 individuals, and tabu with 1000 iterations and 20 neighbors:
main.py --gen --parent-type ROULETTE --num-generations 500 --num-individuals 50 --tabu --num-iterations 1000 --num-neighbors 20

10. Genetic algorithm with 30 cities and a map size of 300:
main.py --gen --num-cities 30 --map-size 300

11. Tabu algorithm with 30 cities and a map size of 300:
main.py --tabu --num-cities 30 --map-size 300

12. Default tests:
main.py --run-default-tests

13. Both algorithms with 40 cities, a map size of 400, For generation Both ELITIST and ROULETTE parent selections, 15 elites, 500 generations, and 50 individuals, For tabu 1000 iterations, 20 neighbors:
main.py --gen --parent-type ALL --num-elites 15 --num-generations 500 --num-individuals 50 --tabu --num-iterations 1000 --num-neighbors 50 --num-cities 40 --map-size 400

14. 38 cities with exact coordinates. Both algorithms with map size of 1000, For generation Both ELITIST and ROULETTE parent selections, 15 elites, 500 generations, and 50 individuals, For tabu 1000 iterations, 20 neighbors:
main.py --gen --parent-type ALL --num-elites 15 --num-generations 500 --num-individuals 50 --tabu --num-iterations 1000 --num-neighbors 20 --map-size 1000 --cities "[(100, 700), (450, 200), (800, 900), (350, 100), (600, 750), (200, 550), (750, 400), (950, 300), (300, 600), (700, 100), (50, 900), (850, 250), (500, 800), (150, 450), (900, 50), (650, 350), (250, 850), (400, 600), (550, 200), (950, 750), (100, 100), (200, 200), (300, 300), (400, 400), (500, 500), (600, 600), (700, 700), (800, 800), (900, 900), (100, 900), (200, 800), (300, 700), (400, 600), (500, 500), (600, 400), (700, 300), (800, 200), (900, 100)]"

15. Both algorithms with SAME DATASET of 40 cities, a map size of 400, For generation Both ELITIST and ROULETTE parent selections, 15 elites, 500 generations, and 50 individuals, For tabu 1000 iterations, 20 neighbors:
main.py --gen --parent-type ALL --num-elites 15 --num-generations 500 --num-individuals 50 --tabu --num-iterations 1000 --num-neighbors 50 --num-cities 40 --map-size 400 --generate-cities

"""
        return default_help + custom_help
