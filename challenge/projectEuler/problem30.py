import math

def problem30(power):
    total = 0
    stop = False
    length = 1
    while len(str(int(math.pow(9, power) * length))) <= length or not stop:
        if len(str(int(math.pow(9, power) * length))) <= length:
            stop = True
    for i in range(2, int("9" * length)):
        num = str(i)
        summation = 0
        for n in num:
            summation += math.pow(int(n), power)
            if summation == i:
                total += i
    return total
    
if __name__ == "__main__":
    print(problem30(5))