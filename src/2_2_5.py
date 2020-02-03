"""You are given a positive integer. Your function should
calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will
be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Precondition: 0 < number < 10**6"""


def checkio(number: int) -> int:
    if 0 < number < 10 ** 6:
        c = 1
        for symbol in str(number):
            if symbol != '0':
                element = int(symbol)
                c *= element

        return c


print(checkio(123))
