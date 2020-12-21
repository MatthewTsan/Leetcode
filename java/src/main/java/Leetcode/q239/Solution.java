package main.java.Leetcode.q239;

import java.util.*;

class Solution {
    ArrayDeque<Integer> deq = new ArrayDeque<>();
    int[] nums;

    private void clean_deque(int i, int k){
        if(!deq.isEmpty() && deq.getFirst() == i - k){
            deq.removeFirst();
        }

        while(!deq.isEmpty() && nums[i] > nums[deq.getLast()]){
            deq.removeLast();
        }
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if(n == 0 || k == 0){
            return new int[0];
        }
        if(k == 1){
            return nums;
        }
        this.nums = nums;
        int[] ans = new int[n-k+1];
        for(int i=0; i<k; i++){
            clean_deque(i, k);
            deq.addLast(i);
        }
        ans[0] = nums[deq.getFirst()];
        for(int i=k; i<n; i++){
            clean_deque(i, k);
            deq.addLast(i);
            ans[i-k+1] = nums[deq.getFirst()];
        }
        return ans;
    }
}