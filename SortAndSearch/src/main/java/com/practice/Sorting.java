package com.practice;

import com.sun.org.apache.bcel.internal.generic.SWAP;

public class Sorting {
	
	void mergeSort ( int[] array ) {
		int [] helper = new int[array.length];
		mergeSort(array, helper, 0 , array.length -1 );
	}

	private void mergeSort(int[] array, int[] helper, int low, int high) {
		if ( low < high ) {
			int middle = (low + high) / 2;
			mergeSort(array, helper, low, middle);		// Sort left Half
			mergeSort(array, helper, middle+1, high);	// Sort right Half
			merge(array, helper, low, middle, high);	// Merge them
		}
	}

	private void merge(int[] array, int[] helper, int low, int middle, int high) {

		/*	Copy both halves into a helper array */
		for ( int i=low ; i <=high ; i++ ) {
			helper[i] = array[i];
		}
		
		int helperLeft = low;
		int helperRight = middle + 1 ;
		int current = low;
		
		while ( helperLeft <= middle && helperRight <= high ) {
			
			if (helper[helperLeft] <= helper[helperRight]) {
				array[current] = helper[helperLeft];
				helperLeft++;
			} else {
				array[current] = helper[helperRight];
				helperRight++;
			}
			current++;
		}
		/* Copy rest of the left side of the array into the target array */
		int remaining = middle = helperLeft ; 
		for ( int i = 0 ; i < remaining ; i++) {
			array[current+i] = helper[helperLeft + i];
		}
	}

	void quickSort( int arr[] , int left, int right ) {
		int index = partition(arr, left, right);
		
		if(left < index -1) {
			quickSort(arr, left, index -1 );
		}
		
		if(index < right) {
			quickSort(arr,index,  right);
		}
	}

	private int partition(int[] arr, int left, int right) {
		int pivot = arr[(left + right)/2];
		
		while (left < right) {
			while (arr[left] < pivot) left++ ;
			while (arr[right] > pivot) right++ ;
			
			if(left <= right) {
				swap(arr, left, right);
				left++;
				right++;
			}
		}
		return left;
	}

	private void swap(int[] arr, int left, int right) {
		int temp = arr[left];
		arr[left] = arr[right];
		arr[right] = temp;
	}
	

}
