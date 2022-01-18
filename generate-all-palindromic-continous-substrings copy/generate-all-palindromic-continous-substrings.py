'''
Linux File Path - find the correct path 
code Serialize and deSerialize functions

intput: "/usr/bin/$HOME$/$TMP$/somefile.txt"

hashmap = {
    HOME = "$username$"
    TMP  = "$PRIVATE$/folder/$username$"
    PRIVATE = "tmpfolder"
    username = "TMP%"
}
'''
class makeLinuxPath:
    def __init__(self):
        self.lookup = dict()
        self.isCycle = False
        
    def serialize(self,array):
        for each in array:
            key,value = each
            if key not in self.lookup:
                self.lookup[key] = value
        

    def decodeStringHelper(self,string,visited = set()):
        visited.add(string)
        result = self.lookup[string]
        result = result.split('/')

        for each in range(0,len(result)):
            subString = result[each]
            if subString.startswith('%') and subString.endswith('%'):
                if subString[1:len(subString)-1] in visited:
                    self.isCycle = True
                    return ''

                result[each] = self.decodeStringHelper(subString[1:len(subString)-1],visited)
        
        return '/'.join(result)
        
        
            
    def deSerialize(self,decodeString):
        decodeString = decodeString.split('/')
        decodedString = []
        for eachString in decodeString:
            if eachString.startswith('%') and eachString.endswith('%'):
                subResult = self.decodeStringHelper(eachString[1:len(eachString)-1],set())
                
                if self.isCycle == True:
                    return 'CYCLE IN DATA'
                
                decodedString.append(subResult)
            else:
                decodedString.append(eachString)
        
        return '/'.join(decodedString)

if __name__ == "__main__":
    array = [ 
        ['HOME','%username%'],
        ['TMP','%PRIVATE%/folder/%username%'],
        ['PRIVATE','tmpfolder'],
        ['username','HOME'],
    ]
    
    decodeString = "/usr/bin/%HOME%/%TMP%/somefile.txt"
    obj = makeLinuxPath()   
    obj.serialize(array)
    print(obj.deSerialize(decodeString))