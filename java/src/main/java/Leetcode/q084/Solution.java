package main.java.Leetcode.q084;
import java.util.*:

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

public class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack < Integer > stack = new Stack < > ();
        stack.push(-1);
        int maxarea = 0;
        for (int i = 0; i < heights.length; ++i) {
            System.out.println(stack.toString());
            while (stack.peek() != -1 && heights[stack.peek()] >= heights[i])
                maxarea = Math.max(maxarea, heights[stack.pop()] * (i - stack.peek() - 1));
            stack.push(i);
        }
        while (stack.peek() != -1){
            System.out.println(stack.toString());
            maxarea = Math.max(maxarea, heights[stack.pop()] * (heights.length - stack.peek() -1));
        }
        return maxarea;
    }
}
