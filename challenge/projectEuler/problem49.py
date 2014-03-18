import helper, math

def problem49():
    for i in range(1000, 10000):
        # Building list of prime and non-prime nums
        helper.is_prime_num(i)
    prime_nums = list(helper.get_prime_nums())
    prime_nums.sort()
    answer = []
    for i in range(len(prime_nums)):
        for j in range(i + 1, len(prime_nums)):
            num = prime_nums[j] + prime_nums[j] - prime_nums[i]
            if num in prime_nums:
                correct = True
                for k in range(0, 9):
                    digit = str(k)
                    if str(prime_nums[j]).count(digit) != str(prime_nums[i]).count(digit) or str(prime_nums[j]).count(digit) != str(num).count(digit):
                        correct = False
                if correct:
                    answer.append(str(prime_nums[i]) + str(prime_nums[j]) + str(num))
    return answer

if __name__ == "__main__":
    print(problem49())