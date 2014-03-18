import math

def problem20(factorial_num):
    num = str(math.factorial(factorial_num))
    total = 0
    for i in range(len(num)):
        total += int(num[i])
    return total

if __name__ == "__main__":
    print(problem20(100))