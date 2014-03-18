import math

def problem29(a_upper_bound, b_upper_bound):
    terms = set()
    for a in range(2, a_upper_bound + 1):
        for b in range(2, b_upper_bound + 1):
            terms.add(math.pow(a, b))
    return len(terms)

if __name__ == "__main__":
    print(problem29(100, 100))