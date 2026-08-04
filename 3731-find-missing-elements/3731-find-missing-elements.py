class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        com_nums = list(x for x in range(min(nums),max(nums)+1,1))

        return_list = []
        for i in com_nums:
            if i not in nums:
                return_list.append(i)
        
        return return_list