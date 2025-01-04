# Sorting-Algorithms-Analysis
This Python script implements and analyzes three classic sorting algorithms: **Insertion Sort**, **Selection Sort**, and **Bubble Sort**. The analysis measures the number of exchanges and the time taken to sort various lists.

## Features
- Implements the following sorting algorithms:
  - Insertion Sort
  - Selection Sort
  - Bubble Sort
- Analyzes the performance of these algorithms using:
  - A nearly sorted list: `[1, 2, 3, 4, 5, 7, 6, 8, 9, 10]`
  - A small random list: `[9, 3, 5, 1, 7]`
  - A large random list: `[89, 45, 68, 90, 29, 34, 17, 70, 12, 18, 24, 53, 94, 52, 45, 23, 25, 36, 75, 61]`
- Reports the number of exchanges made during sorting and the time taken for each algorithm.

## Functions

### 1. `insertion_sort(a_list)`
Sorts a list using the insertion sort algorithm and returns the number of exchanges made during sorting.

### 2. `selection_sort(a_list)`
Sorts a list using the selection sort algorithm and returns the number of exchanges made during sorting.

### 3. `bubble_sort(a_list)`
Sorts a list using the bubble sort algorithm and returns the number of exchanges made during sorting.

### 4. `test_sorting_algorithm(sort_func, a_list, list_name, sort_name)`
Tests a sorting algorithm by:
- Timing its execution
- Counting the number of exchanges
- Printing the results for analysis

## How to Run
1. Save the script as a `.py` file (e.g., `sorting_analysis.py`).
2. Run the script using Python:
   ```bash
   python sorting_analysis.py
   ```
3. The script will output the performance metrics for each sorting algorithm and each test list.

## Sample Output
The output includes the number of exchanges and the time taken for each sorting algorithm:

```
Insertion Sort Analysis:
Insertion Sort Exchanges for nearly sorted list: 1, Time: 0.0000025600 seconds
Insertion Sort Exchanges for small random list: 7, Time: 0.0000054300 seconds
Insertion Sort Exchanges for large random list: 72, Time: 0.0000882300 seconds

Selection Sort Analysis:
Selection Sort Exchanges for nearly sorted list: 1, Time: 0.0000075400 seconds
Selection Sort Exchanges for small random list: 3, Time: 0.0000049200 seconds
Selection Sort Exchanges for large random list: 19, Time: 0.0001234100 seconds

Bubble Sort Analysis:
Bubble Sort Exchanges for nearly sorted list: 1, Time: 0.0000056100 seconds
Bubble Sort Exchanges for small random list: 6, Time: 0.0000078100 seconds
Bubble Sort Exchanges for large random list: 94, Time: 0.0001129000 seconds
```

## Purpose
This code demonstrates the differences in efficiency and performance between three basic sorting algorithms. It can be used as a teaching tool or for basic performance benchmarking.

## License
This project is licensed under the MIT License.
