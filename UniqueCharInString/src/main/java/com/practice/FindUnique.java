package com.practice;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

public class FindUnique {
	
	public static boolean findLeastRepeatingCharacter (String word) {
		return false;
	}
	
	/**
	 * Checking if String has unique Characters
	 * only works for lower case string. 
	 * For example : abc, aab, etc
	 * 
	 * @return true : if all unique characters
	 * 			false : at least one repeated character
	 */
	public static boolean isUniqueChars( String word ) {
		
		// short circuit - supposed to imply that
	    // there are no more than 256 different characters.
	    // this is broken, because in Java, char's are Unicode,
	    // and 2-byte values so there are 32768 values
	    // (or so - technically not all 32768 are valid chars)
		if (word.length() > 256) return false;
	
		// checker is used as a bitmap to indicate which characters
	    // have been seen already
		int checker = 0;
		
		for ( int i=0; i<word.length() ; i++) {
			 // set val to be the difference between the char at i and 'a'
	        // unicode 'a' is 97
	        // if you have an upper-case letter e.g. 'A' you will get a
	        // negative 'val' which is illegal
			int asciiVal = word.charAt(i) - 'a';
			
			// if this lowercase letter has been seen before, then
	        // the corresponding bit in checker will have been set and
	        // we can exit immediately.
			if ( ( checker & ( 1 << asciiVal) ) > 0 ) return false ;
			
			// set the bit to indicate we have now seen the letter.
			checker |= (1<<asciiVal) ;
		}
		
		// none of the characters has been seen more than once.
		return true;
		
		
	}


	


	/* Using HashMap to find first non-repeated character from String in Java. 
	Algorithm : 
		Step 1 : Scan String and store count of each character in HashMap 
		Step 2 : traverse String and get count for each character from Map. 
	Since we are going through String from first to last character, 
	when count for any character is 1, we break, it's the first 
	non repeated character. Here order is achieved by going 
	through String again.
	
	Note : Output is the first occurance of NON-repeating (Only occuring Once / Unique) Character 
			NOT THE LEASE REPEATING CHAR.
	 
	*/
	public static char firstNonRepeatedCharacter(String word) {

		/*	
		 * Method #3	
		 * */
		HashMap<Character,Boolean> uniqueness = new HashMap<>();
		char uniqueChar = word.charAt(0);
		int index = 0;
		
		for (char c : word.toCharArray()) {
			++index;
			
			if (uniqueness.containsKey(c)) {
				uniqueness.put(c, true);
				continue;
			}
			
			uniqueChar = c;
			uniqueness.put(c, false);
			for (int  j = index ; j < word.length() ; j++ ) {
				if ( uniqueChar == word.charAt(j)) {
					uniqueness.put(c, true);
				}
			}
			
			if ( uniqueness.containsKey(c) & uniqueness.get(c) == false ) {
				return c;
			}
		}
		throw new RuntimeException("Undefined behaviour");
	}


	/**
	 * @param word
	 * @return
	 */
	public static char firstUniqueCharUsingDoubleFor(String word) {
		/*	
		 * Method #2	
		 * */
		HashMap<Character,Integer> scoreboard = new HashMap<>();
		char uniqueChar = word.charAt(0);
		int lowestScore = 0;

		for (char c : word.toCharArray()) { 
			if (scoreboard.containsKey(c)) {
				scoreboard.put(c, scoreboard.get(c)+1);
			}
			else {
				scoreboard.put(c, 1);
			}
		}

		for (char c : word.toCharArray()) { 
			if (scoreboard.get(c)==1) {
				return c; 
			}
		}
		throw new RuntimeException("Undefined behaviour");
		

		
		/*	
		 * Method #1 :	build table [char -> count]	
		 * */
		
		/*
		HashMap<Character,Integer> scoreboard = new HashMap<>();
		for (int i = 0;i < word.length();i++) { 
			char c = word.charAt(i);
			if (scoreboard.containsKey(c)) 
			{ 
				scoreboard.put(c, scoreboard.get(c) + 1);
			} else { scoreboard.put(c, 1);
			} 
		} 
		// since HashMap doesn't maintain order, going through string again 
		for (int i = 0;i < word.length();i++) { 
			char c = word.charAt(i);
			if (scoreboard.get(c) == 1) { 
				return c;
			} 
		} 
		throw new RuntimeException("Undefined behaviour");
		*/
	}


	/* * Finds first non repeated character in a String in just one pass. 
	 * * It uses two storage to cut down one iteration, 
	 * standard space vs time trade-off. 
	 * * Since we store repeated and non-repeated character separately, 
	 * * at the end of iteration, first element from List is our first non 
	 * * repeated character from String. */ 
	
	public static char firstUniqueCharUsingTwoMaps(String word) { 
		Set<Character> repeatingChars = new HashSet<>();
		List<Character> nonRepeatingChars = new ArrayList<>();
	
		for (int i = 0; i < word.length(); i++) { 
			char letter = word.charAt(i);
			
			if (repeatingChars.contains(letter)) { 
				continue;
			} 
			if (nonRepeatingChars.contains(letter)) { 
				nonRepeatingChars.remove((Character) letter);
				repeatingChars.add(letter);
			} else { 
				nonRepeatingChars.add(letter);
			} 
		} 
		return nonRepeatingChars.get(0);
	}

	/** * Java Program to find first duplicate, non-repeated character in a String. 
	 * * It demonstrate three simple example to do this programming problem. * 
	 * * @author Javarevisited */ 
	
	/* * Using LinkedHashMap to find first non repeated character of String * Algorithm : 
	 * * Step 1: get character array and loop through it to build a 
	 * * hash table with char and their count. 
	 * * Step 2: loop through LinkedHashMap to find an entry with 
	 * * value 1, that's your first non-repeated character, 
	 * * as LinkedHashMap maintains insertion order. */ 
	
	public static char getFirstNonRepeatedChar(String str) {
		Map<Character,Integer> counts = new LinkedHashMap<>(str.length());
	
		for (char c : str.toCharArray()) { 
			counts.put(c, counts.containsKey(c) ? counts.get(c) + 1 : 1);
	
		} 
		for (Entry<Character,Integer> entry : counts.entrySet()) { 
			if (entry.getValue() == 1) { return entry.getKey();
			} 
		} 
		throw new RuntimeException("didn't find any non repeated Character");
	}
}

