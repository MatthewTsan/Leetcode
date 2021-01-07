package main.java.Leetcode.q763;


import java.util.*;


class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> ans = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();

        for(int i=0; i<S.length(); i++){
            map.put(S.charAt(i), i);
        }

        int bg=0, ed=0;
        for(int i=0; i<S.length(); i++){
            ed = Math.max(ed, map.get(S.charAt(i)));
            if(i == ed){
                ans.add(ed-bg+1);
                bg = i+1;
            }
        }

        return ans;
    }
}