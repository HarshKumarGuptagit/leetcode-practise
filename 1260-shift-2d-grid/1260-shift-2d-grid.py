class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])

        flatten_list = []

        for i in grid:
            for j in i:
                flatten_list.append(j)

        for i in range(0,k):
            last=flatten_list[-1]
            flatten_list= flatten_list[0:-1]
            flatten_list.insert(0,last)

        result = []
        for i in range(0, len(flatten_list), n):
            result.append(flatten_list[i:i + n])
        
        return result