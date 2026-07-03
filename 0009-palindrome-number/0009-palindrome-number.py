class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        length = len(str_x)

        for i in range(0,length//2):
            if str_x[i] != str_x[length - 1- i]:
                return False
            
        return True