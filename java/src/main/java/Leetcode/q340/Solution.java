package main.java.Leetcode.q340;

import java.util.*;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if(s.length() == 0) return 0;
        Map<Character, Integer> map = new HashMap<>();
        int num = 0;
        int l=0, r=0, ans=0;
        for(r=0; r<s.length(); r++){
            int count = map.getOrDefault(s.charAt(r), 0);
            map.put(s.charAt(r), count+1);
            if(count == 0){
                num++;
            }
            while(num > k){
                count = map.get(s.charAt(l)).intValue();
                map.put(s.charAt(l), count-1);
                if(count == 1){
                    num--;
                }
                l++;
            }
            ans = Math.max(ans, r-l+1);
        }
        return ans;
    }
}