class Solution:
    def maxProduct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        digits.sort(reverse=True)

        return digits[0] * digits[1]