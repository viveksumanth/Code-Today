
class Solution(self):

	def generateAllParlindromesHelper(left,right,stringArray):
	    allParlindomesHelper = []
	    
	    while(left < right):

	        if left < 0 or right > len(stringArray) - 1:
	            break
	        
	        if stringArray[left] == stringArray[right]:
	            substring = ''.join(stringArray[left:right+1])
	            allParlindomesHelper.append(substring)
	            left -= 1
	            right += 1   
	            
	        elif stringArray[left] != stringArray[right]:
	            break
	        

	    return allParlindomesHelper
	            

	def generateAllParlindromes(string):
	    
	    allParlindomes = []
	    substringsOddLength = []
	    substringsEvenLength = []
	    stringArray = list(string)

	    if len(stringArray) == 0:
	        return 0
	        
	    allParlindomes.append(string[0])
	    
	    for idx in range(1,len(stringArray)):
	        
	        allParlindomes.append(string[idx])
	        substringsOddLength = generateAllParlindromesHelper(idx-1,idx+1,stringArray)
	        substringsEvenLength = generateAllParlindromesHelper(idx-1,idx,stringArray)
	        allParlindomes += substringsEvenLength 
	        allParlindomes += substringsOddLength 

	    return allParlindomes 

if __name__ == '__main__':
    string = 'abaxyzzyxa'
    solution = Solution()
    result = solution.generateAllParlindromes(string)
    print(result)
        
        
                
    
            
        
        
        