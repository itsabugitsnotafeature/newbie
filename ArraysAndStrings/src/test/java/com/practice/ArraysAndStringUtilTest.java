package com.practice;

import org.junit.Test;

import junit.framework.TestCase;

public class ArraysAndStringUtilTest extends TestCase {
	
	/*
	@Test
	public void testIsPermutation() {
		assertFalse(ArraysAndStringUtil.isPermutation("aabbcc","ccaabb"));
		assertFalse(ArraysAndStringUtil.isPermutation("O, Draconian devil!","Oh, lame saint!"));
	}
	*/
	
	@Test
	public void testIsPermutationSecond() {
		assertTrue(ArraysAndStringUtil.isPermutationSecond("aabbcc","ccaabb"));
		assertFalse(ArraysAndStringUtil.isPermutationSecond("o, draconian devil!","oh, lame saint!"));
		assertTrue(ArraysAndStringUtil.isPermutationSecond("dormitory","dirtyroom"));
		assertTrue(ArraysAndStringUtil.isPermutationSecond("aeaabccdddeeeee","dbeceaeceadadee"));
	}

}
