'''This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.'''

arr = [2, 1, 2, 3, 3, 1, 3, 5]

l = 0
r = 0
maxy = -9999
curr_window = {}

while r < len(arr):
    curr_window[arr[r]]=r
    print(curr_window)

    
    while len(curr_window) > 2:
        min_index = min(curr_window.values())
        del curr_window[arr[min_index]]
        l = min_index+1

        
    maxy = max(maxy, r - l + 1)
    r += 1

print(maxy)


'''{2: 0}
{2: 0, 1: 1}
{2: 2, 1: 1}
{2: 2, 1: 1, 3: 3}
{2: 2, 3: 4}
{2: 2, 3: 4, 1: 5}
{3: 6, 1: 5}
{3: 6, 1: 5, 5: 7}
4
'''

# great use of dict and uses .values() and reminds of .keys() and then del to delete a value
