import random
def fitness(x):
return x**2
population = [random.randint(0, 31) for _ in range(6)]
generations = 5
for gen in range(generations):
sources = [fitness(x) for x in population]
# Select best 2 parents
parents = sorted(zip(population, sources), key=lambda x: x[1], reverse=True)[:2]
p1, p2 = parents[0][0], parents[1][0]
# Crossover
point = random.randint(1, 4)
e1 = (p1 & ((1 << point) - 1)) | (p2 & ~((1 << point) - 1))
e2 = (p2 & ((1 << point) - 1)) | (p1 & ~((1 << point) - 1))

# Mutation
def mutate(x):
bit = 1 << random.randint(0, 4)
return x ^ bit if random.random() < 0.3 else x
c1, c2 = mutate(e1), mutate(e2)
# New population
population = [p1, p2, c1, c2] + [random.randint(0, 31) for _ in range(2)]
best = max(population, key=fitness)
print(f"Generation {gen+1}: Population: {population}, Best Individual: {best}
(fitness={fitness(best)})")
print(f"\nFinal Best after {generations} generations: {best} with fitness {fitness(best)}")
