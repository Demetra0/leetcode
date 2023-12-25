# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        for i in range(1, n + 1):
            cur = 0

            while i:
                cur += i % 2
                i = i >> 1

            ans.append(cur)

        return ans