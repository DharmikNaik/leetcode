class Solution:
    
    def __init__(self):
        self.solutions = 0
    
    def climbStairs(self, n: int) -> int:
        
        def helper(n, step_size):
            if n-step_size == 0:
                self.solutions+=1
                return
            if n-step_size<0:
                return
            helper(n-step_size,1)
            helper(n-step_size,2)
    
        def find_solution(n):
            helper(n,1)
            helper(n,2)
    
        
        find_solution(n)
        
        return self.solutions
