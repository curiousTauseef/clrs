def sort_nondecreasing(sequence):
    for i in range(1, len(sequence)):
        element = sequence[i]
        j = i-1
        while j >= 0 and sequence[j] > element:
            sequence[j+1] = sequence[j]
            j -= 1
        sequence[j+1] = element
    return sequence
