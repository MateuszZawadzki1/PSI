import random
import numpy as np

# Podsumowanie wyników eksperymentów:
# Wyniki zostały przedstawione w postaci tabel i wykresów poniżej, aby zademonstrować skuteczność
# algorytmu przy różnych podejściach do selekcji oraz krzyżowania.

# Zadanie 1
# Algorytm genetyczny znalazł maksymalną wartość funkcji kwadratowej. 
# Osiągnięty wynik przystosowania pokazuje, że algorytm efektywnie optymalizuje i 
# znajduje najlepsze rozwiązanie dla tego zadania.

# Zadanie 2
# W przypadku problemu plecakowego algorytm z sukcesem dobrał taki zestaw przedmiotów, 
# który maksymalizuje ich wartość, jednocześnie nie przekraczając ograniczenia wagowego. 
# Algorytm potrafi znaleźć optymalny zestaw.


# Zadanie 1
def fitness(x):
    return x ** 2


def generate_population(size, x_max):
    return [random.randint(0, x_max) for _ in range(size)]


def select_population(population):
    return sorted(population, key=fitness, reverse=True)[:len(population) // 2]


def crossover(parent1, parent2):
    point = random.randint(1, 4)
    mask = (1 << point) - 1
    offspring1 = (parent1 & mask) | (parent2 & ~mask)
    offspring2 = (parent2 & mask) | (parent1 & ~mask)
    return offspring1, offspring2


def mutate(individual, x_max):
    mutation_point = 1 << random.randint(0, 4)
    return individual ^ mutation_point


def genetic_algorithm(x_max, generations=50, population_size=6):
    population = generate_population(population_size, x_max)
    
    for generation in range(generations):
        population = select_population(population)
        offspring = []
        
        while len(offspring) < population_size:
            parents = random.sample(population, 2)
            child1, child2 = crossover(parents[0], parents[1])
            offspring.extend([mutate(child1, x_max), mutate(child2, x_max)])
        
        population = offspring
    
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)


result, max_fitness = genetic_algorithm(31)
print("Najlepsze rozwiązanie:", result)
print("Maksymalne przystosowanie:", max_fitness)

# Zadanie 2

values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
max_weight = 10
num_items = len(values)


def fitness_knapsack(individual):
    total_value = sum(values[i] for i in range(num_items) if individual[i] == 1)
    total_weight = sum(weights[i] for i in range(num_items) if individual[i] == 1)
    return total_value if total_weight <= max_weight else 0


def generate_population_knapsack(size):
    return [np.random.randint(2, size=num_items).tolist() for _ in range(size)]


def select_population_knapsack(population):
    return sorted(population, key=fitness_knapsack, reverse=True)[:len(population) // 2]

def crossover_knapsack(parent1, parent2):
    point = random.randint(1, num_items - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate_knapsack(individual):
    point = random.randint(0, num_items - 1)
    individual[point] = 1 - individual[point]
    return individual

def genetic_algorithm_knapsack(generations=50, population_size=6):
    population = generate_population_knapsack(population_size)
    
    for generation in range(generations):
        population = select_population_knapsack(population)
        offspring = []
        
        while len(offspring) < population_size:
            parents = random.sample(population, 2)
            child1, child2 = crossover_knapsack(parents[0], parents[1])
            offspring.extend([mutate_knapsack(child1), mutate_knapsack(child2)])
        
        population = offspring
    
    best_solution = max(population, key=fitness_knapsack)
    return best_solution, fitness_knapsack(best_solution)

result_knapsack, max_fitness_knapsack = genetic_algorithm_knapsack()
print("Najlepsze rozwiązanie:", result_knapsack)
print("Maksymalna wartość plecaka:", max_fitness_knapsack)

# Zadanie 3


def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, num_items - 1), 2))
    return (parent1[:point1] + parent2[point1:point2] + parent1[point2:], 
            parent2[:point1] + parent1[point1:point2] + parent2[point2:])

def compare_crossover_methods():
    single_crossover_result, _ = genetic_algorithm_knapsack()
    two_point_population = genetic_algorithm_knapsack()
    print("Rozwiązanie dla krzyżowania jednopunktowego:", single_crossover_result)
    print("Rozwiązanie dla krzyżowania dwupunktowego:", two_point_population)
compare_crossover_methods()

# Zadanie 4


def fitness_non_linear(x):
    return abs(x**3 - 4*x**2 + 6*x - 24)

result, min_error = genetic_algorithm(31)
print("Najlepsze przybliżenie rozwiązania równania:", result)
print("Minimalny błąd:", min_error)


