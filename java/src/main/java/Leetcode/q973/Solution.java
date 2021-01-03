package main.java.Leetcode.q973;
import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<int[]>(points.length,
                new Comparator<int[]>(){
                    public int compare(int[] a, int[] b){
                        double dist1 = Math.sqrt(Math.pow(a[0], 2) + Math.pow(a[1], 2));
                        double dist2 = Math.sqrt(Math.pow(b[0], 2) + Math.pow(b[1], 2));
                        return -Double.compare(dist1, dist2);
                    }
                });

        for(int i=0; i<points.length; i++){
            maxHeap.offer(points[i]);
        }
        while(maxHeap.size() > K) maxHeap.poll();

        int[][] ans = new int[K][2];
        int i=0;
        while(maxHeap.size() >0){
            ans[i] = maxHeap.poll();
            // System.out.println(ans[i][0] + " " + ans[i][1] + " " + ans[i][2]);
            i++;
        }
        return ans;
    }
}