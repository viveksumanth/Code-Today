class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        string = ''
        if ch in word:
            index = word.index(ch)
            prefix = word[0:index+1]
            end = word[index+1::]
            prefix = prefix[::-1]
            word = prefix + end
        return word
        