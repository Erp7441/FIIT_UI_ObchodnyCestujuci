# Fitnes funkcia - Ohodnoti clena populacie nejakym indexom

# Pseudo kod GA
# 0. Start
# 1. Fitnes (vyhodnotenie kazdeho chromozomu v populacii)
# 2. Reprodukcia
    # 2.0 Vyber (Zalozeny na fitnes value)
    # 2.1 Rekombinacia (Krizenie chromozomov)
    # 2.2 Mutacia (Mutacia chromozomov (na zakladne nejakej pravdepodobnostnej value))
    # 2.3 Prijatie (Remove alebo accept novy chromozom)
# 3. Nahrada (Nahradenie starej populacie novou)
# 4. Test (Testovanie ci sa mi riesenie nachadza v novej populacii)
# 5. Loop (Opakuj 1-4 dokym nejaky chromozom prejde uspesne testom [diskutabilne])

# Problemy GA
# 1. Metoda kodovania
# 2. Procedura incializacie
# 3. Vyhodnocovanie fitnes
# 4. Vyber rodicov
# 5. Geneticke operatory?
# 6. Nastavenie parametrov

from Genetic import Genetic
from Tabu import Tabu
from utils.Graph import Graph


def main():

    # TODO:: Add running on a single set of cities
    # TODO:: Add timer
    start_gen()
    start_tabu()


def start_gen():
    print("Genetic algorithm")
    gen = Genetic()
    best_path, best_distance = gen.start(num_generations=1000, num_individuals=50)
    print("Best path:", best_path)
    print("Path length:", best_distance)

    graph_gen = Graph(best_path, "Genetic algorithm")
    graph_gen.plot()


def start_tabu():
    print("\nTabu search")
    tabu = Tabu()
    best_path, best_distance = tabu.start(num_iterations=1000, num_neighbors=10)
    print("Best path:", best_path)
    print("Path length:", best_distance)

    graph_tabu = Graph(best_path, "Tabu search")
    graph_tabu.plot()

if __name__ == "__main__":
    main()
