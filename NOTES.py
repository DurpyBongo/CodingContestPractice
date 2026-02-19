# ===============================
# PYTHON COMPETITIVE PROGRAMMING CHEAT SHEET
# ===============================

# -------------------------
# LIST / ARRAY TRICKS
# -------------------------

my_list = [1, 2, 3, 4, 5]

# Reverse a list
reversed_list = my_list[::-1]          # returns a new reversed list
my_list.reverse()                      # in-place reversal

# Sort
my_list.sort()                          # ascending
my_list.sort(reverse=True)              # descending
sorted_list = sorted(my_list)           # new sorted list

# Index / Count
idx = my_list.index(3)                  # first occurrence index
count_2 = my_list.count(2)              # number of times 2 appears

# Add / Remove
my_list.append(6)                       # add to end
my_list.insert(2, 99)                   # insert at index
my_list.pop()                            # remove last
my_list.pop(1)                           # remove at index
my_list.remove(99)                       # remove first occurrence

# Map / Filter / List Comprehension
squared = list(map(lambda x: x**2, my_list))
evens = list(filter(lambda x: x%2==0, my_list))
squared2 = [x**2 for x in my_list]      # list comprehension
evens2 = [x for x in my_list if x%2==0]

# Sum / Min / Max / Len
total = sum(my_list)
maximum = max(my_list)
minimum = min(my_list)
length = len(my_list)

# Copy
copy_list = my_list.copy()               # shallow copy

# Swap variables
a, b = 5, 10
a, b = b, a                              # now a=10, b=5

# -------------------------
# STRING FUNCTIONS
# -------------------------

my_string = "hello world"

# Length
length = len(my_string)

# Find / Index
pos = my_string.find("o")                # first 'o'
pos_r = my_string.rfind("o")             # last 'o'
# replace
new_string = my_string.replace("world","python")
# strip spaces
cleaned = "  hi  ".strip()

# Case
upper = my_string.upper()
lower = my_string.lower()
capitalized = my_string.capitalize()

# Split / Join
words = my_string.split()                # ['hello','world']
joined = "-".join(words)                 # 'hello-world'

# Check
is_alpha = "abc".isalpha()
is_digit = "123".isdigit()
is_space = "   ".isspace()

# Reverse a string
reversed_str = my_string[::-1]

# -------------------------
# SET / DICTIONARY
# -------------------------

# Set (unique elements)
s = {1, 2, 3}
s.add(4)
s.remove(2)
has_3 = 3 in s

# Dictionary
d = {"a":1,"b":2}
d["c"] = 3
val = d.get("b")                        # safe get
keys = d.keys()
values = d.values()
items = d.items()

# -------------------------
# LOOPING / ITERTOOLS
# -------------------------

# Range
nums = list(range(5))                     # [0,1,2,3,4]
nums2 = list(range(1,10,2))              # [1,3,5,7,9]

# Enumerate
for i,val in enumerate(my_list):
    print(i,val)

# Zip (parallel iteration)
a = [1,2,3]
b = ['x','y','z']
for num, char in zip(a,b):
    print(num, char)

# Any / All
all_pos = all(x>0 for x in my_list)
any_even = any(x%2==0 for x in my_list)

# -------------------------
# MATH / BUILT-IN FUNCTIONS
# -------------------------

import math

ceil_val = math.ceil(4.2)
floor_val = math.floor(4.7)
sqrt_val = math.sqrt(16)
power_val = pow(2,5)
abs_val = abs(-7)
gcd_val = math.gcd(12,18)
lcm_val = math.lcm(12,18)                # Python 3.9+

# -------------------------
# INPUT / OUTPUT TRICKS
# -------------------------

# Fast input (competitive programming)
import sys
input = sys.stdin.readline

# Multiple integers in one line
a,b,c = map(int,input().split())

# -------------------------
# LIST / STRING TRICKS
# -------------------------

# Flatten a 2D list
matrix = [[1,2],[3,4]]
flat = [x for row in matrix for x in row]

# Count characters in string
from collections import Counter
freq = Counter(my_string)                # {'h':1,'e':1,...}

# -------------------------
# OTHER USEFUL TRICKS
# -------------------------

# Swap two numbers
x, y = 10, 20
x, y = y, x

# Lambda function
square = lambda x: x**2

# Sorting with key
arr = [(1,3),(2,1),(4,0)]
arr.sort(key=lambda x: x[1])             # sort by second element

# Bisect / binary search
import bisect
lst = [1,3,5,7]
pos = bisect.bisect_left(lst,4)          # returns 2
bisect.insort(lst,4)                     # insert 4 in sorted order

# Deep copy
import copy
new_list = copy.deepcopy(my_list)

# Time measurement
import time
start = time.time()
# code to measure
end = time.time()
elapsed = end - start

# -------------------------
# STACK / QUEUE
# -------------------------

from collections import deque
q = deque()
q.append(1)
q.appendleft(0)
q.pop()
q.popleft()

