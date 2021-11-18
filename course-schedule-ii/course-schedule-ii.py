
from collections import defaultdict
class Solution:
    
    def generateChildren(self,courses,node):
        
        children = []
        
        for eachCourse in courses[node]:
            children.append(eachCourse)
        
        return children
    
    def countCourses(self, courses):
        '''
        counting the indegree of the nodes
        '''
        coursesCount = {node:0 for node in courses}

        for eachPreq in courses:
            for eachCourse in courses[eachPreq]:
                coursesCount[eachCourse] += 1

        
        return coursesCount
    
    def topoSort(self,courses):
        
        coursesCount = self.countCourses(courses)
        queue = []
        result = []
        
        '''
        adding the nodes whose InDegree = 0 first
        '''
        for eachCourse in coursesCount:
            if coursesCount[eachCourse] == 0:
                queue.append(eachCourse)
        
        while(len(queue)):
            
            node = queue.pop(0)
            result.append(node)
            
            children = self.generateChildren(courses,node)
            
            for eachChild in children:
                
                coursesCount[eachChild] -= 1
                
                if coursesCount[eachChild] == 0:
                    queue.append(eachChild)
                    
        return result
    
    
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        
        '''
        if they are no prerequisites then courses can be completed.
        '''
        
        if len(prereq)  == 0:
            return [i for i in range(0,numCourses)]
        
        for eachPreq in prereq:
            
            '''
            if both the nodes are same we just return False because that forms a cycle
            '''

            if eachPreq[1] == eachPreq[0]: 
                return []
            
            courses[eachPreq[1]].append(eachPreq[0])
            
            if eachPreq[0] not in courses:
                courses[eachPreq[0]] = []
        
        for course in range(0,numCourses):
            if course not in courses:
                courses[course] = []
        

        result = self.topoSort(courses)
        
        '''
        if number of nodes after topologically sorting the graph is less than the number of nodes in graph which means that there is a cycle.
        '''
        if len(courses.keys()) != len(result):
            return []
        
        return result