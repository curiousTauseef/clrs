def sort_nondecreasing(sequence):
  if len(sequence) < 2:
      return sequence
  middle = int(len(sequence)/2)
  left, right = sequence[middle:], sequence[:middle]
  return merge(sort_nondecreasing(left), sort_nondecreasing(right))

def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged
