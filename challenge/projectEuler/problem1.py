def problem1a(factors, limit):
    summation = 0
    i = 1
    while i < limit:
        for factor in factors:
            if i % factor == 0:
                summation += i
                break;
        i += 1
    return summation

def problem1b(factors, limit):
    summation = 0
    i = 1
    factors.sort()
    multiples, common = [], []
    while (i * factors[0]) < limit:
        for factor in factors:
            if (i * factor) < limit:
                multiples.append(i * factor)
                common.append(0)
        for factor in factors:
            for j in range(len(multiples)):
                if multiples[j] % factor == 0:
                    common[j] +=1
        summation += sum([(multiples[j] / common[j]) for j in range(len(multiples))])
        multiples.clear()
        common.clear()
        i += 1
    return int(summation)

if __name__ == "__main__":
    print (problem1a([3, 5], 1000))
    print (problem1b([3, 5], 1000))