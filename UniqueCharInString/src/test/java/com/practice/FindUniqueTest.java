package com.practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Ignore;
import org.junit.Test;

import junit.framework.TestCase;

import com.practice.FindUnique;;

public class FindUniqueTest extends TestCase {
	
	@Test
	public void testDivFirstUniqueCharUsingTwoMaps() {
//		divFirstNonRepeating
		assertEquals('b', FindUnique.divFirstNonRepeating("abcdefghija")); 
		assertEquals('h', FindUnique.divFirstNonRepeating("hello")); 
		assertEquals('J', FindUnique.divFirstNonRepeating("Java")); 
		assertEquals('i', FindUnique.divFirstNonRepeating("simplest"));
		assertEquals('c', FindUnique.divFirstNonRepeating("compression"));
		assertEquals('u', FindUnique.divFirstNonRepeating("communication"));
		assertEquals('b', FindUnique.divFirstNonRepeating("aab"));
		assertEquals('b', FindUnique.divFirstNonRepeating("aabacaaaa"));
	}
	
	
	
	@Test
	public void testFindLeastRepeatingCharacter() {
		assertEquals("ab",FindUnique.findLeastRepeatingCharacter("aabbccc"));
		assertEquals("ad",FindUnique.findLeastRepeatingCharacter("abbbcccd"));
		assertEquals("bdfg",FindUnique.findLeastRepeatingCharacter("aaaaabbcccddeeeeeeffgghhh"));
		
	}
	

	@Test
	public void testFirstUniqueCharUsingTwoMaps() {
		assertEquals('b', FindUnique.firstUniqueCharUsingMapAndList("abcdefghija")); 
		assertEquals('h', FindUnique.firstUniqueCharUsingMapAndList("hello")); 
		assertEquals('J', FindUnique.firstUniqueCharUsingMapAndList("Java")); 
		assertEquals('i', FindUnique.firstUniqueCharUsingMapAndList("simplest"));
		assertEquals('c', FindUnique.firstUniqueCharUsingMapAndList("compression"));
		assertEquals('u', FindUnique.firstUniqueCharUsingMapAndList("communication"));
		assertEquals('b', FindUnique.firstUniqueCharUsingMapAndList("aab"));
		assertEquals('b', FindUnique.firstUniqueCharUsingMapAndList("aabacaaaa"));
	}


	@Test
	public void testGetFirstNonRepeatedChar() {
		assertEquals('b', FindUnique.firstNonRepeatedCharacter("abcdefghija")); 
		assertEquals('h', FindUnique.firstNonRepeatedCharacter("hello")); 
		assertEquals('J', FindUnique.firstNonRepeatedCharacter("Java")); 
		assertEquals('i', FindUnique.firstNonRepeatedCharacter("simplest"));
		assertEquals('c', FindUnique.firstNonRepeatedCharacter("compression"));
		assertEquals('u', FindUnique.firstNonRepeatedCharacter("communication"));
		assertEquals('b', FindUnique.firstNonRepeatedCharacter("aab"));
	}

	@Test
	public void testfirstUniqueCharUsingDoubleFor() {
		assertEquals('b', FindUnique.firstUniqueCharUsingDoubleFor("abcdefghija")); 
		assertEquals('h', FindUnique.firstUniqueCharUsingDoubleFor("hello")); 
		assertEquals('J', FindUnique.firstUniqueCharUsingDoubleFor("Java")); 
		assertEquals('i', FindUnique.firstUniqueCharUsingDoubleFor("simplest"));
		assertEquals('c', FindUnique.firstUniqueCharUsingDoubleFor("compression"));
		assertEquals('u', FindUnique.firstUniqueCharUsingDoubleFor("communication"));
		assertEquals('b', FindUnique.firstUniqueCharUsingDoubleFor("aab"));
	}



	@Test
	public void testFasleIsUniqueChars() {
		assertFalse(FindUnique.isUniqueChars("abcdefghija")); 
		assertFalse(FindUnique.isUniqueChars("hello")); 
		assertFalse(FindUnique.isUniqueChars("Java")); 
		assertFalse(FindUnique.isUniqueChars("simplest"));
		assertFalse(FindUnique.isUniqueChars("compression"));
		assertFalse(FindUnique.isUniqueChars("communication"));
		assertFalse(FindUnique.isUniqueChars("aab"));

		assertFalse(FindUnique.isUniqueChars("ABCA"));
	}

	@Test
	public void testTrueIsUniqueChars() {
		assertTrue(FindUnique.isUniqueChars("abc"));
		assertTrue(FindUnique.isUniqueChars("qwertyuiop"));
		assertTrue(FindUnique.isUniqueChars("ed"));
		assertTrue(FindUnique.isUniqueChars("v"));
		assertTrue(FindUnique.isUniqueChars("123456789"));

		assertTrue(FindUnique.isUniqueChars("ABC"));

	}

	@Ignore
	@Test(expected=RuntimeException.class)
	public void testGetFirstNonRepeatedCharException() throws RuntimeException {
		//		FindUnique.firstNonRepeatedCharacter("aabbcc");
	}

}
