class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_Color = image[sr][sc]
        # image[sr][sc] = newColor
        visited = [[False for i in range(len(image[0]))] for j in range(len(image))] 
        
        def dfs(sr,sc,visited):
    
            if (sr >= len(image) or 
                sc >= len(image[0]) or 
                sc < 0 or sr < 0 or 
                image[sr][sc] != old_Color 
                or visited[sr][sc] == True):return
            
            # print(sr,sc)
            visited[sr][sc] = True
            image[sr][sc] = newColor

            dfs(sr+1, sc,visited)
            dfs(sr-1, sc,visited)
            dfs(sr, sc+1, visited)
            dfs(sr, sc-1, visited)
            
            return image
        
        return dfs(sr,sc, visited)
                
                
        