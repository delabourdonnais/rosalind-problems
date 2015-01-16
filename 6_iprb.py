import random

def run_experiment(k, m, n):
    parents = random.sample(range(k+m+n), 2)
    alleles = []
    for p in parents:
        if p < k:
            alleles.append('AA')
        elif p < k + m:
            alleles.append('Aa')
        else:
            alleles.append('aa')
    offspring = [''.join(random.sample(a, 1)) for a in alleles]
    return ''.join(offspring)

def is_success(res):
    return 'A' in res

def run_simulation(k, m, n, num_trials):
    count = 0
    for t in range(num_trials):
        res = run_experiment(k, m, n)
        if is_success(res):
            count += 1
    return round(float(count) / num_trials, 5)

def get_probability(k, m, n):
    return run_simulation(k, m, n, 1000000)
    

