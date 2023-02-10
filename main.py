def my_tuple():
    this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "cherry", True, 40)
    return this_tuple


my_tuple = my_tuple()
print(my_tuple)

print(len(my_tuple))

#  Accessing a tuple
print(my_tuple[1])

print(my_tuple[2:5])

# Updating tuples
y = list(my_tuple)  # first. convert a tuple to a list
y[1] = "kiwi"  # add to the list
x = tuple(y)  # convert the list back to a tuple

print(x)

#  Adding to a tuple
s = list(my_tuple)
s.append("pineapple")
my_tuple = tuple(s)

print(my_tuple)

#  Adding tuple to a tuple
new_tuple = ("strawberry",)  # a new tuple
my_tuple += new_tuple

print(my_tuple)
print()

#  Removing from a tuple
a_tuple = ("Chi", "Ben", "Dan")
a = list(a_tuple)
a.remove("Chi")
a_tuple = tuple(a)

print(a_tuple)

# Looping through a tuple
for x in my_tuple:
    print(x)

print()

for i in range(len(my_tuple)):
    print(my_tuple[i])

print()

#  Joining tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
