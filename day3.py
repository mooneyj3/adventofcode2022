



def get_pri(c):
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38

def common_chars(word1, word2):
    return ''.join(set(word1).intersection(word2))

# part 1
# ord('A') = 65 --> 27 (subtract )
# ord('a') = 97 --> 1 (subtract 96)
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def sum_items(filename):
    total = 0
    with open(filename, 'r') as f:
        for l in f:
            items = l.strip()
            mid = len(items) // 2
            left = items[:mid]
            right = items[mid:]
            total += get_pri(common_chars(left,right))
    
    print("DAY 3 (part 1) total: %d" % (total))

# part 2
def sum_items_2(filename):
    total = 0
    counter = 0
    elf1 = ''
    elf2 = ''
    elf3 = ''
    with open(filename, 'r') as f:
        for l in f:
            if counter % 3 == 0:
                elf1 = l.strip()
            elif counter % 3 == 1:
                elf2 = l.strip()
            else:
                elf3 = l.strip()
                total += get_pri(common_chars(common_chars(elf1,elf2),elf3))
            counter += 1
        print("DAY 3 (part 2) total: %d" % (total))

if __name__ == "__main__":
    sum_items("day3.input")
    sum_items_2("day3.input")


