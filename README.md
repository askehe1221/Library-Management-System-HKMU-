# Library Management System

## Project Description

This is a fully functional library management system with a beautiful GUI interface. It supports book management, borrowing management, statistical analysis, and borrowing record management. The system is written in Python, uses the tkinter library to implement the graphical interface, and uses JSON files for data storage to ensure data persistence.

## Features

### 1. Book Management
- Add new books (supports setting book ID, name, author, and category)
- Multi-condition search for books (supports searching by ID, name, author, and category)
- Delete books
- View all book lists

### 2. Borrowing Management
- Borrow books (requires entering book ID and borrower name)
- Return books (requires entering book ID)
- View current unreturned borrowing records

### 3. Statistical Analysis
- Overall statistics: total number of books, available books, borrowed books
- Category statistics: number of books in each category, available quantity, and borrowed quantity

### 4. Borrowing Records
- View all borrowing records, including borrowing date and return date

### 5. Data Persistence
- Automatically save data to `library_data.json` file
- Automatically load previous data when the program starts

## Project Structure

```
task1/
├── book.py          # Book class, defines book attributes and methods
├── library.py       # Library class, implements core functions for book and borrowing management
├── gui.py           # GUI interface implementation
├── main.py          # Program entry point
├── menu.py          # Command line menu 
├── library_data.json # Data storage file
```

## How to Run

1. Ensure Python 3.x is installed on your computer
2. Open the command line terminal and navigate to the project directory
3. Run the following command to start the system:

```bash
python main.py
```

4. After the system starts, you will see a beautiful GUI interface and can start using various functions

## Usage Instructions

### 1. Book Management
- **Add Book**: In the "Book Management" tab, fill in the book ID, name, author, and category, then click the "Add Book" button
- **Search Book**: In the "Book Management" tab, select the search condition (ID, name, author, or category), enter keywords, then click the "Search" button
- **Delete Book**: In the "Book Management" tab, select the book to delete from the book list, then click the "Delete Book" button

### 2. Borrowing Management
- **Borrow Book**: In the "Borrow Management" tab, fill in the book ID and borrower name, then click the "Borrow Book" button
- **Return Book**: In the "Borrow Management" tab, fill in the book ID, then click the "Return Book" button

### 3. Statistical Analysis
- In the "Statistics" tab, you can view the overall statistics and category statistics of books

### 4. Borrowing Records
- In the "Borrow Records" tab, you can view all borrowing records, including returned and unreturned records

## Notes

1. Book IDs must be unique and cannot be duplicated
2. You must enter the borrower's name when borrowing books
3. Data will be automatically saved to the `library_data.json` file, no manual saving required
4. If the `library_data.json` file does not exist, the system will automatically create it and add some initial book data

## Technical Implementation

- **Programming Language**: Python 3.x
- **GUI Library**: tkinter
- **Data Storage**: JSON file
- **Main Classes**:
  - `Book`: Book class, defines book attributes and methods
  - `Library`: Library class, implements core functions for book and borrowing management
  - `LibraryGUI`: GUI interface class, implements graphical interface and user interaction

## Initial Data

When the system starts, if there is no `library_data.json` file, the following initial book data will be automatically added:

1. Python Programming - Jack (Computer Science)
2. Data Structures - Li (Computer Science)
3. Algorithms - He (Computer Science)
4. Introduction to Physics - Smith (Science)
5. World History - Johnson (History)

## Future Improvement Directions

1. Add user login functionality to distinguish between administrators and ordinary users
2. Implement book reservation functionality
3. Add book recommendation system
4. Implement barcode scanning functionality
5. Optimize interface design and add more animation effects

## Contribution

Welcome to provide suggestions and improvements for this project!
# Task 2: Binary Tree and Heap Sort

## Project Introduction

This project contains implementations and analyses of binary tree data structure and heap sort algorithm. Through this project, you can learn about the basic concepts, implementation methods, and application scenarios of binary trees, as well as the principles, implementation, and performance analysis of heap sort algorithm.

## Directory Structure

```
task2/
├── binary_tree.py       # Binary tree implementation
├── heap_sort.py         # Heap sort implementation
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

This project provides complete implementations and detailed analyses of binary tree and heap sort, serving as a good resource for learning data structures and algorithms. By understanding and running these codes, you can deepen your understanding of binary trees and heap sort, laying a foundation for more complex algorithm learning
