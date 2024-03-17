import random

# Task_1


def generate_sort():

    random_list = [random.randint(1, 1000) for _ in range(100)]

    ascending_list = sorted(random_list)

    descending_list = sorted(random_list, reverse=True)

    return ascending_list, descending_list


ascending_sorted, descending_sorted = generate_sort()

print("Ascending Sorted List:", ascending_sorted)
print("Descending Sorted List:", descending_sorted)


# Task_2


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    center = arr[len(arr) // 2]
    left = [x for x in arr if x < center]
    middle = [x for x in arr if x == center]
    right = [x for x in arr if x > center]

    return quick_sort(left) + middle + quick_sort(right)


def generate_and_sort():

    random_list = [random.randint(1, 1000) for _ in range(100)]

    bubble_sorted = random_list.copy()
    bubble_sort(bubble_sorted)

    quick_sorted_list = random_list.copy()
    quick_sorted_list = quick_sort(quick_sorted_list)[::-1]

    return bubble_sorted, quick_sorted_list


bubble_sorted, quick_sorted = generate_and_sort()

print("Ascending Sorted List (Bubble Sort):", bubble_sorted)
print("Descending Sorted List (Quicksort):", quick_sorted)
