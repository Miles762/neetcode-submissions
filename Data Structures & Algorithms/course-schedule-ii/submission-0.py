class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashm= {i:[] for i in range(numCourses)}
        for curr,pre in prerequisites:
            hashm[curr].append(pre)
        visit = set() #currently the ndoe is in the dfs path
        res = [] 
        compl = set() #the node is completed


        def dfs(root):
            curr = root
        
        #    if hashm[curr] == []:return True
         #the addition of the course doesnt happen 
        # #    and the fn just return so thsi is commented is CS2
            
             # Cycle found
            if curr in visit:
                return False

            # Already processed before
            if curr in compl:
                return True


            visit.add(curr)
            for pre in hashm[curr]:
                if not dfs(pre): return False
            visit.remove(curr)
            compl.add(curr)
            res.append(curr)
            return True

    
        for i in range(numCourses):
            if not dfs(i): 
                return []
        return res
        