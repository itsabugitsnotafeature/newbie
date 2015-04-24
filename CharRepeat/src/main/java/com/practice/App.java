package com.practice;
import com.practice.UniqueChar;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        
//        assertEquals('b', UniqueChar.firstNonRepeatedCharacter("abcdefghija")); 
//        assertEquals('h', UniqueChar.firstNonRepeatedCharacter("hello")); 
//        assertEquals('J', UniqueChar.firstNonRepeatedCharacter("Java")); 
//        assertEquals('i', UniqueChar.firstNonRepeatedCharacter("simplest"));

        System.out.println( UniqueChar.firstNonRepeatedCharacter("abcdefghija")); 
        System.out.println( UniqueChar.firstNonRepeatedCharacter("hello")); 
        System.out.println( UniqueChar.firstNonRepeatedCharacter("Java")); 
        System.out.println( UniqueChar.firstNonRepeatedCharacter("simplest"));
        
    }
}
