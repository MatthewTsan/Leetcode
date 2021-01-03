package main.java.Leetcode.q023;

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
import java.util.*;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;
        ListNode head = new ListNode();
        ListNode p = head;
        PriorityQueue<ListNode> minHeap = new PriorityQueue<ListNode>(lists.length,
                (a, b) -> a.val - b.val);
        for(int i=0; i<lists.length; i++){
            if(lists[i] != null) minHeap.offer(lists[i]);
        }

        while(!minHeap.isEmpty()){
            ListNode minList = minHeap.poll();
            ListNode next = minList.next;
            p.next = minList;
            p = p.next;
            p.next = null;
            if(next != null){
                minHeap.offer(next);
            }
        }
        return head.next;
    }
}