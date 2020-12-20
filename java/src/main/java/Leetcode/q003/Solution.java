package main.java.Leetcode.q003;

import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int maxLen = 0, i=0, j=0;
        while(i<n && j<n){
            if(set.contains(s.charAt(j))) {
                set.remove(s.charAt(i));
                i += 1;
            } else{
                set.add(s.charAt(j));
                j += 1;
                maxLen = Math.max(maxLen, j-i);
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "abcabcbb";
        int ans = solution.lengthOfLongestSubstring(s);
        System.out.println(ans);
    }
}