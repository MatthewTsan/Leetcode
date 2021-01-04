package main.java.Leetcode.q759;

/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

import java.util.*;

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> ans = new ArrayList<>();
        PriorityQueue<Interval> minHeap = new PriorityQueue<>(
                (x, y) -> Integer.compare(x.start, y.start));
        for(List<Interval> l: schedule){
            for(Interval interval: l){
                minHeap.add(interval);
            }
        }
        int startTime = 0;
        while(minHeap.size() != 0){
            Interval job = minHeap.poll();
            startTime = job.end;
            while(!minHeap.isEmpty() && minHeap.peek().end <= startTime){
                minHeap.poll();
            }
            if(!minHeap.isEmpty() && minHeap.peek().start > startTime){
                ans.add(new Interval(startTime, minHeap.peek().start));
            }
        }
        return ans;
    }
}