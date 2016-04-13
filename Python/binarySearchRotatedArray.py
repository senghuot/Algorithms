'''
    Premise: a sorted array with a none decreasing order is being rotated. For example: you can imagine
            [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]. find 5 will return index 8.

            Let A = [a_1, a_2,..., a_n] and at index i is where the array is being rotated on.

'''
def binarySearchRotatedArray(A, lo, hi, n):

    if lo > hi: return -1

    mid = (lo + hi) / 2

    if A[mid] == n: return mid

    # lets look at the left half and the right half to decide which direction to do our search
    if A[lo] < A[mid]:
        if A[lo] <= n and n <= A[mid]:
            return binarySearchRotatedArray(A, lo, mid-1, n)
        return binarySearchRotatedArray(A, lo+1, hi, n)

    if A[mid] < A[hi]:
        if A[mid] <= n and n <= A[hi]:
            return binarySearchRotatedArray(A, mid+1, hi, n)
        return binarySearchRotatedArray(A, lo, mid-1, n)

    if A[lo] == A[mid]:
        if A[mid] == A[hi]:
            return binarySearchRotatedArray(A, lo, mid-1, n)
        else:
            result = binarySearchRotatedArray(A, lo, mid-1, n)
            if result != -1:
                return result
            return binarySearchRotatedArray(A, mid+1, hi, n)



A = [4,5,6,7, 1,2,3]
print binarySearchRotatedArray(A, 0, 6, 4)