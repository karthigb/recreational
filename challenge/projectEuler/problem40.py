def problem40(positions):
    num_add = len(positions)
    answer = 1
    num_added = 0
    digit = 1
    pos = 1
    while num_added < num_add:
        for i in str(digit):
            if pos in positions:
                answer *= int(i)
                num_added += 1
            pos += 1
        digit += 1
    return answer

if __name__ == "__main__":
    print(problem40([1, 10, 100, 1000, 10000, 100000, 1000000]))