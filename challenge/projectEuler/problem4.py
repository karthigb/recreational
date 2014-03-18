import math

def problem4(length):
    start = int('9' * length)
    answer = 0
    for i in range(start, 500, -1):
        for k in range(start, i - 1, -1):
            product = str(i * k)
            palindrome = True
            for j in range(math.ceil(len(product) / 2)):
                if product[0 + j] != product[-(1 + j)]:
                    palindrome = False
            if palindrome and int(product) > answer:
                answer = int(product)
    return answer

if __name__ == "__main__":
    print (problem4(3))