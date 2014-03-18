import helper

def problem21(limit):
    all_sum_of_factors = {}
    for i in range(2, limit):
        all_sum_of_factors[i] = sum(helper.all_factors(i)) - i
    summation = 0
    for i in range(2, limit):
        if all_sum_of_factors.get(all_sum_of_factors[i], 0) == i and all_sum_of_factors[i] != i:
            summation += i
    return summation

if __name__ == "__main__":
    print(problem21(10000))