import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Original Code - O(n^2)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

# Solution Code - O(n)

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         # left case?
#         # check if the value is before the root value in the alphabet?
#         if value < self.value:
#             # move to the left and check if it is none?
#             if self.left == None:
#                 # insert node here
#                 new_node = BSTNode(value)
#                 self.left = new_node
#             # otherwise
#             else:
#                 # call insert on the root's left node
#                 self.left.insert(value)
#         # right case?
#         if value > self.value:
#         # otherwise
#             # move to the right and check if it is none?
#             if self.right == None:
#                 # insert the node here
#                 new_node = BSTNode(value)
#                 self.right = new_node
#             # otherwise
#             else:
#                 # call insert on the root's right node
#                 self.right.insert(value)   
        

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         # check if the node is == target
#         if self.value == target:
#             # if true return true
#             return True
#         # otherwise check if target is before node value in alphabet
#         elif target < self.value:
#             # if left is None, target doesn't exist in tree, return false
#             if self.left == None:
#                 return False  
#             # otherwise move down left, call contains on left node
#             else:
#                 return self.left.contains(target)
#         # otherwise check if target is after node value in alphabet
#         elif target > self.value: 
#             # if right is None, target doesn't exist in tree, return false
#             if self.right == None:
#                 return False  
#             # otherwise move down right, call contains on right node
#             else:
#                 return self.right.contains(target)

# duplicates = [] 
# bst = BSTNode(names_1[0])
# for name_1 in names_1:
#     bst.insert(name_1)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
