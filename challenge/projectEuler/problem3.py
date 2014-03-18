import math

def is_prime_num(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if (num % i == 0 and num != i):
            return False
    return num > 1

def problem3(num):
    largest = num
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if (is_prime_num(i) and num % i == 0):
            largest = i
    return largest

if __name__ == "__main__":
    print (problem3(600851475143))