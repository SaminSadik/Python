def objective_function(solution):
    return sum(solution)

def generate_neighbor(current_solution, index):
    neighbor = current_solution[:]
    neighbor[index] = 1 - neighbor[index]
    return neighbor

def hill_climbing(current_solution):
    current_fitness = objective_function(current_solution)
    iterations = min(len(current_solution), 5)
    for i in range(iterations):
        neighbor = generate_neighbor(current_solution, i)
        neighbor_fitness = objective_function(neighbor)
        if neighbor_fitness >= current_fitness:
            current_solution = neighbor
            current_fitness = neighbor_fitness
    return current_solution, current_fitness

input_str = input("Enter initial solution (e.g. 10110): ")
initial_solution = [int(bit) for bit in input_str]
best_solution, best_fitness = hill_climbing(initial_solution)
print("Best Solution:", best_solution, "- Fitness:", best_fitness)