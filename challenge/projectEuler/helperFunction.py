def is_prime_num(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if (num % i == 0 and num != i):
            return False
    return num > 1

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