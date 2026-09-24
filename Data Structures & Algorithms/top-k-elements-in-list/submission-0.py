class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}

        for i in nums:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        
        buckets=[[] for i in range(len(nums)+1)]

        for x in seen:
            buckets[seen[x]].append(x)

        res=[]
        for i in range(len(buckets)-1,0,-1):
            for x in buckets[i]:
                res.append(x)
                if len(res)==k:
                    return res


        
        