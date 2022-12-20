

# To begin, find all of the directories with a total size of at most 100000, 
# then calculate the sum of their total sizes. In the example above, these 
# directories are a and e; the sum of their total sizes is 95437 (94853 + 584). 
# (As in this example, this process can count files more than once!)
#
# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

class file:
    def __init__(self, type, name, size, parent):
        self.type = type # file or dir
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}  # {fname: {content}}
    
    def update_size(self, fsize):
        if self.type == "dir":
            self.size += fsize
            if self.parent is not None:
                self.parent.update_size(fsize)
        else:
            self.size = fsize


def ls_update_parent(parent, fname, ftype, fsize):
    # short circuit if parent already contains file
    if fname in parent.children.keys():
        return
    
    # update parent with new child
    parent.children[fname] = file(ftype, fname, fsize, parent)

    # if new child is file, then update size through parents
    if ftype == "file":
        parent.update_size(fsize)


# PART 1
def process_commands(filename):
    root = file(type="dir", size=0, name="/", parent=None)
    current_dir = root
    ls_loop = False

    for l in filename:
        cmd = l.strip().split()

        if cmd[0] == '$':
            if cmd[1] == 'cd':
                ls_loop = False
                if cmd[2] == "/":
                    continue
                elif cmd[2] == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.children[cmd[2]]
            elif cmd[1] == 'ls':
                ls_loop = True
        elif cmd[0] == 'dir':
            fname = cmd[1]
            ls_update_parent(current_dir, fname, "dir", 0)
        else:
            fsize = int(cmd[0])
            fname = cmd[1]
            ls_update_parent(current_dir, fname, "file", fsize)
    
    return root



def display_dir_sizes(fdir, indent="", size_limit=100000):
    print(indent + fdir.name + " (" + str(fdir.size) + ")")

    size_ref = fdir.size if fdir.size < size_limit else 0

    for fname, fref in fdir.children.items():
        if fref.type == "dir":
            size_ref += display_dir_sizes(fref, indent= indent + "--")
    
    return size_ref

# part 2: 
# The total disk space available to the filesystem is  70000000. 
# To run the update, you need unused space of at least 30000000. 
#   30000000
# You need to find a directory you can delete that will free up enough space to run the update.
def find_dir_to_delete(fdir, update_size, total_size):
    
    search_list = [fdir]
    best = fdir
    available_space = total_size - fdir.size
    target_size = update_size - available_space

    while search_list != []:
        current_node = search_list.pop(0)
        # look for dir's and append to search_list
        for fname, fref in current_node.children.items():
            if fref.type == "dir":
                search_list.append(fref)
        if current_node.size < best.size and current_node.size >= target_size:
            best = current_node
    
    return best



if __name__ == "__main__":
    input_file = "day7.input"
    root_dir = None
    with open(input_file, 'r') as f:
        root_dir = process_commands(f)
        solution = display_dir_sizes(root_dir)
        print("DAY 7 (part 1) total size : %d " % solution)
        dir_to_delete = find_dir_to_delete(root_dir, 30000000, 70000000)
        print("DAY 7 (part 2) dir to delete : %s with %d " % (dir_to_delete.name, dir_to_delete.size))
        
    


