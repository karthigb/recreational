def problem2(limit):
    a, b = 1, 2
    summation = 2
    while b < limit:
        a, b = b, a + b
        if b % 2 == 0:
            summation += b
    return summation

if __name__ == "__main__":
    print (problem2(4000000))