
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2

        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)

        merge(A, p, q, r)


def merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]

    i = 0
    j = 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


A = [8, 3, 6, 2]

merge_sort(A, 0, len(A) - 1)

print("Sorted array:", A)
