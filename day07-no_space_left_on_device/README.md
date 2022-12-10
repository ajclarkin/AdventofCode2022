# Day 7 - No Space Left on Device

After sailing through the first 6 days they're starting to get harder. I had a couple of abortive starts because I didn't 
understand the problem properly or saved the wrong data even when I did understand it.


## Part 1
Given a series of directory traversal commands find all the directories with size <= 100,000.
- The size of each directory should include the sizes of subdirectories (and so there will be some double-counting
 when coming to do the final sum).
- Some directories have the same name - this caught me out once I had what looked like a working solution for the example.

This a really a series of nested if statements. We identify when going down a level with a `cd` and for each directory above save a list of every directory below it the `children` dictionary.

When we get a directory listing we sum the sizes of all the files in that directory and add it to `sizes` dictionary; we increment each entry in that dictionary that is in the current file path (so add the size to the current dir but also each parent dir).

So we end up with a dictionary storing the size of each directory, and another storing a set of all the directories below it on the path.

We keep a track of where we are in the file path by appending or popping the current dir as moving up or down using `current_path` list.

Each directory is identified by it's full path name and for a directory separator we use `>` because the top dir is already called `/`.

In the end we find all the directories (keys) with size (value) <= 100,000 in sizes and sum them.


## Part 2

The filesystem is 70,000,000 big. We need 30,000,000 free space. The total space used is `sizes["/"]`. Find the one smallest directory where deleting it will create enough free space. What size is it?
