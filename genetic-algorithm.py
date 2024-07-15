import random
import numpy as np

def fitness(individual, person1, person2):
    # Calculate the fitness of an individual.
    sum_diff1 = sum(abs(a - b) for a, b in zip(individual[:len(person1)], person1))
    sum_diff2 = sum(abs(a - b) for a, b in zip(individual[len(person1):], person2))
    return sum_diff1 + sum_diff2

def generate_individual(person1, person2):
    # Generate a random individual.
    individual1 = random.sample(person1, len(person1))
    individual2 = random.sample(person2, len(person2))
    return individual1 + individual2

def mutate_individual(individual):
    # Mutate an individual by swapping two random elements within each part.
    i, j = random.sample(range(len(individual[:len(individual)//2])), 2)
    individual[i], individual[j] = individual[j], individual[i]
    i, j = random.sample(range(len(individual)//2, len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

def crossover(parent1, parent2):
    # Perform crossover (recombination) between two parents.
    crossover_point1 = random.randint(1, len(parent1)//2 - 1)
    crossover_point2 = random.randint(1, len(parent2)//2 - 1)
    offspring1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point1+len(parent1)//2] + parent1[crossover_point1+len(parent1)//2:]
    offspring2 = parent2[:crossover_point2] + parent1[crossover_point2:crossover_point2+len(parent2)//2] + parent2[crossover_point2+len(parent2)//2:]
    return offspring1, offspring2

def genetic_algorithm(person1, person2, population_size=500, generations=500):
    # Run the genetic algorithm.
    population = [generate_individual(person1, person2) for _ in range(population_size)]
    for _ in range(generations):
        fitness_values = [fitness(individual, person1, person2) for individual in population]
        fittest_individual = population[np.argmin(fitness_values)]
        fittest_fitness = min(fitness_values)
        print(f'Generation {_+1}: Fittest individual {fittest_individual[:len(person1)]} | {fittest_individual[len(person1):]} with fitness {fittest_fitness}')
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate_individual(offspring1), mutate_individual(offspring2)])
        population = new_population
    return fittest_individual, fittest_fitness

# Example usage
person1 = [int(x) for x in '316245'][0:3] + [int(x) for x in '112121'][3:6]  # Bsp. S.39
person2 = [int(x) for x in '112121'][0:3] + [int(x) for x in '121212'][3:6]  # Bsp. S.39
fittest_individual, fittest_fitness = genetic_algorithm(person1, person2)
print(f'Fittest individual: {fittest_individual[:len(person1)]} | {fittest_individual[len(person1):]} with fitness {fittest_fitness}')