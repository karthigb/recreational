import datetime

def problem19(startYear, endYear):
    total = 0
    for i in range(startYear, endYear+1):
        for j in range(1, 13):
            total += (0, 1)[datetime.date(i, j, 1).weekday() == 6]
    return total

if __name__ == "__main__":
    print(problem19(1901, 2000))