a = 1               # There integer data type is used
time_zone = "GMT+3" # There string data type is used

print(time_zone)    # And you will see ... GMT+3

a = 10

def foo():
    pass

class Bar:
    pass

print(type(a))
print(type(foo))
print(type(Bar))

a = 10
b = 10.5
c = 8+3j

print(type(a))
print(type(b))
print(type(c))

my_str = "This is my string!"
print(type(my_str))

some_list = [1, 2.5, True, "Str in a list"]
print(type(some_list))

my_tuple = (22, 89, True, False)
print(type(my_tuple))

our_set = {4, 3, 6.6, "Hello"}
print(type(our_set))

another_dict = {"message": "Hi!", 33: True}
print(type(another_dict))

a = 1
print(id(a))

a += 2
print(id(a))

# As ids are different it conveys that integers are immutable

my_list = [1, 2]
print(id(my_list))

my_list.append(3)
print(id(my_list))

# ids are same meaning my_list is still referring to the same object -> mutable
