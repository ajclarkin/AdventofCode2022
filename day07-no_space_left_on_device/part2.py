# Day 7 - No Space Left On Device, part 1
# Follow a series of directory traversal commands
# Find all directories with size <= 10,000 and sum them

# Filesystem has 70,000,000 space.
# Largest dir is '/'.
# We need to create 30,000,000 free space - find the one smallest dir to delete to create this free space - how big is it?


input = [x for x in open('input.txt').read().split('\n')]

current_dir = ''
current_path = []
sizes = {}
children = {}


for i in input:
    words = i.split(' ')
    if words[0] == '$':
        if words[1] == 'cd':
            if words[2] == '..':
                current_path.pop()
                current_dir = ">".join(current_path)
            else:
                # Moving down a level - save the details for the level we're moving from
                current_path.append(words[2])
                current_dir = ">".join(current_path)

                sizes[current_dir] = 0

                children[current_dir] = set()
                build_path = ''
                for dir in current_path[:-1]:
                    build_path += dir
                    children[build_path].add(current_dir)
                    build_path += '>'



        elif words[1] == 'ls':
            sizes[current_dir] = 0


    # Here we need to process dir contents
    elif words[0] == 'dir':
        pass
    else:
        # A value we need to save
        build_path = ''
        for dir in current_path:
            build_path += dir
            sizes[build_path] += int(words[0])
            build_path += '>'



available = (70000000 - sizes['/'])
space_reqd = 30000000 - available

closest_val = 70000000
closest_key = ''

for k,v in sizes.items():
    if v >= space_reqd and v < closest_val:
        closest_val = v
        closest_key = k

print(f'The closest sized directory has size {closest_val}')
