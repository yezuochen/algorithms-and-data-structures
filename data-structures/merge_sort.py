# merge sort

def merge_sort(list):
    """
    Sorts a list in ascending order.
    Return a new sorted list.

    divide: find the midpoint of the list and divide into sublists
    conquer: recursively sort the sublists created in previous step
    combine: merge the sorted sublists created in previous step

    Takes O(kn log n) time.
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.
    Takes overall O(k log n) time.
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process.
    Returns a new merged list.
    Run in overall O(n) time.
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])



alist = [45,34,54,36,32,23,77,22,67,83,95,21]

print(verify_sorted(alist))

l = merge_sort(alist)
print(l)

print(verify_sorted(l))