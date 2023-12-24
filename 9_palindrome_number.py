# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        origNumber = x
        resultNumber = 0

        while x > 0:
            x, d = divmod(x, 10)
            resultNumber = resultNumber * 10 + d

        return resultNumber == origNumber
