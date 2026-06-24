class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        num = n
        while True:
            num_list = [int(x)**2 for x in str(num)]
            list_sq_sum = sum(num_list)
            if list_sq_sum == 1:
                return True
            elif list_sq_sum in l:
                return False
            else:
                num=list_sq_sum
                l.add(list_sq_sum)
                continue  
        