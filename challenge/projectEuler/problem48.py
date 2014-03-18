import math

def problem48(term):
    i = 1
    total = 0
    while i <= term:
        print(i)
        total += math.pow(i, i)
        i += 1
    return str(total)[-10:0]

if __name__ == "__main__":
    print(problem48(1000))