import math
import codecs
import re

num2wordsDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety", 100:"hundred", 1000:"thousand", 1000000:"million", 1000000000:"billion", 0:""}
prime_nums = set()
non_prime_nums = set()

def num2words(number):
    if number == 0:
        return "zero"
    number = str(number)
    output = ""
    for i in range(0, len(number), 3):
        if i > 0:
            num = int(number[-i - 3: -i])
        else:
            num = int(number[-3:])
        hundred = math.floor(num / 100)
        ten = math.floor(num % 100 / 10) * 10
        one = num % 10
        num_string = num2wordsDict.get(hundred, "")
        if hundred > 0:
            num_string = num2wordsDict.get(hundred, "") + " hundred"
            if ten or one:
                num_string += " and "
        if ten == 10:
            num_string += num2wordsDict.get(ten + one, "")
        elif ten and one:
            num_string += num2wordsDict.get(ten, "") + '-' + num2wordsDict.get(one, "")
        else:
            num_string += num2wordsDict.get(ten, "") + num2wordsDict.get(one, "")
        if i > 0:
            num_string += " " + num2wordsDict.get(10**i, "")
        if output and num_string:
            output = num_string + " " + output
        else:
            output = num_string
    return output

def is_prime_num(num):
    if num < 2:
        return False
    if num in prime_nums:
        return True
    if num in non_prime_nums:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if (num % i == 0 and num != i):
            non_prime_nums.add(num)
            return False
    prime_nums.add(num)
    return True

def multiple_of_factors(factors, num):
    copy = factors[:]
    print(factors)
    for i in factors:
        if num % i == 0:
            num /= i
            copy.remove(i)
            if (is_prime_num(num) and not num in copy) or num == 0:
                return True
            else:
                return multiple_of_factors(copy, num)
    return False

def ith_prime(ith):
    nth = 0
    num = 1
    while nth < ith:
        num += 1
        if is_prime_num(num):
            nth += 1
            print ('%d : %d' % (nth, num))
    return num

def string_input(string):
    maxProduct = 0
    for i in range(len(string) - 4):
        nums = [int(string[k]) for k in range(i, i + 5)]
        product = 1
        for k in nums:
            product *= k
        if product > maxProduct:
            maxProduct = product
    return maxProduct
    
def ith_prime(position):
    num = 0
    pos = 0
    while pos < position:
        num += 1
        if is_prime_num(num):
            pos += 1
    return num
    
def triangle_number(position):
    return (position * (position + 1))/2
    
def all_factors(number):
    factors = set()
    for i in range(1, int(math.floor(math.sqrt(number)) + 1)):
        if number % i == 0:
            factors.add(i)
            factors.add(int(number / i))
    return factors
    
def letter_position(character):
    return (ord(character.upper()) - 64)
    
def triangle_pos(num):
    return ((math.sqrt(8 * num + 1) - 1) / 2)
    
def get_prime_nums():
    return prime_nums