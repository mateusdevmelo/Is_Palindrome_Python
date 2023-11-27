# leetcode challenger

# 9. Palindrome Number:

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x%10
            x = x // 10
        return newNum == inputNum
    
sol = Solution()

result = sol.isPalindrome(121)

print(result)