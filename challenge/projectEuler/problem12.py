def problem12(divisors):
    i = 0
    divisors = 0
    while divisors <= 500:
        i += 1
        divisors = len(all_factors(i))
    return divisors

if __name__ == "__main__":
    print problem12(5000)