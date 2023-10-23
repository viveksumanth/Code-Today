class Solution:
    def letterCombinationsHelper(self, validStates, combinations, currentState, prevState):
        if len(currentState) == len(validStates):
            combinations.append("".join(currentState))
            return 
        
        for eachLetter in validStates[prevState]:
            currentState.append(eachLetter)
            prevState += 1
            self.letterCombinationsHelper(validStates, combinations, currentState, prevState)
            prevState -= 1
            currentState.pop()
        
        return
      
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        lookup = {
            "":[],
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
        
        combinations = []
        validStates = []
        
        for eachDigit in digits:
            validStates.append(lookup[eachDigit])
        self.letterCombinationsHelper(validStates, combinations, [], 0)
        
        return combinations
        
        