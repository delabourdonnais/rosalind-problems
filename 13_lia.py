import random

def mate(person1, person2, nbChilds=1):
    offspring = []
    for i in range(nbChilds):
        child = [random.choice(person1.split()[k])
                 + random.choice(person2.split()[k])
                 for k in range(len(person1.split()))]
        offspring.append(' '.join(child))
    return offspring

def run_experiment(k, N=1):
    population = ["Aa Bb"]
    for i in range(k):
        newGeneration = []
        for p in population:
            newGeneration += mate(p, "Aa Bb", 2)
        population = newGeneration
    sortedPopulation = []
    for p in population:
        sortedPopulation.append(
            ' '.join([''.join(sorted(el)) for el in p.split()]))
    return N <= sortedPopulation.count("Aa Bb")

def get_probability(k, N):
    numTrials = 150000
    count = 0
    for t in range(numTrials):
        count += run_experiment(k, N)
    return float(count) / numTrials
