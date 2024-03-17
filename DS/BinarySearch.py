'''
Iteration 1=n/2
Iteration 2=(n/2)/2 = n/2^2
Iteration 3=(n/2^2)/2 = n/2^3
...
Iteration K=n/2^K

K = log n -> O(log n)
'''
from util import time_it


@time_it
def linear_search(numbers_list, number_to_finds):
    for index, element in enumerate(numbers_list):
        if element == number_to_finds:
            return index
    return -1


@time_it
def binary_search(numbers_list, number_to_finds):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2  # // only get Integer index, / get floating point index
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_finds:
            return mid_index

        if mid_number < number_to_finds:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(numbers_list, number_to_finds, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2  # // only get Integer index, / get floating point index
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_finds:
        return mid_index

    if mid_number < number_to_finds:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_finds, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [15, 33, 36, 45, 47, 52, 61, 88]
    number_to_finds = 3622

    # index = linear_search(numbers_list, number_to_finds)
    # index = binary_search(numbers_list, number_to_finds)
    index = binary_search_recursive(numbers_list, number_to_finds, 0, len(numbers_list))
    # print(f"Number found at index {index} using linear search")
    print(f"Number found at index {index} using binary search")
