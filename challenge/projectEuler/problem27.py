import helper

def problem27(limit):
    max = 0
    a_max = 0
    b_max = 0
    for a in range(-1*limit, limit + 1):
        for b in range(-1*limit, limit + 1):
            n = 0
            while helper.is_prime_num((n*n + a*n + b)):
                n += 1
                if n > max:
                    max = n
                    a_max = a
                    b_max = b
    return (a_max * b_max)

if __name__ == "__main__":
    print(problem27(1000))