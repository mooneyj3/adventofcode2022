


def parse_config(config_file):
    with open(config_file, 'r') as config:
        rows = []

        for l in config:
            rows.append(l.replace('\n', ''))
        
        num_stacks = (len(rows[0]) + 1) // 4
        num_rows = len(rows)
        stack_array = [ [] for i in range(num_stacks) ]

        for i in range(num_stacks):
            c_idx = i*4 + 1
            stack_item = []
            for j in range(num_rows - 1):
                stack_array[i].append(rows[j][c_idx])
                if ' ' in stack_array[i]:
                    stack_array[i].remove(' ')

        for i in range(len(stack_array)):
            stack_array[i].reverse()

        return stack_array


def print_code(stack_array):
    code = ""
    for i in stack_array:
        if len(i) > 0:
            code += i[-1]
    
    print(code)


# PART 1
# .split()[1::2]
# move 6 from 4 to 3
def crane_code(input, stack_array):
    for l in input:
        idx = l.split()[1::2]
        mov = int(idx[0])
        frm = int(idx[1]) - 1
        too = int(idx[2]) - 1

        for j in range(mov):
            rmv = stack_array[frm].pop()
            stack_array[too].append(rmv)
    print("DAY 5 (part 1) code: ", end="")
    print_code(stack_array)

# PART 2
# crane can move multiple at a time.
# move 6 from 4 to 3

# [x, x, x, x, x, x, x, x, x]
# len = 9
# move idx = len - 6 = 3

def crane_code_2(input, stx):
    for l in input:
        idx = l.split()[1::2]
        mov = int(idx[0])
        frm = int(idx[1]) - 1
        too = int(idx[2]) - 1

        mov_idx = len(stx[frm]) - mov

        stack = stx[frm][mov_idx:]
        stx[frm] = stx[frm][:mov_idx]
        stx[too] += stack

    print("DAY 5 (part 2) code: ", end="")
    print_code(stx)


if __name__ == "__main__":
    config_file = "day5.config"
    input_file = "day5.input"
    stack_array = parse_config(config_file)
    stack_array_pt2 = parse_config(config_file)
    with open(input_file) as f:
        crane_code(f, stack_array)
        f.seek(0, 0)
        crane_code_2(f, stack_array_pt2)

