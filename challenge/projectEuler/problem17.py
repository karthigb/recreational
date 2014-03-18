import helper

def problem17(start, end):
    length = 0
    for i in range(start, end + 1):
        length += len(helper.num2words(i).replace(" ", "").replace("-", ""))
    return length

if __name__ == "__main__":
    print (problem17(1, 1000))