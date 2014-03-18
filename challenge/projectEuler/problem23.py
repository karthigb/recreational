import helper

def problem23a():
    abundants = []
    for i in range(2, 28123):
        total = sum(helper.all_factors(i)) - i
        if total > i:
            abundants.append(i)
    total = 0
    for i in range(1, 28124):
        non_abundant_sum = True
        for abundant in abundants:
            if abundant > i:
                break
            elif (i - abundant) in abundants:
                non_abundant_sum = False
                break
        if non_abundant_sum:
            total += i
    return total
 
def problem23b():
    abundants = []
    for i in range(0, 28123):
        total = sum(helper.all_factors(i)) - i
        if total > i and total <= 28123:
            abundants.append(i)
    total = 0
    abundant_sums = set()
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            abundant_sum = abundants[i] + abundants[j]
            if abundant_sum <= 28123 and abundant_sum >= 0:
                abundant_sums.add(abundant_sum)
    total = ((28123 * 28124) / 2) - sum(abundant_sums)
    return total

if __name__ == "__main__":
    #print(problem23a())
    print(problem23b())