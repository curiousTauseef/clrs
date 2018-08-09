def binary_search(sequence, element, left=0, right=0):
    sequence.sort()
    left = 0
    right = right or len(sequence)
    middle = left + abs(left-right)//2

    while True:
        middle = left + abs(left-right)//2
        print("Left: {0}\nRight: {1}\nMiddle: {2}".format(left, right, middle))
        if sequence[middle] == element:
            return middle
        elif sequence[middle] > element:
            right = middle
        elif sequence[middle] < element:
            left = middle
    return -1

a = [1, 2, 3, 3, 3, 3, 1, 5, 1, 12, 2, 1, 2, 3]

print(binary_search(a, 54))
print(binary_search(a, 4))
print(binary_search(a, 3))
print(binary_search(a, 12))
print(binary_search(a, 1))
print(binary_search(a, 8))
print(binary_search(a, 12))
