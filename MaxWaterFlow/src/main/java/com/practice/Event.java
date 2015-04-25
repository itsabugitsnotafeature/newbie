package com.practice;

import java.util.HashMap;
import java.util.PriorityQueue;

import com.sun.xml.internal.fastinfoset.util.StringArray;

public class Event {

	int startTime, endTime, rate;


	public static int getMaxFlow(Event[] events)	{
		PriorityQueue<Event> heap1 = new PriorityQueue<Event>(events.length);
		PriorityQueue<Event> heap2 = new PriorityQueue<Event>(events.length);
		
		for(Event event : events){
			heap1.add(event);
		}

		int bestFlowRate = Integer.MIN_VALUE;
		int totalFlowRate = 0;
		
		while(!heap1.isEmpty()){
			int earliest = heap1.peek().startTime;
			if(!heap2.isEmpty() && heap2.peek().endTime < earliest){
				earliest = heap2.peek().endTime;
			}
			while(!heap1.isEmpty() && heap1.peek().startTime == earliest){
				Event event = heap1.poll();
				totalFlowRate += event.rate;
				heap2.add(event);
			}
			while(!heap2.isEmpty() && heap2.peek().endTime == earliest){
				Event event = heap2.poll();
				totalFlowRate -= event.rate;
			}
			if(totalFlowRate > bestFlowRate){
				bestFlowRate = totalFlowRate;
			}
		}
		return bestFlowRate;
	}
	
	public HashMap<Integer, String> buildMap (String[] passedStringArray) {
		
		HashMap<Integer, String> constructedMap = new HashMap<Integer, String>();
		int index = 0;
		for ( String eachString : passedStringArray ) {
			constructedMap.put(index++, eachString);
		}
		return constructedMap;
	}
		
		
	private String joinWordsToString ( String[] passedStringArray ) {
		StringBuffer sentence = new StringBuffer();
		
		for (String eachWord : passedStringArray )
			sentence.append(eachWord);

		return sentence.toString();
	}
		
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
