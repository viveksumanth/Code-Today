
class Employee:
    
    def __init__(self,ids,name,reports):
        self.name = name
        self.ids = ids
        self.reports = reports


class Solution:
    
    def findCeo(self,employeeList):
        #finds the employee
        outdegree = dict()
        ceo = None
        
        for eachEmployee in employeeList:
            for eachsub in eachEmployee.reports:
                if eachsub.ids in outdegree:
                    outdegree[eachsub.ids] += 1
                else:
                    outdegree[eachsub.ids] = 1
                    
        
        for eachEmployee in employeeList:
            if eachEmployee.ids not in outdegree:
                ceo = eachEmployee
                outdegree[eachEmployee.ids] = 0 

        return ceo
    
    def computePath(self,currentEmp,curPath,comPath,target):
        subs = currentEmp.reports

        if currentEmp.ids == target.ids:
            comPath.append(curPath[:])
            return comPath
        
        if len(subs) == 0:
            return 
        
        for eachEmployee in subs:
            self.computePath(eachEmployee,curPath+[eachEmployee.ids],comPath,target)
        
        return comPath

    
    def findPath(self,employeeList,target):
        
        ceo = self.findCeo(employeeList)
       
        path = self.computePath(ceo,[ceo.ids],[],target)
        
        return path


if __name__ == "__main__":
    
    newSub2 = Employee(2,'s',[])
    newSub3 = Employee(3,'su',[])
    newSub7 = Employee(7,'sumant',[])
    newSub6 = Employee(6,'sumant',[newSub7])
    newSub5 = Employee(5,'suman',[newSub6])
    newSub4 = Employee(4,'suma',[newSub5])

    newEmployee = Employee(1,'vivek',[newSub2,newSub3,newSub4])

    EmployeeList = [newEmployee, newSub2, newSub3 ,newSub4 ,newSub5 ,newSub6 ,newSub7]
    sol = Solution()
    path = sol.findPath(EmployeeList,newSub7)
    print(path)