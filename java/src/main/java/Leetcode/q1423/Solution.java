package main.java.Leetcode.q1423;

class Solution {
    public int maxScore(int[] cardPoints, int k) {
        if(cardPoints.length == 0 || k == 0){
            return 0;
        }
        int leftSum = 0, rightSum = 0, ans = 0;
        for(int i=0; i<k; i++){
            leftSum = leftSum + cardPoints[i];
        }
        if(k == cardPoints.length){
            return leftSum;
        }
        int l=k-1, r=cardPoints.length-1;
        ans = leftSum;
        while(l >= 0){
            leftSum = leftSum - cardPoints[l];
            rightSum = rightSum + cardPoints[r];
            ans = Math.max(ans, leftSum + rightSum);
            l--;
            r--;
        }
        return ans;
    }
}
