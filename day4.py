

def parse_line(line):
    # 98-99,3-97
    items = line.replace(",","-").split("-")
    items = [ int(x) for x in items ]
    return items

# In how many assignment pairs does one range fully contain the other?
def contained_assignments(input):
    counter = 0
    for l in input:
        items = parse_line(l.strip())

        #case 1: first contains second
        if items[0] <= items[2] and items[1] >= items[3]:
            counter += 1

        #case 2: second contains first
        elif items[2] <= items[0] and items[3] >= items[1]:
            counter+=1
    
    print("DAY 4 (part 1) count: %d" % (counter))

def overlapped_assignements(input):
    counter = 0
    for l in input:
        items = parse_line(l.strip())

        range1 = range(items[0],items[1] + 1)
        range2 = range(items[2],items[3] + 1)

        if items[0] in range2 or items[1] in range2:
            counter += 1
        elif items[2] in range1 or items[3] in range1:
            counter += 1

    print("DAY 4 (part 2) count: %d" % (counter))


if __name__ == "__main__":
    input_file = "day4.input"
    with open(input_file) as f:
        contained_assignments(f)
        f.seek(0, 0)
        overlapped_assignements(f)