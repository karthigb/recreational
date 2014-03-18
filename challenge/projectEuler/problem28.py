import math

def problem28(size):
    if size % 2 == 0:
        return "Size must be of odd length"
    grid = []
    for i in range(size):
        grid.append([None]*size)
    x = math.floor(size / 2)
    y = math.floor(size / 2)
    n = 1
    delta_x = 0
    delta_y = 1
    while -1 < x and x < size and -1 < y and y < size:
        grid[x][y] = n
        if not(grid[x + delta_y][y - delta_x]):
            delta_x, delta_y = delta_y, -delta_x
        x += delta_x
        y += delta_y
        n += 1
    total = 0
    for i in range(0, len(grid)):
        total += grid[i][i]
        total += grid[size - 1 - i][i]
    total -= grid[math.floor(size / 2)][math.floor(size / 2)]
    return total
    
if __name__ == "__main__":
    print(problem28(1001))