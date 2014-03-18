def problem25(length):
    a = 1
    b = 1
    term = 2
    while len(str(b)) < length:
        b, a = a + b, b
        term += 1
    return term

if __name__ == "__main__":
    print(problem25(1000))