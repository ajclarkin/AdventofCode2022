# Day 7 - No Space Left On Device, part 1
# Follow a series of directory traversal commands
# Find all directories with size <= 10,000 and sum them
# - The size should include the sizes of subdirectories

# FFS! Some directories have the same name.

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

                # Make sure each parent directory has this new one it it's list of childre
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
        # A value we need to save - add value to each directory in the path
        build_path = ''
        for dir in current_path:
            build_path += dir
            sizes[build_path] += int(words[0])
            build_path += '>'



big = [v for v in sizes.values() if v <= 100000]
print(f'The final value is {sum(big)}')
