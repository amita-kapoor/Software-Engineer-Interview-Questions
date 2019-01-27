from random import randrange
def bubble_sort(A):
    # edge case check
    if len(A) < 2:
        return A
    i= len(A)-1
    while i > 0:
        max = A[i]
        for j in range(i):
            if A[j] > max:
                A[i], A[j] = A[j], A[i]
                max = A[j]
        i -= 1
    return A

def insertionSort(A):
    # Edge case check
    if len(A) < 2:
        return A
    for j in range(1,len(A)):
        i=j
        while i > 0 and A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            i = i-1
    return A

def selectionSort(A):
    # Edge case check
    if len(A) < 2:
        return A
    for j in range(len(A)):
        indexSmall = j
        for i in range(j+1, len(A)):
            if A[i] < A[indexSmall]:
                indexSmall = i
        A[j] , A[indexSmall] = A[indexSmall], A[j]
    return A


def mergeSort(A):
    # Edge case check
    result = []
    if len(A) < 2:
        return A
    middle = int(len(A)/2)
    L = mergeSort(A[:middle])
    R = mergeSort(A[middle:])

    ## merging the two returned arrays
    iR = 0
    iL = 0
    while len(result) < len(L) + len(R):
        if L[iL] < R[iR]:
            result.append(L[iL])
            iL += 1
        else:
            result.append(R[iR])
            iR += 1

        if iR == len(R) or iL == len(L):
            result.extend(R[iR:] or L[iL:])
    return result


def quikSort(A, start, end):
    if end <= start:
        return A
    # pivot = randrange(iL, iR + 1)
    pivot = start
    iR = end
    iL = start
    #print("In quick sort", pivot, iL, iR, A)
    #w = input("enter")
    #iL += 1
    while iL < iR:
        while A[iL] <= A[pivot] and iL < end: iL += 1
        while A[iR] >= A[pivot] and start < iR: iR -= 1
        if iL <= iR:
            A[iL], A[iR] = A[iR], A[iL]
    A[iR], A[pivot] = A[pivot], A[iR]
    pivot = iR
    quikSort(A,start, pivot-1)
    quikSort(A, pivot+1, end)
    return


import numpy
import timeit
import copy

print(bubble_sort([5, 4, 6,2,7]))
print (" n tI  tB   tS     tM   tQ")

for n in range(10, 5000, 100):
    A = numpy.random.randint(1000, size=n)
    B = copy.deepcopy(A)

    startTime = timeit.default_timer()  ## Starting time
    insertionSort(A)
    tI = timeit.default_timer() - startTime

    A = copy.deepcopy(B)

    startTime = timeit.default_timer()  ## Starting time
    bubble_sort(A)
    tB = timeit.default_timer() - startTime

    A = copy.deepcopy(B)

    startTime = timeit.default_timer()  ## Starting time
    selectionSort(A)
    tS = timeit.default_timer() - startTime

    A = copy.deepcopy(B)

    startTime = timeit.default_timer()  ## Starting time
    result = mergeSort(A)
    tM = timeit.default_timer() - startTime

    A = copy.deepcopy(B)

    startTime = timeit.default_timer() ## Starting time
    quikSort(A, 0, len(A) - 1)
    tQ = timeit.default_timer() - startTime

    A = copy.deepcopy(B)
    print( n, tI, tB, tS, tM, tQ)
