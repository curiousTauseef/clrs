def sort_nondecreasing(sequence):
    for i in range(len(sequence)-1):
        index_min = i
        for j in range(i+1, len(sequence)):
            if sequence[j] < sequence[index_min]:
                index_min = j
        sequence[i], sequence[index_min] = sequence[index_min], sequence[i]
    return sequence
