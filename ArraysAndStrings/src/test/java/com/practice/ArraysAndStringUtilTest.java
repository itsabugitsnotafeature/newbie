package com.practice;

import org.junit.Ignore;
import org.junit.Test;

import junit.framework.TestCase;

public class ArraysAndStringUtilTest extends TestCase {

	@Test
	public void testCompressByMe() {
//		System.out.println("EXPECTED: a2c6e1i6l3m2n4o9p2r2s4t1u2v1 \n  ACTUAL: "+ 
//				ArraysAndStringUtil.compressByMe("pneumonoultramicroscopicsilicovolcanoconiosis"));
		assertEquals("a2c6e1i6l3m2n4o9p2r2s4t1u2v1",
					ArraysAndStringUtil.compressByMe("pneumonoultramicroscopicsilicovolcanoconiosis"));
		assertEquals("a5b5c5d5",
				ArraysAndStringUtil.compressByMe("dbdabcabcabdcacbcadd"));
	}

	
	
	
	
	@Ignore
	@Test
	public void testCompressByBook() {
		System.out.println("EXPECTED: a4b4c5e3f1 \n  ACTUAL: "+ 
					ArraysAndStringUtil.compressByBook("aaabbcccccaeeebbf"));
		//		System.out.println("EXPECTED: a3b1c4 \n  ACTUAL: "+ ArraysAndStringUtil.compressByBook("aaabccccc"));
	}


	@Ignore
	@Test
	public void testReplaceAllWith20Percent() {
		char[] b = new char[20];
		b[0] = 'a';
		b[1] = ' ';
		b[2] = 'b';
		b[3] = ' ';
		b[4] = 'c';

		assertEquals("", ArraysAndStringUtil.replaceAllWith20Percent(b, 5));
	}



	/*
	@Test
	public void testIsPermutation() {
		assertFalse(ArraysAndStringUtil.isPermutation("aabbcc","ccaabb"));
		assertFalse(ArraysAndStringUtil.isPermutation("O, Draconian devil!","Oh, lame saint!"));
	}
	 */
	@Ignore
	@Test
	public void testIsPermutationSecond() {
		assertTrue(ArraysAndStringUtil.isPermutationSecond("aabbcc","ccaabb"));
		assertFalse(ArraysAndStringUtil.isPermutationSecond("o, draconian devil!","oh, lame saint!"));
		assertTrue(ArraysAndStringUtil.isPermutationSecond("dormitory","dirtyroom"));
		assertTrue(ArraysAndStringUtil.isPermutationSecond("aeaabccdddeeeee","dbeceaeceadadee"));
		assertTrue(ArraysAndStringUtil.isPermutationSecond("",""));

		assertTrue(ArraysAndStringUtil.isPermutationSecond("AAAABBCDEF","CADAFBABEA"));
	}


}
