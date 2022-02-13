from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def generate_states(word,wordDict):
            word = list(word)
            letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            states = []
            for i in range(0,len(word)):
                for j in range(0,len(letters)):
                    tempword = ''.join(word[:i] + [letters[j]] + word[i+1:] )
                    if tempword in wordDict:
                        states.append(tempword)
            
            return states
        
        def bfs(beginWord, endWord, wordDict):
            
            queue = deque([beginWord])
            steps = 1
            usedWords = set()
            usedWords.add(beginWord)
            
            while(len(queue)):
                
                for i in range(0,len(queue)):
                    
                    curr_word = queue.popleft()

                    if curr_word == endWord:
                        return steps


                    states = generate_states(curr_word, wordDict)
                    # print(states)

                    for eachState in states:
                        if eachState not in usedWords:
                            queue.append(eachState)
                            usedWords.add(eachState)
                            
                steps = steps + 1
            return 0
            
            
        def wordLadder(beginWord, endWord, wordList):
            wordDict = dict()
            
            for i in wordList:
                wordDict[i] = 1
            
            shortest = bfs(beginWord, endWord, wordDict)
            return shortest
        
        
        return wordLadder(beginWord, endWord, wordList)
            
                
        
        