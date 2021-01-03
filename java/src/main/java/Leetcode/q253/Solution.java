package main.java.Leetcode.q253;
import java.util.*;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if(intervals.length == 0) return 0;

        PriorityQueue<int[]> minHeap = new PriorityQueue<int[]>(intervals.length,
                new Comparator<int[]>() {
                    public int compare(int[] a, int[] b){
                        return Integer.compare(a[1], b[1]);
                    }
                });

        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] a, int[] b){
                return Integer.compare(a[0], b[0]);
            }
        });

        minHeap.add(intervals[0]);
        for(int i=1; i<intervals.length; i++){
            if(intervals[i][0] >= minHeap.peek()[1]){
                minHeap.poll();
            }
            minHeap.add(intervals[i]);
        }

        return minHeap.size();
    }
}