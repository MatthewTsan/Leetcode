package main.java.Leetcode.q295;

import java.util.*;

public class MedianFinder {
    /** initialize your data structure here. */
    PriorityQueue<Integer> minHeap, maxHeap;

    public MedianFinder() {
        this.minHeap = new PriorityQueue<Integer>();
        this.maxHeap = new PriorityQueue<Integer>(10, (a, b) -> b-a);
    }

    public void addNum(int num) {
        this.minHeap.offer(num);
        if(minHeap.size() - maxHeap.size() == 2){
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if(minHeap.size() == maxHeap.size())
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        return minHeap.peek();
    }
}

