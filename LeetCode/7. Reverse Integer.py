class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        result = 0

        while x!=0:
            digit = x%10
            x//= 10
            result = result*10 + digit
            if result > 2**31-1:
                return 0
        return result*-1 if is_negative else result

        #time: O(log 10 base x)
        #spce: O(1