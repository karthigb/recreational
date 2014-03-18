def problem9(sum):
    for a in range(333):
        for b in range(a + 1, 500):
            c = 1000 - a - b
            if (a*a) + (b*b) == (c*c) and c > b and b > a:
                return a*b*c
    return 0

if __name__ == "__main__":
    print (problem9(1000))  