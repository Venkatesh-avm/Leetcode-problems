class Solution():
    def sumlist(self,nums,target):
        mp = {}
        for i in range (len(nums)):
            num=nums[i]
            comp=target-num
            if comp in mp:
                return (mp[comp],i)
            mp[num]=i
        return[]
nums=[2,7,9,11]
target=9
s=Solution()
result=s.sumlist(nums,target)
print(result)

        
    

        
