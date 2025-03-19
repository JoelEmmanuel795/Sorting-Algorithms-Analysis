import time 

def insertion_sort(a_list): 
    exchanges = 0  # Counter for exchanges
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos -= 1
            exchanges += 1
        a_list[cur_pos] = cur_val
    return exchanges

def selection_sort(a_list):
    exchanges = 0  # Counter for exchanges
    for i in range(len(a_list)):
        min_idx = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
            exchanges += 1
    return exchanges

def bubble_sort(a_list):
    exchanges = 0  # Counter for exchanges 
    for i in range(len(a_list) - 1, 0, -1):
        swapped = False  # Track if any swaps occur during this pass
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges += 1
                swapped = True
        if not swapped:  # Exit early if no swaps occurred
            break
    return exchanges

# Test lists
a_list1 = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
a_list2 = [9, 3, 5, 1, 7]
a_list3 = [89, 45, 68, 90, 29, 34, 17, 70, 12, 18, 24, 53, 94, 52, 45, 23, 25, 36, 75, 61]

# Function to test and time sorting algorithms
def test_sorting_algorithm(sort_func, a_list, list_name, sort_name):
    start_time = time.perf_counter()
    exchanges = sort_func(a_list[:])  # Sort the copy of the list to avoid in-place sorting
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{sort_name} Exchanges for {list_name}: {exchanges}, Time: {elapsed_time:.10f} seconds")

# Test insertion sort on all lists
print("Insertion Sort Analysis:")
test_sorting_algorithm(insertion_sort, a_list1, "nearly sorted list", "Insertion Sort")
test_sorting_algorithm(insertion_sort, a_list2, "small random list", "Insertion Sort")
test_sorting_algorithm(insertion_sort, a_list3, "large random list", "Insertion Sort")

# Test selection sort on all lists
print("\nSelection Sort Analysis:")
test_sorting_algorithm(selection_sort, a_list1, "nearly sorted list", "Selection Sort")
test_sorting_algorithm(selection_sort, a_list2, "small random list", "Selection Sort")
test_sorting_algorithm(selection_sort, a_list3, "large random list", "Selection Sort")

# Test bubble sort on all lists
print("\nBubble Sort Analysis:")
test_sorting_algorithm(bubble_sort, a_list1, "nearly sorted list", "Bubble Sort")
test_sorting_algorithm(bubble_sort, a_list2, "small random list", "Bubble Sort")
test_sorting_algorithm(bubble_sort, a_list3, "large random list", "Bubble Sort")
