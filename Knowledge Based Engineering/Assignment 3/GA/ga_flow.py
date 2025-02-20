import random
import math

class GeneticAlgorithmFlow:
    def __init__(self, target_flow, population_size, mutation_rate):
        self.target_flow = target_flow
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.best_radius = None

        # Initialize the population with random radii
        for _ in range(population_size):
            self.population.append(self.generate_random_radius())

        self.evolve(generations=100)

    def generate_random_radius(self):
        return random.uniform(0.01, 10)  # range of the radius randomly generated

    def calculate_flow(self, radius):
        g= 9.81 # gravity
        velocity = math.sqrt(2*g*radius/2) # calculate the velocity of the teapot spout
        return math.pi * (radius**2)*velocity # calculate the flow of the teapot spout

    def fitness(self, radius):
        flow = self.calculate_flow(radius)
        return abs(self.target_flow - flow) # the closer to 0, the better, as this is closer to desired flow

    def mutate(self, radius):
        if random.random() < self.mutation_rate:
            return self.generate_random_radius()
        return radius

    def crossover(self, parent1, parent2):
        return (parent1 + parent2) / 2  # Average of the two parents

    def evolve(self, generations):
        for generation in range(generations):
            self.population.sort(key=lambda x: self.fitness(x))
            best_radius = round(self.population[0],1)

            if self.fitness(best_radius) == 0:
                best_flow = round(self.calculate_flow(best_radius),1)
                self.best_radius = best_radius  # Store the best radius
                #print(f"Generation {generation}: Found a match! Radius: {best_radius}, Flow: {best_flow}")
                break


            new_population = [best_radius]

            for _ in range(1, self.population_size):
                parent1 = best_radius
                parent2 = random.choice(self.population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            self.population = new_population

            if generation % 10 == 0:
                best_flow = round(self.calculate_flow(best_radius),1)
                #print(f"Generation {generation}: Best fit: Radius: {best_radius}, Flow: {best_flow}")

        if self.fitness(best_radius) > 0:
            best_flow = round(self.calculate_flow(best_radius),1)
            self.best_radius = best_radius  # Store the best radius
            #print(f"Best result after {generations} generations: Radius: {best_radius}, Flow: {best_flow}")


"""
def main():
    try:
        target_flow = float(input("Enter the desired flow for the teapot: "))
        population_size = 10
        mutation_rate = 0.15

        ga = GeneticAlgorithmFlow(target_flow, population_size, mutation_rate)
        print(ga.best_radius)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the target flow.")

if __name__ == "__main__":
    main()"""