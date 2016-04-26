

def debugPrint(karg):
    print " %s " % karg


def sortedLinearSearch(target, lists):
    length = len(lists)
    for i in range(length):
        if target == lists[i]:
            return True
        elif target < lists[i]:
            return False
        
    # find to the end of the lists, and not meet target
    return False

def binarySearch(target, theValues):
    low = 0
    high = len(theValues)-1
    
    debugPrint(high)
    debugPrint(theValues[high])
    
    if high==0 and theValues[high] != target:
        return False
    else:
        mid = (high-low)/2 + low
        debugPrint(theValues)
        debugPrint(mid)
        debugPrint(theValues[mid])             
        if target == theValues[mid]:
            return True
        elif target < theValues[mid]:
            high = mid
            return binarySearch(target, theValues[:high])
        else:
            low = mid+1
            return binarySearch(target, theValues[low:])        

        
    
def binarySearchNonRecurse(target, lists):
    low = 0
    high = len(lists) - 1
    
    while(low <= high):
        mid = (high - low)/2 + low
        if target == lists[mid]:
            debugPrint(mid)
            debugPrint(lists[mid])
            return True
        elif target < lists[mid]:
            high = mid-1
        else:
            low = mid + 1
            
    return False