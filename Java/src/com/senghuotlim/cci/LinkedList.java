package com.senghuotlim.cci;

public class LinkedList {
	
	public static void main(String[] args) {
		LinkedList head = new LinkedList();
		for (int i=1; i<=10; i++)
			head.add(i);
		System.out.println(head);
		
		head.reverse();
		System.out.println(head);
	}
	
	Node head;
	
	public void add(int data) {
		if (head == null)
			head = new Node(data, null);
		else {
			Node tmp = head;
			while (tmp.next != null)
				tmp = tmp.next;
			tmp.next = new Node(data, null);
		}
	}
	
	public String toString() {
		String res = "";
		Node tmp = head;
		while (tmp != null) {
			res += " " + tmp.data;
			tmp = tmp.next;
		}
		return res;
	}
	
	public void reverse() {
		Node reverse = reverse(head);
		head.next = null;
		head = reverse;
	}
	
	public Node reverse(Node head) {
		if (head == null || head.next == null)
			return head;
		
		Node next = head.next;
		Node reverse = reverse(head.next);
		next.next = head;
		
		return reverse;
	}
	
}
