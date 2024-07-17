import random
import numpy as np
import matplotlib.pyplot as plt #pip install matplotlib


def generate_individual(person1, person2):
    # Generate a random individual by concatenating two random permutations
    individual1 = random.sample(person1, len(person1))
    individual2 = random.sample(person2, len(person2))
    return individual1 + individual2

def mutate_individual(individual):
    # Mutate an individual by swapping two random elements within each part
    i, j = random.sample(range(len(individual)//2), 2)
    individual[i], individual[j] = individual[j], individual[i]
    i, j = random.sample(range(len(individual)//2, len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

def crossover(parent1, parent2):
    # Perform crossover (recombination) between two parents
    crossover_point1 = random.randint(1, len(parent1)//2 - 1)
    crossover_point2 = random.randint(1, len(parent2)//2 - 1)
    offspring1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point1+len(parent1)//2] + parent1[crossover_point1+len(parent1)//2:]
    offspring2 = parent2[:crossover_point2] + parent1[crossover_point2:crossover_point2+len(parent2)//2] + parent2[crossover_point2+len(parent2)//2:]
    return offspring1, offspring2


def fitness(individual, person1, person2, safety_distance, process_duration):
    # Check if all safety distances are greater than the minimum safety distance
    travel_time = 5  # example travel time
    processing_times = [10, 20, 30, 40, 50, 60]  # example processing times


    #output = [3, 6, 1, 6, 1, 6]  # task sequence
    robot_assignment = [1, 1, 1, 2, 2, 1]  # robot assignment for each task
    #offspring1, offspring2 = crossover  
    output = (individual[:len(person1)], person1)
    #robot_assignment = (individual[len(person1):], person1)
    
    total_time_robot1 = 0
    total_time_robot2 = 0


    for i, (task, _) in enumerate(zip(output[0], output[1])):
        station = task
        #print (station)
        #robot = zip(robot_assignment[0], robot_assignment[1])
        robot = robot_assignment
        if robot == 1:
            total_time_robot1 += processing_times[int (station) - 1]  # subtract 1 because station indices start at 1
        if i < len(output) - 1 and robot_assignment[i + 1] == 1:
                total_time_robot1 += travel_time  # add travel time if not at the last station and next task is also for robot 1
        else:
            total_time_robot2 += travel_time  # add travel time if not at the last station and next task is also for robot 2
    
    #savety part
    total_processing_time = (total_time_robot1 + total_time_robot2)
    if len(set(output[0])) != len(output[0]):  # check if there are duplicates
        return f'Invalid individual: duplicate task. fitness: {total_processing_time}'
    else:
        return total_processing_time

def genetic_algorithm(person1, person2, safety_distance, process_duration, population_size=1000, generations=10000):
    # Run the genetic algorithm
    population = [generate_individual(person1, person2) for _ in range(population_size)]
    fitness_values = []
    for _ in range(generations):
        fitness_values_generation = [fitness(individual, person1, person2, safety_distance, process_duration) for individual in population]
        fitness_values.extend(fitness_values_generation)
        fittest_individual = population[np.argmin(fitness_values_generation)]
        fittest_fitness = min(fitness_values_generation)
        print(f'Generation {_+1}: Fittest individual {fittest_individual[:len(person1)]} | {fittest_individual[len(person1):]} with fitness {fittest_fitness}')
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population, 2)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate_individual(offspring1), mutate_individual(offspring2)])
        population = new_population
        
        # Plot the fitness values
        plt.clf()
        plt.plot(fitness_values)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Fitness Values Over Generations')
        plt.pause(0.01)
    
    return fittest_individual, fittest_fitness

# Example usage
person1 = [int(x) for x in '316245'][0:3] + [int(x) for x in '112121'][3:6]  # Bsp. S.39
person2 = [int(x) for x in '112121'][0:3] + [int(x) for x in '121212'][3:6]  # Bsp. S.39
safety_distance = 1  # Minimum safety distance
process_duration = [5, 3, 4, 2, 6, 1]  # Process duration for each task
number_of_robots = 2  # Number of available robots

plt.ion()  # Turn on interactive mode
fittest_individual, fittest_fitness = genetic_algorithm(person1, person2, safety_distance, process_duration)
plt.ioff()  # Turn off interactive mode
plt.show()
print(f'Fittest individual: {fittest_individual[:len(person1)]} | {fittest_individual[len(person1):]} with fitness {fittest_fitness}')