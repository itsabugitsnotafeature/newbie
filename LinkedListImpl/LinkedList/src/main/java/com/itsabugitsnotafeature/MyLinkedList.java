package com.itsabugitsnotafeature;

public class MyLinkedList {

	Node head = null ; 

	public boolean addNode ( int data ) {
		if ( this.head == null ) {
			Node newNode = new Node(data, null);
			head = newNode;
			return true;
		}	else {
			return appendLinkedList(data);
		}
	}

	private boolean appendLinkedList(int data) {
		if ( this.head == null ) {
			return addNode(data);
		}

		Node newNode = new Node(data, null);
		Node currentNode = head;

		while ( currentNode.getNext() != null )	{
			currentNode = currentNode.getNext();
		}
		currentNode.setNext(newNode);
		return true;
	}

	public void printLinkedList() {
		if ( this.head == null ) {
			System.out.println("No Linked list to print");
		}

		Node currentNode = head;
		System.out.println("\nLinkedList ::");
		while ( currentNode != null )	{
			System.out.print( currentNode.getData() + "-->");
			currentNode = currentNode.getNext();
		}
		System.out.println("\n<<END>>");
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
