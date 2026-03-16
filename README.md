# MSCS532 Assignment 2
Divide and Conquer Algorithms: Merge Sort and Quick Sort Implementation and Performance Analysis

## Overview
This project implements two classic divide-and-conquer sorting algorithms: **Merge Sort** and **Quick Sort**.  
The goal of the assignment is to analyze the behavior and performance of these algorithms when applied to datasets of different sizes and conditions.

The project includes implementations of both algorithms and a performance testing script used to compare execution time and memory usage.

## Files Included

README.md  
Project documentation and overview.

merge_sort.py  
Implementation of the Merge Sort algorithm.

performance_test.py  
Script used to generate datasets and measure the performance of both sorting algorithms.

quick_sort.py  
Implementation of the Quick Sort algorithm.


## Algorithms Implemented

### Merge Sort
Merge Sort follows a divide-and-conquer approach by recursively dividing the list into smaller sublists and then merging them in sorted order. It guarantees a time complexity of **O(n log n)** in all cases but requires additional memory for merging.

### Quick Sort
Quick Sort also uses a divide-and-conquer strategy by selecting a pivot element and partitioning the array around it. It typically performs very efficiently in practice with an average time complexity of **O(n log n)**, although its worst-case complexity can reach **O(n²)**.

## Performance Analysis
The performance testing script evaluates both algorithms using datasets of varying sizes.  
The results highlight the differences in execution time and memory usage between Merge Sort and Quick Sort under different input conditions.

## Author
Ranjith Kumar Bollam

## Course
MSCS 532 – Algorithms and Data Structures,
University of the Cumberlands
