class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zeros = []

        for i in str(n):
            if int(i)>0:
                non_zeros.append(str(i))
        if len(non_zeros) ==0:
            return 0
        else:
            x = int("".join(non_zeros))
            return x * sum(list(int(i) for i in non_zeros))