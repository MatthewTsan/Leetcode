package main.java.Leetcode.q394;
import java.util.*;

class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c == ']') {
                char topE = stack.pop();
                ArrayList<Character> arr = new ArrayList<Character>();
                while(topE != '['){
                    arr.add(topE);
                    topE = stack.pop();
                }
                String strNum = String.valueOf(stack.pop());
                topE = stack.empty()? '#' : stack.peek();
                while(Character.isDigit(stack.empty()? '#': stack.peek())){
                    strNum = String.valueOf(stack.pop()) + strNum;
                }
                int time = Integer.parseInt(strNum);

                for(int j=0; j<time; j++){
                    for(int k=arr.size(); k>0; k--){
                        stack.push(arr.get(k-1));
                    }
                }
            } else{
                stack.push(c);
            }
        }
        String ans = "";
        for(int i=0; i<stack.size(); i++){
            ans = ans.concat(String.valueOf(stack.get(i)));
        }
        return ans;
    }

}