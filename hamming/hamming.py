def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) is not len(strand_b):
        raise ValueError('They have different lengths')
    for i in range(0, len(strand_a)):
        if strand_a[i] is not strand_b[i]:
            count += 1
    return count
