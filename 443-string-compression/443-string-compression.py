class Solution:
    def __init__(self):
        self.count = 1
        
    def makeCount(self,chars,idx,prev):
        # print(chars,idx,prev)
        if self.count == 1:
            pass

        elif self.count > 1 and self.count < 10:
            chars[idx-1] = str(self.count)
            # print(chars)
            chars[idx-2] = prev
            # print(chars)

        elif self.count >= 10 and self.count < 100:
            numb = str(self.count)
            chars[idx-1] = numb[1]
            chars[idx-2] = numb[0]
            chars[idx-3] = prev

        elif self.count >= 100 and self.count < 1000:
            numb = str(self.count)
            chars[idx-1] = numb[2]
            chars[idx-2] = numb[1]
            chars[idx-3] = numb[0]
            chars[idx-4] = prev

        else:
            numb = str(self.count)
            chars[idx-1] = numb[3]
            chars[idx-2] = numb[2]
            chars[idx-3] = numb[1]
            chars[idx-4] = numb[0]
            chars[idx-5] = prev

        self.count = 1
                
                
    def compress(self, chars: List[str]) -> int:
        lastIdx = 0
        if len(chars) == 1:
            return 1
        
        for idx in range(1,len(chars)):
            # print(chars)
            prev = chars[idx-1]
            current = chars[idx]

            if prev != current:
                self.makeCount(chars,idx,prev)
            
            else:
                self.count += 1
                chars[idx-1] = ''
            lastIdx = idx
         
        # print(chars,lastIdx,prev)
        self.makeCount(chars,lastIdx+1,prev)
        
        while("" in chars):
            chars.remove("")
            
        return len(chars)
            
                