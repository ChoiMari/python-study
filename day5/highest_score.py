numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#sum()
print(sum(numbers))

sum : int = 0
for num in numbers:
    sum += num
    print(sum)
print(sum)

# max()
print(max(numbers)) # 10

max : int = 0
for num in numbers:
    if num > max:
        max = num
        print(max)
print(max)