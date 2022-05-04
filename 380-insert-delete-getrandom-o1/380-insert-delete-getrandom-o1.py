import random

class RandomizedSet:

    def __init__(self):
        self.lookup = dict()
        self.lList = ['X']
        
    def insert(self, val: int) -> bool:
        # print(self.lookup)
        if val not in self.lookup:
            self.lookup[val] = len(self.lList)
            self.lList.append(val)
            return True
        return False
        
    def swap(self,popp):
        lastIndex = len(self.lList) - 1
        element = self.lList[lastIndex]
        self.lookup[element] = popp
        self.lList[lastIndex], self.lList[popp] = self.lList[popp],self.lList[lastIndex]
        
    def remove(self, val: int) -> bool:
        
        if val in self.lookup:
            popp = self.lookup[val]
            self.swap(popp)
            self.lList.pop()
            del self.lookup[val]
            # print(self.lookup)
            return True
        
        return False
        

    def getRandom(self) -> int:
        
        randomNumber = random.randint(1,len(self.lList)-1)
        return self.lList[randomNumber]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()