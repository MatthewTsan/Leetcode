package main.java.Leetcode.q002;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, cur = dummyHead;
        int left = 0;
        while(p != null || q != null){
            int x = (p == null)? 0: p.val;
            int y = (q == null)? 0: q.val;
            int sum = x + y + left;
            cur.next = new ListNode(sum % 10);
            left = sum / 10;
            cur = cur.next;
            p = (p == null)? p:p.next;
            q = (q == null)? q:q.next;
        }
        cur.next = (left == 0)? null: new ListNode(left);
        return dummyHead.next;
    }
}
