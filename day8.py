# PART 1
# A tree is visible if all of the other trees between it and an edge of the grid are 
# shorter than it. Only consider trees in the same row or column; that is, only look 
# up, down, left, or right from any given tree.

# Consider your map; how many trees are visible from outside the grid?

def build_grid(file):
    tree_grid = []
    for l in file:
        row = [int(a) for a in l.strip()]
        tree_grid.append(row)
    return tree_grid

def print_grid(grid):
    w = len(grid[0])
    h = len(grid)
    for i in range(h): # 
        for j in range(w):
            print(grid[i][j], end="")
        print()

def vertical_slide(grid):
    slice = None
    return slice

def count_visible_trees(grid):
    w = len(grid[0]) # width / columns
    h = len(grid) # height / rows
    #outer_trees = (2 * w) + (2 * (h-2))
    #inner_trees = 0

    vis_grid = [[0 for x in range(w)] for y in range(h)]  # 0 (not visible) or 1 (visible)
    
    # set top/bottom borders to visible
    for i in range(w):
        vis_grid[0][i] = 1
        vis_grid[w-1][i] = 1
    # set side columns to visible
    for i in range(h):
        vis_grid[i][0] = 1
        vis_grid[i][h-1] = 1

    #iterate through each row starting at row 1 through h - 1
    for i in range(1, h - 1):
        current_row = grid[i]
        tallest_left_tree = current_row[0]
        tallest_right_tree = current_row[h-1]
        
        for x in range(w):
            left_tree = current_row[x]
            right_tree = current_row[w-x-1]
            if tallest_left_tree == 9 and tallest_right_tree == 9:
                break
            if tallest_left_tree != 9 and left_tree > tallest_left_tree:
                vis_grid[i][x] = 1
                tallest_left_tree = left_tree
            if tallest_right_tree != 9 and right_tree > tallest_right_tree:
                vis_grid[i][w-x-1] = 1
                tallest_right_tree = right_tree

    #iterate through each column
    for col in range(1, w-1):
        tallest_top_tree = grid[0][col]
        tallest_btm_tree = grid[h-1][col]

        for i in range(h): # iterate through each row of the ocolumn
            top_tree = grid[i][col]
            btm_tree = grid[h-i-1][col]
            if tallest_top_tree == 9 and tallest_btm_tree == 9:
                break
            if tallest_top_tree != 9 and top_tree > tallest_top_tree:
                vis_grid[i][col] = 1
                tallest_top_tree = top_tree
            if tallest_btm_tree != 9 and btm_tree > tallest_btm_tree:
                vis_grid[h-i-1][col] = 1
                tallest_btm_tree = btm_tree

    # return sum of vis_grid
    return sum(sum(vis_grid,[]))


if __name__ == "__main__":
    input_file = "day8.input"
    with open(input_file, 'r') as f:
        tree_grid = build_grid(f)
    
    #Part 1
    # print(tree_grid)
    solution = count_visible_trees(tree_grid)
    print("DAY 8 (part 1) visible trees : %d " % solution)
