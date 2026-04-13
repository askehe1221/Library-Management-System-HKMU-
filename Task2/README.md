# Task 2: Binary Tree and Heap Sort

## Project Introduction

This project contains implementations and analyses of binary tree data structure and heap sort algorithm. Through this project, you can learn about the basic concepts, implementation methods, and application scenarios of binary trees, as well as the principles, implementation, and performance analysis of heap sort algorithm.

## Directory Structure

```
task2/
├── binary_tree.py       # Binary tree implementation
├── heap_sort.py         # Heap sort implementation
├── 二叉树报告.md        # Detailed report on binary tree data structure
├── 堆排序报告.md        # Detailed report on heap sort algorithm
├── 完善建议.md          # Improvement suggestions for binary tree and heap sort
└── README.md            # This file
```

## Main Files Description

### 1. binary_tree.py

Implements basic binary tree functions, including:
- Node addition
- Four traversal methods (pre-order, in-order, post-order, level-order)
- Calculating tree height and node count
- Finding nodes and maximum/minimum values

### 2. heap_sort.py

Implements the heap sort algorithm, including:
- Recursive and non-recursive versions of heapify function
- Support for ascending and descending sort
- Efficient sorting with O(n log n) time complexity

### 3. 二叉树报告.md (Binary Tree Report)

Detailed introduction to binary trees:
- Basic concepts and properties
- Application scenarios (binary search tree, balanced binary tree, heap, etc.)
- Implementation methods and code analysis
- Time complexity analysis
- Examples and usage methods

### 4. 堆排序报告.md (Heap Sort Report)

Detailed introduction to heap sort:
- Basic concepts and principles
- Application scenarios (priority queue, sorting, selection problems)
- Implementation methods and code analysis
- Time complexity analysis
- Advantages and disadvantages analysis

### 5. 完善建议.md (Improvement Suggestions)

Provides improvement suggestions for binary tree and heap sort, including:
- Function enhancement suggestions
- Code optimization suggestions
- Performance improvement suggestions
- Extensibility suggestions

## How to Use

### Run Binary Tree Example

```python
# Run binary tree test
python binary_tree.py
```

### Run Heap Sort Example

```python
# Run heap sort test
python heap_sort.py
```

## Technical Points

### Binary Tree
- **Data Structure**: Non-linear data structure where each node has at most two children
- **Traversal Methods**: Pre-order, in-order, post-order, level-order
- **Application Scenarios**: Binary search tree, balanced binary tree, heap, Huffman tree, expression tree
- **Time Complexity**: Traversal O(n), search in binary search tree average O(log n)

### Heap Sort
- **Algorithm Principle**: Sorting algorithm based on heap data structure
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1) (in-place sorting)
- **Application Scenarios**: Priority queue, large-scale data sorting, selection problems

## Learning Points

Through this project, you can learn:
- Basic concepts and implementation methods of binary trees
- Principles and implementation of heap sort algorithm
- Time complexity analysis of data structures and algorithms
- Application scenarios of different data structures and algorithms
- Methods for code optimization and performance improvement

## Summary

This project provides complete implementations and detailed analyses of binary tree and heap sort, serving as a good resource for learning data structures and algorithms. By understanding and running these codes, you can deepen your understanding of binary trees and heap sort, laying a foundation for more complex algorithm learning.