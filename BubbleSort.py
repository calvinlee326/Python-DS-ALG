from util import time_it

@time_it
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp

        if not swapped:
            break


if __name__ == '__main__':
    # elements = [5, 33, 1, 32, 77, 9, 64]
    elements = [1,3,5]

    bubble_sort(elements)
    print(elements)
