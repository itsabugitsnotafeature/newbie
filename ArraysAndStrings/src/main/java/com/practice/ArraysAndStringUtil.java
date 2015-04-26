package com.practice;

import java.util.Arrays;

public class ArraysAndStringUtil {
	
	public static boolean isPermutation ( String first, String second ) {
		System.out.println("Start1 : " + first);
		System.out.println("Start2 : " + second);
		
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
