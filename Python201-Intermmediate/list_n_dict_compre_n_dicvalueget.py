
#* <------List comprehension--->

numbers = []
for num in [1, 3, 5, 7, 9]:
    numbers.append(num**2)
print(numbers)

numbers = [num**2 for num in [1, 3, 5, 7, 9]]       #list comprehension
print(numbers)

# ANother Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#* <-----------------Dictionary Comprehension----------->

names = [("name", "Kalob"), ("occupation", "Coder")]
d = {}
for key, value in names:
    d[key] = value
print(d)

#^1st way

d = {key: value for key, value in names}
print(d)

#^2nd way

d = dict(names)
print(d)

#^ getting dictionar values 

courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"
}

# suppose yo want js value here ,we can do courses["js"],but its sort of painful



