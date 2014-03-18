def problem16(power):
    num = str(2**power)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

if __name__ == "__main__":
    print (problem16(1000))