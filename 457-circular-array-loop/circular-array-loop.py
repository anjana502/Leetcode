class Solution:
    def cyclePresent(self, u, adj, nums, ls, s, s1):
        s.add(u)
        s1.add(u)

        if (nums[u] > 0):
            ls[0] += 1
        else:
            ls[1] += 1

        for v in adj[u]:
            if (v not in s):
                if (self.cyclePresent(v, adj, nums, ls, s, s1) == True):
                    return True
            elif (v in s1):
                return True
        
        s1.remove(u)
        
        return False
    
    def circularArrayLoop(self, nums: List[int]) -> bool:
        adj = [[] for i in range(len(nums))]

        for i in range(len(nums)):
            u = i
            v = (i + nums[i]) % len(nums)

            if (u != v):
                adj[u].append(v)
        
        for i in range(len(nums)):
            s = set()
            s1 = set()
            ls = [0, 0]

            if ((self.cyclePresent(i, adj, nums, ls, s, s1) == True) and (len(s) == ls[0] or len(s) == ls[1])):
                return True
        
        return False