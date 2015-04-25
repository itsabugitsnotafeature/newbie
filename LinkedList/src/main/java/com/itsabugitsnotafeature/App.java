package com.itsabugitsnotafeature;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        
//        Primitive data types
        byte	test1 = 0 ; 
        short	test2 = 0 ;
        int		test3 = 0 ;
        long	test4 = 0L ;
        float	test5 = 0.0f ;
        double	test6 = 0.0d ;
        char	test7 = '\u0000' ;
        String 	test8 =   	null ;
        boolean	test9 = false ;
        
        Character 	test10;
        Integer		test12;
        String 		test13;
        
        
        MyLinkedList testList = new MyLinkedList();
        testList.addNode(99);
        testList.addNode(1);
        testList.addNode(2);
        testList.addNode(3);
        testList.addNode(4);
        testList.addNode(5);
        testList.addNode(6);
        
        testList.printLinkedList();
        
    }
}
