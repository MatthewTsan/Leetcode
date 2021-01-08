package main.java.Leetcode.q532;


import java.util.Arrays;

class Solution {
    public int findPairs(int[] nums, int k) {
        Arrays.sort(nums);
        int i=0, j=0;
        int ans = 0;
        while(j<nums.length){
            if(i==j){
                j++;
                continue;
            }
            if(nums[j] - nums[i] == k){
                ans++;
                j++;
            } else if(nums[j] - nums[i] < k){
                j++;
            } else{
                i++;
            }
            while(j<nums.length && nums[j-1] == nums[j]) j++;
            while(i>0 && i<j && nums[i-1] == nums[i]) i++;
        }
        return ans;
    }
}