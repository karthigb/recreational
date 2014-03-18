import codecs
import re
import helper

def problem22(file_path):
    f = codecs.open(file_path, 'rU')
    names = f.read()
    names = re.sub('",', '\n', names)
    names = re.sub('"', '', names)
    names = names.split()
    names.sort()
    total = 0
    for pos in range(len(names)):
        name = names[pos]
        value = 0
        for i in range(len(name)):
            value += helper.letter_position(name[i])
        total += (value * (pos + 1))
    return total
    
if __name__ == "__main__":
    print(problem22("names.txt"))