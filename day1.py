# In case the Elves get hungry and need extra snacks, they need to know which 
# Elf to ask: they'd like to know how many Calories are being carried by the 
# Elf carrying the most Calories. In the example above, this is 24000 (carried 
# by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that 
# Elf carrying?



def elf_with_most(filename):

    f = open(filename, "r")

    elf_num = 1
    elf_subtotal = 0
    elf_most = 0

    for l in f:
        if l != "\n":
            elf_subtotal += int(l)
        else:
            # print("Elf %d: %d" % (elf_num, elf_subtotal))
            if elf_subtotal > elf_most:
                elf_most = elf_subtotal
            elf_subtotal = 0
            elf_num += 1
    
    f.close()
    
    print("DAY 1 (part 1): Elf with the most: %d" % (elf_most))


def elves_with_most_calories(filename, top_n):
    f = open(filename, "r")
    calories = []
    elf_subtotal = 0

    for l in f:
        if l != "\n":
            elf_subtotal += int(l)
        else:
            calories.append(elf_subtotal)
            elf_subtotal = 0
    f.close()

    calories.sort(reverse=True)

    print("DAY 1 (part 2): Top %d with the most: %d" % (top_n, sum(calories[:top_n])))



if __name__ == "__main__":
    elf_with_most("day1-1.input")
    elves_with_most_calories("day1-1.input", 3)