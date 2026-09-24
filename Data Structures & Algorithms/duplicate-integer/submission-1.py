class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=set()
        for i in nums:
            if i not in b:
                b.add(i)
                
            elif  i in b:
                return True
        return False

        