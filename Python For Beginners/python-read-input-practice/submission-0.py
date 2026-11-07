def add_two_numbers() -> int:
    a = input()
    array = a.split(",")
    return sum(int(x) for x in array)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())