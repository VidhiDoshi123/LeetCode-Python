class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        tortoise = n
        hare = get_next(n)
        while hare!=1 and hare!=tortoise:
            tortoise = get_next(tortoise)
            hare = get_next(get_next(hare))
        return hare == 1