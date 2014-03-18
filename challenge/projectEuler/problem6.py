def problem6(start, end):
    sum_of_squares = 0
    for i in range(start, end + 1):
        sum_of_squares += i ** 2
    square_of_sum = ((end * (end + 1) / 2) - (start * (start - 1) / 2)) ** 2
    return abs(sum_of_squares - square_of_sum)

if __name__ == "__main__":
    print (problem6(1, 100))