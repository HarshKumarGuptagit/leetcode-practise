class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        total_sum = sum(list(z for z in range(0,n+1)))

        for i in range(0,n+1):
            left_sum += i
            right_sum = total_sum - left_sum + i

            if left_sum == right_sum:
                return i
        return -1