import random

def genetic_knapsack(weights, values, max_weight, population_size=20, generations=5, mutation_rate=0.2, crossover_probability=0.75):
    n = len(weights)

    # Funkcja fitness obliczająca wartość rozwiązania i sprawdzająca ograniczenie wagowe
    def fitness(individual):
        total_weight = sum(individual[i] * weights[i] for i in range(n))
        total_value = sum(individual[i] * values[i] for i in range(n))
        if total_weight > max_weight:
            return 0  # Przekroczenie maksymalnej wagi
        return total_value

    # Tworzenie początkowej populacji
    def create_individual():
        return [random.randint(0, 1) for _ in range(n)]

    population = [create_individual() for _ in range(population_size)]

    # Krzyżowanie dwóch rodziców
    def crossover(parent1, parent2):
        point = random.randint(1, n - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    # Mutacja jednego osobnika
    def mutate(individual):
        for i in range(n):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]  # Zamiana 0 na 1 lub 1 na 0

    # Algorytm genetyczny
    for generation in range(generations):
        print(f"Pokolenie {generation + 1}:")
        
        # Ocena populacji
        population = sorted(population, key=fitness, reverse=True)
        print("Najlepszy osobnik w tym pokoleniu:", population[0], "Wartość:", fitness(population[0]))

        # Elitarna selekcja (zachowanie najlepszego osobnika)
        next_generation = population[:2]

        # Tworzenie nowej populacji
        for i in range(0, population_size - 2, 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            # Sprawdzenie prawdopodobieństwa krzyżowania
            if random.random() <= crossover_probability:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1[:], parent2[:]

            mutate(child1)
            mutate(child2)
            next_generation.extend([child1, child2])

        population = next_generation

    # Najlepsze rozwiązanie
    best_individual = max(population, key=fitness)
    best_value = fitness(best_individual)
    selected_items = [i + 1 for i in range(n) if best_individual[i] == 1]

    print("Finalne rozwiązanie: ", best_individual, "Wartość:", best_value)

    return best_value, selected_items

# Dane z zestawu 14
weights = [6, 14, 3, 8, 17, 6, 4, 9, 15, 4]
values = [12, 5, 8, 14, 12, 6, 8, 10, 8, 12]
max_weight = 65

# Rozwiązanie problemu plecakowego
max_value, selected_items = genetic_knapsack(weights, values, max_weight)

# Zwracanie wyników
result = {
    "Maksymalna wartość": max_value,
    "Wybrane przedmioty": selected_items
}

print(result)
