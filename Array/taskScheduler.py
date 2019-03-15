# https://leetcode.com/problems/task-scheduler/
# Get number of As, Bs, Cs, 
# sort number of As, Bs

# the potential maximum idle slots is
# A .... A .... A .... A .... A
# maxIdle = (numberOfA - 1 ) * n 
# we then fill in Bs, Cs, notice that if numberOfB or C or D == A, 
# we only use B -1 numeber of B
# actualIdle = maxIdle - filledIns if less then 0, we set as 0
# final result = actualIdle + elements
class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        if len(tasks) <= 1:
        	return len(tasks)
        strMap = {}
        for task in tasks:
        	if task not in strMap:
        		strMap[task] = 1
        	else:
        		strMap[task] +=1
        sortedTaskNumbers = sorted(strMap.items(), key = lambda item: item[1], reverse = True)
        maxIdleNumber = (sortedTaskNumbers[0][1] - 1) * n
        if maxIdleNumber == 0:
        	return len(tasks)
        for i in range(1, len(sortedTaskNumbers)):
        	currentNumberOfStrs = sortedTaskNumbers[i][1]
        	if currentNumberOfStrs == sortedTaskNumbers[0][1]:
        		currentNumberOfStrs -= 1
        	maxIdleNumber -= currentNumberOfStrs
        	if maxIdleNumber <= 0:
        		return len(tasks)
        return len(tasks) + maxIdleNumber


#practiced
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) <= 1:
            return len(tasks)
        taskMap = {}
        for task in tasks:
            if task in taskMap:
                taskMap[task] += 1
            else:
                taskMap[task] = 1
        sortedTaskMap = sorted(taskMap.items(), key = lambda item:item[1], reverse = True)
        maxIdle = (sortedTaskMap[0][1] - 1) * n
        for i in range(1,len(sortedTaskMap)):
            filledTasks = sortedTaskMap[i][1]
            if sortedTaskMap[i][1] == sortedTaskMap[0][1]:
                 filledTasks -= 1
            maxIdle -= filledTasks
        maxIdle = 0 if maxIdle < 0 else maxIdle
        return maxIdle + len(tasks)


