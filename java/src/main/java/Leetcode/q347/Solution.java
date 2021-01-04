package main.java.Leetcode.q347;

import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        for(int key : map.keySet()){
            minHeap.add(new int[]{key, map.get(key)});
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
        int[] ans = new int[k];
        System.out.println();
        while(!minHeap.isEmpty()){
            ans[k-1] = minHeap.poll()[0];
            k --;
        }
        return ans;
    }
}