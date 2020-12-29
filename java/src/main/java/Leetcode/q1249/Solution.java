package main.java.Leetcode.q1249;
import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> stack = new Stack<>();
        Set<Integer> delete = new HashSet<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                stack.push(i);
            } else if(c == ')'){
                if(stack.empty()){
                    delete.add(i);
                } else{
                    stack.pop();
                }
            }
        }
        while(!stack.empty()){
            delete.add(stack.pop());
        }

        StringBuilder str = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            if(!delete.contains(i)) {
                str.append(s.charAt(i));
            }
        }
        return str.toString();
    }
}