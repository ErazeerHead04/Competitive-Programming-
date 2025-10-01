class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottle = empty // numExchange
            total += new_bottle
            empty = empty % numExchange + new_bottle
        return total
