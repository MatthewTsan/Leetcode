# Leetcode

## Brute force
+ 012 M:

## Basic method
+ q121 E:
    find the max diff in one pass
+ q146 M:
    queue and dictionary

+ q238 M:
    result = left * right

+ q721 M:    
    DSU and dictionary

+ q876 E:
    fast and slow on linkedList to find the middle.


## Sliding windows
+ q076 H:
    Sliding window. Two dictions, with flag to decrease mathching process
    
+ q424:
    Understand k, then regular sliding windows
    
+ q904:
    facing problems with multiple same numbers: consider sum it up.


## Heap
+ q295:
    small num into maxHeap. big num into minHeap.


## Sorting
+ q056:
    sort all beginings and merge. QuickSort algorithm in.

+ q075
    One time traverse: for k to the end. 0-i is 0 and j-len(list) is 2, 1 will be left in the middle

+ q148 E:
    Typical merge sort.
    
+ q287 M:
    Basket sort
    
+ q1528:
    Note:
    + list to str: use "".join(list)
    + Use bucketSort in small size data
    
## Link list
+ q019 M:
    create one pointer before n stops of cur
    
+ q021 E: 
    merge two link list
    
+ q023 H:
    merge K link list, use heap
   
+ q092 M:
    reverse, just be careful
    
+ q138 M:
    make dict.

+ q143 M:
    Split, reverse, merge

+ q148 E:
    Typical merge sort on link list.

## Dynamic programing
+ q010 H
    note: on "*" or not

+ q053:
    Note: anylize all the hiden information.
    
+ q062 M: easy

+ 063 M:
    note: be careful if the rock in edge

+ q064

+ q72 H

+ q91 M
    not complete. Not a good one for DP

+ q120 M: typically DP

+ q152:
    colulate max and min
    
+ q416 M:
    package question.
    

## Greedy
+ q055

+ q134

+ q376

+ q402
    Note: min number must be increase. To minimize, remove the peak. To get the most min number, remove the first peak.

## DFS
+ 046 M:
Do DFS with recursive

+ 078 M: 
Do DFS with recursive.

+ 200 M:
DFS to count island

## Recursive
+ q095 M: Typically recursive. 
    Time complexity could be large, n is small: 0<= n <= 8.
    
+ q096 M: recursive + mem


## Tree


## Binary Search Tree
Add BST template into /template/BST

+ q144
    Two ways: Recursive and Stack

+ q1038
    Note: Do DFS with sum in right-left order. 