"""
Big O notation is used to measure how running time or
space requirements for your program grows as input size grows.
"""


# O(n)
def get_squared_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers


numbers = [1, 4, 6, 9]
print(get_squared_number(numbers))


# O(1)
def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe


# O(n^2)
numbers = [3, 6, 2, 4, 3, 6, 8, 9]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(str(numbers[i]) + "is a duplicate")
            break

# O(n^2) time complexity = a*n^2 + b*n + c
numbers = [3, 6, 2, 4, 3, 6, 8, 9]
duplicates = None
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicates = numbers[i]
            break
for i in range(len(numbers)):
    if numbers[i] == duplicates:
        print(i)
