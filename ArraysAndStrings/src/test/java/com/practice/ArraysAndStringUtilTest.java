package com.practice;

import org.junit.Test;

import junit.framework.TestCase;

public class ArraysAndStringUtilTest extends TestCase {
	
	@Test
	public void testIsPermutation() {
		assertFalse(ArraysAndStringUtil.isPermutation("aabbcc","ccaabb"));
		
//		assertFalse(ArraysAndStringUtil.isPermutation("O, Draconian devil!","Oh, lame saint!"));
	}

}
