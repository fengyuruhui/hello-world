

def bubble_sort_OK(lists):
    j = len(lists) - 1
    k = j 
    while 0<k:
        for i in range(k):
            if lists[i]>lists[i+1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]
            i += 1
        k -= 1
    return lists


def bubble_sort(theSeq):
    # Sorts a sequence in ascending order using the bubble sort algorithm.
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range( n - 1, 0, -1 ) :
    # Bubble the largest item to the end.
        for j in range( i ) :
            if theSeq[j] > theSeq[j + 1] : # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq