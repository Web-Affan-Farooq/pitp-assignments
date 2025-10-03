## Pandas notes:

```python
content = pd.read_csv(DATA_FILE_PATH)
content = pd.read_xlsx(DATA_FILE_PATH)
```

**Working with rows and columns :**
for getting number of rows and columns:

```python
   st.write(f"number of rows : {content.shape[0]}")
   st.write(f"number of columns : {content.shape[1]}")
```

---

Data Types

You’re given the following code:

x = (1, [2, 3], {4, 5})
x[1].append(99)
print(x)

(a) What will be printed?
answer: (1, [2, 3,99], {4, 5})
(b) Why is this possible even though tuples are “immutable”?
answer: because tuples are immutable but we are appending in list

---

print(5 and 0 or 7) # 7
print(0 or [] and "yes") # False
print(True is 1 == (1 < 2)) # True

---

Loops & Range

for i in range(1, 10, 2):
if i % 3 == 0:
break
else:
print("Done")
(a) Will "Done" print?
ans: yes
(b) Explain why:
ans: because loop has all even steps

---

Conditional Statements
Given:

a, b, c = 5, 10, 5
if a < b < c or not a == c:
print("X")
else:
print("Y")

What will be printed?
ans: Y

---

Section B – Data Structures

Sets

s = {frozenset([1, 2]), frozenset([2, 3])}
print(len(s))

Explain the result.
ans: contains two frozen sets

---

Dictionaries
Predict output and explain:

d = {"a": 1, "b": 2}
for k in d:
d[k] += 1
print(d)

output: all values of d will be incremented by one because we loop through the dict and increased each value by one

---

Lists & Tuples

nums = [1, 2, 3]
t = (nums, nums[:])
nums.append(4)
print(t)

(a) What is printed?
([1,2,3,4], [1,2,3])
(b) Why are the two elements in t different?
because one array is original reference and another is stale copy

---

Import/Export Modules
Suppose you have a module math_tools.py with:

def add(x, y): return x + y
def \_hidden(z): return z \* 2

(a) How do you import only add into another script?

```python
from math_tools import add
```

(b) Can you import \_hidden? Why or why not?
ans : because it's protected

---

with Keyword
Explain what’s wrong here:

f = open("data.txt", "w")
with f:
f.write("hello")

ans: When opening the file , there is a chance of error here's why we use with there , but instead of using with in the vulnerable part , we are using it before we execute the vulnerable part , if the above code fails , program will be crached ompletely
