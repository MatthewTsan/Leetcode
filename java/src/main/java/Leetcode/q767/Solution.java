package main.java.Leetcode.q767;
import java.util.*;

class Solution {
    public String reorganizeString(String S) {
        if(S.length() == 0) return "";
        StringBuilder ans = new StringBuilder();
        Map<Character, Integer> map = new HashMap<>();
        PriorityQueue<Character> heap = new PriorityQueue<>(
                (x, y) -> -Integer.compare(map.getOrDefault(x, 0), map.getOrDefault(y, 0))
        );

        for(int i=0; i<S.length(); i++){
            char c = S.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for(char key: map.keySet()){
            heap.add(key);
            if(map.get(key) > (S.length() + 1) / 2) return "";
        }

        while(heap.size() >= 2){
            char c1 = heap.poll();
            char c2 = heap.poll();
            ans.append(c1);
            ans.append(c2);
            map.put(c1, map.get(c1) - 1);
            map.put(c2, map.get(c2) - 1);
            if(map.get(c1) != 0) heap.add(c1);
            if(map.get(c2) != 0) heap.add(c2);
        }
        if(!heap.isEmpty()) ans.append(heap.poll());
        return ans.toString();
    }
}
