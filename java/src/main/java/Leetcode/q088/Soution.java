package main.java.Leetcode.q088;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(n == 0) return;
        int j=0;
        for(int i=0; i<m+n; i++){
            if(nums1[i] >= nums2[j]){
                for(int k = m+j; k>i; k--){
                    nums1[k] = nums1[k-1];
                }
                nums1[i] = nums2[j];
                j++;
            }
            if(i >= m + j){
                nums1[i] = nums2[j];
                j++;
            }
            if(j == n) break;
        }

    }
}