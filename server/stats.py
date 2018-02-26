def variance(values, mean, n):
    return sum([((v - mean)**2)/(n-1) for v in values])

def standard_deviation(values):
    n  = len(values)
    if n <= 1:
        return (0, 0 ,0)
    total = sum(values)
    mean = total / n
    sample_variance = variance(values, mean, n)
    std_dev = math.sqrt(sample_variance)
    return (mean, sample_variance, std_dev)
