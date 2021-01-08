package main.java.Leetcode.q234;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null) return true;
        ListNode slow=head, fast=head, preFast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            preFast = fast.next;
            fast = fast.next.next;
        }
        if(fast == null) fast = preFast;

        ListNode mid = slow; //mid or the begining of the second Linked list

        ListNode cur = mid.next, pre = mid;
        mid.next = null;
        while(cur != null){
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }

        ListNode p1 = head, p2 = fast;
        while(p1 != null && p2 != null){
            if(p1.val == p2.val){
                p1 = p1.next;
                p2 = p2.next;
            } else{
                return false;
            }
        }
        return true;
    }
}
