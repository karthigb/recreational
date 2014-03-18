import helper

def problem10(upperbound):
    summation = 0
    for i in range(upperbound):
        if helper.is_prime_num(i):
            summation += i
    return summation

if __name__ == "__main__":
    print (problem10(2000000))