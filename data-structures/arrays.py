# array

new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

# insert (linear runtime)
# appending (constant time)
numbers = []
print(len(numbers))

numbers.append(2)
numbers.append(200)
print(numbers)

numbers.extend([4, 5, 6])
print(numbers)