package main.java.Leetcode.q1004;

class Solution {
    public int longestOnes(int[] A, int K) {
        int ans = 0;
        int left=0, right=0, count=0;
        for(right=0; right<A.length; right++){
            if(A[right] == 0){
                count++;
            }
            while(count>K){
                if(A[left] == 0){
                    count--;
                }
                left++;
            }
            ans = Math.max(ans, right-left+1);
        }
        return ans;

    }
}