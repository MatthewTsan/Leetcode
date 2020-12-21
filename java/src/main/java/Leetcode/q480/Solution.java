package main.java.Leetcode.q480;

import java.util.*;

public class Solution {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];
        for(int i=0; i<k; i++){
            if(maxHeap.size() == 0 || maxHeap.peek() >= nums[i]){
                maxHeap.offer(nums[i]);
            } else{
                minHeap.offer(nums[i]);
            }
            rebalanceHeap();
        }

        for(int i=k; i<nums.length; i++){
            double mid = 0;
            if(maxHeap.size() == minHeap.size()){
                mid = maxHeap.peek() / 2.0 + minHeap.peek() / 2.0;
            } else{
                mid = maxHeap.peek();
            }
            result[i-k] = mid;

            if(maxHeap.peek() >= nums[i]){
                maxHeap.offer(nums[i]);
            } else{
                minHeap.offer(nums[i]);
            }

            int removeNumber = nums[i-k];
            if(removeNumber > mid){
                minHeap.remove(removeNumber);
            }else{
                maxHeap.remove(removeNumber);
            }
            rebalanceHeap();
        }


        if(maxHeap.size() == minHeap.size()){
            result[nums.length - k] = maxHeap.peek() / 2.0 + minHeap.peek() / 2.0;
        } else{
            result[nums.length - k] = maxHeap.peek();
        }
        return result;
    }

    private void rebalanceHeap() {
        if(maxHeap.size()>minHeap.size()+1) {
            minHeap.add(maxHeap.poll());
        } else if(minHeap.size() > maxHeap.size()) {
            maxHeap.add(minHeap.poll());
        }
    }
}

