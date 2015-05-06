package com.practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public class ArraysAndStringUtil {
	
	public static String compressByMe ( String str ) {
//		if ( calculateCompressionSize(str) > str.length())
//			return "";
		
		HashMap<Character, Integer> scoreboard = new HashMap<Character, Integer>();
		StringBuffer output = new StringBuffer();
		
		for ( char letter : str.toCharArray() ) {
			if ( scoreboard.containsKey(letter) ) {
				scoreboard.put(letter, scoreboard.get(letter) + 1 );
			}
			else {
				scoreboard.put(letter, 1 );
			}
		}
		
		for (Entry<Character, Integer> eachEntry : scoreboard.entrySet() ) {
			output.append(eachEntry.getKey());
			output.append(eachEntry.getValue());
		}
		
		return output.toString();
	}
	
	public static String compressByBook ( String str ) {
		if ( calculateCompressionSize(str) > str.length())
			return "";
		
		StringBuffer newStr = new StringBuffer();
		char last = str.charAt(0);
		int count = 1;
		
		for ( int i= 0; i<str.length() ; i++ ) {
			if ( str.charAt(i) == last )
				count++;
			else {
//				newStr.append(String.valueOf(count));
				newStr.append(last);
				newStr.append(count);
				last = str.charAt(i);
				count = 1;
			}
		}
		newStr.append(last);
		newStr.append(count);
		
		return newStr.toString();
	}
	

	private static int calculateCompressionSize(String str) {
		
		if ( str==null || str.isEmpty() )
			return 0;
		
		char last = str.charAt(0);
		int size = 0;
		int count = 1;
		
		for ( int i=1; i<str.length() ; i++) {
			if ( str.charAt(i) == last ) 
				count++;
			else{
				size += 1 + String.valueOf(count).length();
				count = 1;
				last = str.charAt(i);
			}
		}
		size += 1 + String.valueOf(count).length();
		return size;
	}


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
		return false;

	}

	private String sort (String input) { 
		char [] content	= input.toCharArray();
		Arrays.sort(content);
		return new String(content);
	}


	public static String replaceAllWith20Percent ( char[] word, int length ) {
		System.out.print("\n  INPUT : ");
		for (int j = 0 ; j < word.length ; j++ ) {
			System.out.print(" " + word[j] );
		}

		int spaceCount = 0;
		for ( int i=0; i< word.length ; i++ ) {
			if (word[i] == ' ')
				spaceCount++;
		}

		int newLength = length + (spaceCount*2) + 1;
		word[ newLength ] = '\0';

		for (int j = length ; j >= 0 ; j-- ) {

			if (word[j] == ' ' ) {
				word[newLength-1] = '0';
				word[newLength-2] = '2';
				word[newLength-3] = '%';
				newLength = newLength - 3;
			}
			else {
				word[newLength - 1] = word[j];
				newLength = newLength - 1;
			}
		}
		System.out.print("\n OUTPUT : ");
		for (int j = 0 ; j < word.length ; j++ ) {
			System.out.print(" " + word[j] );
		}

		return "";
	}

}
