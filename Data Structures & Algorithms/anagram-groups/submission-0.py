class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            count={}
            for j in i:
                if j not in count:
                    count[j]=1
                else :
                    count[j]+=1
            print(count)
            key=tuple(sorted(count.items()))

            if key not in seen:
                seen[key]=[i]
            else:
                seen[key].append(i)
        print(seen)
        return list(seen.values())


               