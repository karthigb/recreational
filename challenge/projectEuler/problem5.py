import math, helper

def problem5a(factors):
    use = []
    factors.sort()
    smallest=True
    num = 0
    while smallest:
        num += 1
        smallest = False
        for i in factors:
            if num % i != 0:
                smallest = True
    return num

def problem5b(factors):
    use = []
    factors.sort()
    for i in range(1, len(factors)):
        if helper.is_prime_num(factors[i]):
            use.append(factors[i])
        elif helper.multiple_of_factors(use, factors[i]):
            use.append(factors[i])
    answer = 1
    print (use)
    for i in use:
        answer *= i
    return answer

if __name__ == "__main__":
    print (problem5a([y for y in range(1, 21)]))
    print (problem5b([y for y in range(1, 21)]))