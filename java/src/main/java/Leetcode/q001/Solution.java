package main.java.Leetcode.q001;

import java.util.*;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            int complement = target - nums[i];
            if(map.containsKey(nums[i])){
                return new int[] {i, map.get(nums[i])};
            }
            map.put(complement, i);
            System.out.println(map);
        }
        throw new IllegalArgumentException("No result in given nums[]");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }
}
