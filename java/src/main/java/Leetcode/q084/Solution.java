package main.java.Leetcode.q084;
import java.util.*;

class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        for(int i=0; i<heights.length; i++){
            System.out.println(stack.toString());
            while(!stack.isEmpty() && heights[stack.peek()] > heights[i]){
                int top = stack.pop();
                int area = (i - top) * heights[top];
                maxArea = Math.max(maxArea, area);
            }
            stack.push(i);
        }
        while(!stack.isEmpty()){
            System.out.println(stack.toString());
            int top = stack.pop();
            maxArea = Math.max(maxArea, (heights.length - top) * heights[top]);
        }
        return maxArea;
    }
}
