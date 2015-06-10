package com.itsabugitsnotafeature;

import org.junit.Test;

import junit.framework.TestCase;

public class MyLinkedListTest extends TestCase {
	MyLinkedList globalTestList = new MyLinkedList();

	/**
	 * @return 
	 * 
	 */
	private MyLinkedList initializeList() {
		MyLinkedList testList = new MyLinkedList();
		testList.addNode(99);
		testList.addNode(1);
		testList.addNode(2);
		testList.addNode(3);
		testList.addNode(4);
		testList.addNode(5);
		testList.addNode(6);
		

		testList.addNode(2);
		testList.addNode(3);
		testList.addNode(4);
		testList.addNode(5);
		
		

		testList.addNode(2);
		testList.addNode(3);
		testList.addNode(6);
		testList.addNode(4);
		testList.addNode(5);
		testList.addNode(99);
		testList.addNode(1);
		
		
		return testList;

	}

	@Test
	public void testAddNode() {
		this.globalTestList = initializeList();
		//      this.globalTestList.printLinkedList();
	}

	@Test
	public void testremoveDuplicatesWithBuffer() {
		this.globalTestList = initializeList();
		System.out.println("\nBEFORE w/Buffer :: ");
		this.globalTestList.printLinkedList();

		this.globalTestList.removeDuplicatesWithBuffer();

		System.out.println("\nAFTER w/Buffer:: ");
		this.globalTestList.printLinkedList();
	}

	@Test
	public void testremoveDuplicatesWithoutBuffer() {
		this.globalTestList = initializeList();
		System.out.println("\nBEFORE wo/Buffer:: ");
		this.globalTestList.printLinkedList();

		this.globalTestList.removeDuplicatesWithoutBuffer();

		System.out.println("\nAFTER wo/Buffer:: ");
		this.globalTestList.printLinkedList();
	}

}
