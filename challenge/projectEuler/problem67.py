import problem18, re, codecs

def turn_proper_single_digit(matchobj):
    return matchobj.group(1)

def problem67(file_path):
    f = codecs.open(file_path, 'rU')
    tree = f.read()
    tree = re.sub(r'\b0(\d)\b', turn_proper_single_digit, tree)
    tree = re.sub('\s+', ' ', tree)
    tree = tree.split()
    tree = [int(num) for num in tree]
    return problem18.problem18(tree)

if __name__ == "__main__":
    print(problem67("triangle.txt"))