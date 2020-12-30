package main.java.Leetcode.q042;
import java.util.*;

class Solution {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int ans = 0;
        for(int i=0; i<height.length; i++){
            if(stack.isEmpty() || height[i] <= height[stack.peek()]){
                stack.push(i);
                continue;
            } else{
                while(!stack.isEmpty() && height[stack.peek()] < height[i]){
                    int lower = stack.pop();
                    if(stack.isEmpty()){
                        stack.push(i);
                        continue;
                    }
                    int distence = i - stack.peek() - 1;
                    int hDiff = Math.min(height[i], height[stack.peek()]) - height[lower];
                    ans += distence * hDiff;
                }
                stack.push(i);
            }
        }
        return ans;
    }
}