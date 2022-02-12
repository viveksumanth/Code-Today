def sparseSearch(words,target):
    
    if len(words) == 0:
        return -1
        
    left = 0
    right = len(words)-1
    
    while(left <= right):
        
        mid = (left + right)//2

        
        if words[mid] == "":
            # find the closest posistion
            # move mid to the closest non empty string
            low = mid - 1
            high = mid + 1
            
            while(True):
                
                if low < 0 and high >= len(words) - 1:
                    return -1
                    
                elif low >= left and words[low] != "":
                    mid = low
                    break
                    
                elif high <= right and words[high] != "":
                    mid = high
                    break
                
                low = low - 1
                high = high + 1 
                
        if words[mid] == target:
            return mid     
            
        elif words[mid] > target:
            right = mid - 1
            
        elif words[mid] < target:
            left = mid + 1
                
    return -1

words = ["for", "geeks", "", "", "", "", "ide", "practice", "", "", "", "quiz"]
target = "quiz"

print(sparseSearch(words,target))