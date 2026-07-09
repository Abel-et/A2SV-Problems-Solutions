class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # create component array , indcate teach connected nodes 
        component = [0] * n 
        comp =  0  

        for i  in range(1, n):

            # if the difference of to negiboughs is grater than max differ create another component 
            if nums[i] - nums[i-1] > maxDiff:
                comp += 1
            
            # else of every edge give a component based on compe
            component[i] = comp

        ans = []

        for u , v in queries:
            # if two edges are in the save component make true else false 
            ans.append(component[u] == component[v])
            
        return ans