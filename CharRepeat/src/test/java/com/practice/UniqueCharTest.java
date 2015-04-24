package com.practice;

import org.junit.Test;

import junit.framework.TestCase;

public class UniqueCharTest extends TestCase {
	
	@Test
	public void testGetFirstNonRepeatedChar() {
      assertEquals('b', UniqueChar.firstNonRepeatedCharacter("abcdefghija")); 
      assertEquals('h', UniqueChar.firstNonRepeatedCharacter("hello")); 
      assertEquals('J', UniqueChar.firstNonRepeatedCharacter("Java")); 
      assertEquals('i', UniqueChar.firstNonRepeatedCharacter("simplest"));
	}

	@Test
	public void testFirstNonRepeatingChar() {
//		fail("Not yet implemented");
	}
	
	@Test
	public void testFirstNonRepeatedCharacter() {
//		fail("Not yet implemented");
	}

}
