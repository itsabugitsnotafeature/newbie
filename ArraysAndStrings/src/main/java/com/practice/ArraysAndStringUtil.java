package com.practice;

import java.util.Arrays;

public class ArraysAndStringUtil {
	
	public static boolean isPermutationSecond ( String first, String second ) {
		System.out.println("String#1 : " + first + "  String#2 : " + second);
		
		if (first.length() != second.length())
			return false;
		
		int[] letters = new int[256];	// Assumption
		char[] firstArray = first.toCharArray();
		
		for (char c : firstArray) {
			letters[c]++;
		}
		
		for (int i=0; i < second.length() ; i++ ) {
			char c = second.charAt(i);
			if ( --letters[c] < 0)
				return false;
		}
		return true;
	}
	
	
	public static boolean isPermutation ( String first, String second ) {
		System.out.println("String#1 : " + first + "  String#2 : " + second);
		
		if ( first.length() != second.length())
			return false;
//		System.out.println("1 : " + firstContent);
//		System.out.println("1 : " + secondContent);
		return false;

	}
	
	private String sort (String input) { 
		char [] content	= input.toCharArray();
		Arrays.sort(content);
		return new String(content);
	}
	
	
}
