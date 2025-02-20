import random
import math

class GeneticAlgorithmVolume:
    def __init__(self, target_volume, population_size, mutation_rate):
        self.target_volume = target_volume
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.best_radius = None

        # Initialize the population with random radii
        for _ in range(population_size):
            self.population.append(self.generate_random_radius())
        self.evolve(generations=100)

    def generate_random_radius(self):
        return random.uniform(1, 100)  # adjust the range as needed

    def calculate_volume(self, radius): # calculate the volume of the teapot body
        effective_radius = radius - (radius * 0.05)*2
        return (4/3) * math.pi * (effective_radius**3)

    def fitness(self, radius):
        volume = self.calculate_volume(radius)
        return abs(self.target_volume - volume) # the closer to 0, the better, as this is closer to desired volume

    def mutate(self, radius):
        if random.random() < self.mutation_rate:
            return self.generate_random_radius() # random mutation
        return radius

    def crossover(self, parent1, parent2):
        return (parent1 + parent2) / 2  # Average of the two parents

    def evolve(self, generations): 
        for generation in range(generations):
            self.population.sort(key=lambda x: self.fitness(x))
            best_radius = round(self.population[0],1)

            if self.fitness(best_radius) == 0:
                best_volume = round(self.calculate_volume(best_radius))
                self.best_radius = best_radius  # Store the best radius
                #print(f"Generation {generation}: Found a match! Radius: {best_radius}, Volume: {best_volume}")
                return best_radius
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
                best_volume = round(self.calculate_volume(best_radius),1)
                #print(f"Generation {generation}: Best fit: Radius: {best_radius}, Volume: {best_volume}")

        if self.fitness(best_radius) > 0:
            self.best_radius = best_radius  # Store the best radius
            best_volume = round(self.calculate_volume(best_radius),1)
            #print(f"Best result after {generations} generations: Radius: {best_radius}, Volume: {best_volume}")

        
def main():
    try:
        target_flow = float(input("Enter the desired volume for the teapot: "))
        population_size = 100
        mutation_rate = 0.15

        ga = GeneticAlgorithmVolume(target_flow, population_size, mutation_rate)
        print(ga.best_radius)
        print(ga.calculate_volume(ga.best_radius))
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the target volume.")

if __name__ == "__main__":
    main()