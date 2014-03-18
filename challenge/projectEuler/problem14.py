collatz_length = {}

def next_number(num):
    if (num % 2 == 0):
        return num / 2
    else:
        return (3*num) + 1
 
def perform_collatz_problem(num):
    length = 1
    while num != 1:
        if num in collatz_length:
            length += collatz_length[num] - 1
            num = 1
        else:
            num = next_number(num)
        length += 1
    return length

def problem14(length):
    max_length = 0
    starting_point = 1
    for i in range(1, length):
        sequence_length = perform_collatz_problem(i)
        collatz_length[i] = sequence_length
        if sequence_length > max_length:
            max_length = sequence_length
            starting_point = i
    return starting_point

if __name__ == "__main__":
    print(problem14(1000000))