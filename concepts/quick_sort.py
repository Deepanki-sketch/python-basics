def partition(A, p, r):
    x = A[r]           # Choose the last element as pivot
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


# Main program
A = [8, 3, 1, 7, 0, 10, 2]

quick_sort(A, 0, len(A) - 1)

print("Sorted array:", A)