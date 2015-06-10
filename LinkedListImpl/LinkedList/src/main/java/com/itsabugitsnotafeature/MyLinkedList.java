package com.itsabugitsnotafeature;

import java.util.Hashtable;

public class MyLinkedList {
	Node head = null ; 


	public Node getHead() {
		return head;
	}


	public void setHead(Node head) {
		this.head = head;
	}

	public void removeDuplicatesWithoutBuffer() {
		if ( this.getHead() == null )
			return;
		Node current = this.getHead();

		while (current != null) {
			Node runner = current;
			while (runner.getNext() != null ) {
			if ( runner.getNext().getData() == current.getData() )
				runner.setNext(runner.getNext().getNext());
			else
				runner = runner.getNext();
			}
			current = current.getNext();
		}
	}

	public void removeDuplicatesWithBuffer() {
		if ( this.getHead() == null )
			return;

		Hashtable<Integer, Boolean> table = new Hashtable<Integer, Boolean>();
		Node worker = this.getHead();
		Node prev = null;

		while (worker != null) {
			if (table.containsKey( worker.getData() ) ) {
				prev.setNext(worker.getNext());
			}
			else {
				table.put(worker.getData(), true);
				prev = worker;
			}
			worker = worker.getNext();
		}
	}


	public boolean addNode ( int data ) {
		if ( this.head == null ) {
			Node newNode = new Node(data, null);
			setHead(newNode);
			return true;
		}	else {
			return appendLinkedList(data);
		}
	}

	private boolean appendLinkedList(int data) {
		if ( this.getHead() == null ) {
			return addNode(data);
		}

		Node newNode = new Node(data, null);
		Node currentNode = this.getHead();

		while ( currentNode.getNext() != null )	{
			currentNode = currentNode.getNext();
		}
		currentNode.setNext(newNode);
		return true;
	}

	public void printLinkedList() {
		if ( this.getHead() == null ) {
			System.out.println("No Linked list to print");
		}

		Node currentNode = this.getHead();
		while ( currentNode != null )	{
			System.out.print( currentNode.getData() + "-->");
			currentNode = currentNode.getNext();
		}
	}



	/**
	 * Bit Manipulations
	 * @param number
	 * @param index
	 * @return
	 */
	public boolean getBit(int number, int index) {
		return ( (number & (1 << index) ) != 0 );
	}

	public int setBit(int number, int index) {
		return ( number | ( 1 << index ) );
	}

	public int clearBit(int number, int index) {
		int mask = ~(1 << index);
		return ( number & mask );
	}

	public int clearBitsMSBThroughIndex(int number, int index) {
		int mask = (1 << index) - 1 ;
		return ( number & mask );
	}



	public int clearBitsMSBThroughO(int number, int index) {
		int mask = ~(1 >>> ( 31 - index) );
		return ( number & mask );
	}

	public int updateBit(int number, int index, int value ) {
		int mask = (1 << index) ;
		return ( number & mask ) | ( value << index );
	}






























}
