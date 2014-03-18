import codecs
import re
import helper

def problem41(file_path):
    f = codecs.open(file_path, 'rU')
    words = f.read()
    words = re.sub('",', '\n', words)
    words = re.sub('"', '', words)
    words = words.split()
    words.sort()
    total = 0
    for word in words:
        value = 0
        for character in word:
            value += helper.letter_position(character)
        term = helper.triangle_pos(value)
        if int(term) == term:
            total += 1
    return total

if __name__ == "__main__":
    print(problem41("words.txt"))