def get_expected_value(*args):
    coeffs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    res = sum([coeffs[i] * args[i] for i in range(6)])
    return 2 * res
    
