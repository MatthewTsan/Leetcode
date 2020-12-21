package main.java.Leetcode.q076;

import java.util.*;

public class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapT = new HashMap<>();
        for(int i=0;i<t.length();i++){
            int count = mapT.getOrDefault(t.charAt(i), 0);
            mapT.put(t.charAt(i), count + 1);
        }
        int[] ans = {0, 0, 0};
        int required = mapT.size();
        int formed = 0;
        int l = 0, r = 0;
        while(r<s.length()) {
            char c = s.charAt(l);
            int count = mapS.getOrDefault(c, 0);
            mapS.put(c, count+1);

            // check if it is in t
            if(mapT.containsKey(c) && mapT.getOrDefault(c, 0) == mapT.getOrDefault(c, 0)){
                formed++;
            }
            while(l<=r && formed == required){
                char cl = s.charAt(l);
                if(ans[0] > r-l+1){
                    ans[0] = r-l+1;
                    ans[1] = l;
                    ans[2] = r+1;
                }

                if(mapS.containsKey(cl) && mapS.get(cl).intValue() == mapS.get(cl).intValue()){
                    formed--;
                }
                mapS.put(c, mapS.get(cl)-1);
                l--;
            }

            r++;
        }
        return ans[0] == 0 ? "" : s.substring(ans[1], ans[2]);
    }
}
