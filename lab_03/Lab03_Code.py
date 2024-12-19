import random

def fitness_function(chromosome):
    x = int(chromosome, 2)  
    return x ** 2

def generate_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = ''.join(random.choice('01') for _ in range(chromosome_length))
        population.append(chromosome)
    return population

def roulette_wheel_selection(population):
    total_fitness = sum(fitness_function(chrom) for chrom in population)
    weights = [fitness_function(chrom) / total_fitness for chrom in population]
    selected = random.choices(population, weights=weights, k=len(population))
    return selected

def crossover(chromosome1, chromosome2):
    point = random.randint(1, len(chromosome1) - 1)
    offspring1 = chromosome1[:point] + chromosome2[point:]
    offspring2 = chromosome2[:point] + chromosome1[point:]
    return offspring1, offspring2

def mutation(chromosome, mutation_prob):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_prob:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return ''.join(chromosome)

def genetic_algorithm(population_size, chromosome_length, generations, mutation_prob, crossover_prob=1.0):
    population = generate_population(population_size, chromosome_length)
    best_fitness_history = []
    
    for generation in range(generations):
        population = roulette_wheel_selection(population)
        new_population = []
        
        for i in range(0, population_size, 2):
            parent1, parent2 = population[i], population[i+1]
            
            if random.random() < crossover_prob:
                offspring1, offspring2 = crossover(parent1, parent2)
            else:
                offspring1, offspring2 = parent1, parent2
                
            new_population.extend([mutation(offspring1, mutation_prob), mutation(offspring2, mutation_prob)])
        
        population = new_population
        best_chromosome = max(population, key=fitness_function)
        best_fitness = fitness_function(best_chromosome)
        best_fitness_history.append(best_fitness)
        print(f"Generation {generation + 1}: Best = {best_chromosome}, f(x) = {best_fitness}")

    best_chromosome = max(population, key=fitness_function)
    print(f"\nBest solution: x = {int(best_chromosome, 2)}, f(x) = {fitness_function(best_chromosome)}")
    return best_fitness_history

# Zadanie 1 Rozne parametry
print("\nZadanie 1 Rozne parametry")
# Test 1a Mala populacja wysokie, prawdopodobienstwo mutacji
print("\nTest 1a Mala populacja (6), wysoka mutacja (0.1)")
genetic_algorithm(population_size=6, chromosome_length=5, generations=10, mutation_prob=0.1)

# Test 1b Duza populacja, niskie prawdopodobieństwo mutacji
print("\nTest 1b Duza populacja (20), niska mutacja (0.01)")
genetic_algorithm(population_size=20, chromosome_length=5, generations=10, mutation_prob=0.01)

# Zadanie 2 Wplyw prawdopodobieństwa mutacji 
print("\nZadanie 2 Test riznych prawdopodobienstw mutacji")
mutation_probs = [0.01, 0.05, 0.1, 0.2]
for mp in mutation_probs:
    print(f"\nTest z prawdopodobienstwem mutacji: {mp}")
    genetic_algorithm(population_size=10, chromosome_length=5, generations=10, mutation_prob=mp)

# Zadanie 3 Bardzo mala populacja 
print("\nZadanie 3 Test bardzo malej populacji")
print("\nTest z populacja 2 osobnikow:")
genetic_algorithm(population_size=2, chromosome_length=5, generations=10, mutation_prob=0.01)

print("\nTest z populacja 4 osobnikow:")
genetic_algorithm(population_size=4, chromosome_length=5, generations=10, mutation_prob=0.01)

# Zadanie 4 Rozna liczba pokolen
print("\nZadanie 4: Testowanie roznej liczby pokolen")
generations_to_test = [10, 20, 50, 100]
for gen in generations_to_test:
    print(f"\nTest z liczba pokolen: {gen}")
    genetic_algorithm(population_size=10, chromosome_length=5, generations=gen, mutation_prob=0.01)