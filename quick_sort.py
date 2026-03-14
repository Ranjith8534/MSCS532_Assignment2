# Quick Sort Implementation
# MSCS532 Assignment 2
# Ranjith Kumar Bollam

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]

    print("Original:", data)
    print("Sorted:", quick_sort(data))
