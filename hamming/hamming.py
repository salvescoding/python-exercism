def distance(strand_a, strand_b):
    if len(strand_a) is not len(strand_b):
        raise ValueError('They have different lengths')
    return sum(i is not j for i, j in zip(strand_a, strand_b))



