/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radixsort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 14:48:58 by leodum            #+#    #+#             */
/*   Updated: 2026/01/23 18:46:13 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	count_digits(int d)
{
	int	i;

	i = 0;
	if (d == 0)
		return (1);
	while (d != 0)
	{
		i++;
		d = d / 10;
	}
	return (i);
}

void countingsort(struct node **a_tail)
{
	// Declare a count array < cntArr[] > of size < max(arr[]) +1 >
	// Traverse input array < arr[] > and map each element of < arr[] > as an index of < cntArr[] >
	// Create an array < ans[] > of size N
	// Traverse array < arr[] > from end and update < ans[cntArr[arr[i]] -1] = arr[i] >
	// Also update cntArr[arr[i]] = cntArr[arr[i]]--

	int *cntArr;
	cntArr = malloc(sizeof(int) * (*a_tail)->pos);
	if(cntArr = NULL)
		return ; 
	struct node *curr = a_tail;
	while(curr)
	{
		
	}
	//start by trying to sort single digit integers
	// should use list to have the whole numbers
	
	//here i solve each number
	free (cntArr);
}

void radixsort(struct node **a_tail, struct node **a_head, struct node *b_tail, struct node **b_head)
{
	// Find te largest element to determines how many times we will iterate
	// Sort the elements based on the unit place digits
	// Repeat x times nb of digits
	
	// need to know how many digits i have
	
	
// 	Step 1: Normalize your numbers (CRITICAL FIRST STEP)
// The problem: You might have negative numbers, or numbers like [42, -17, 1003, 5]
// The solution: Convert them to simple indices (0, 1, 2, 3, etc.) based on their rank
// What to do:

// Before sorting, figure out which number is smallest, 2nd smallest, 3rd smallest, etc.
// Replace each number with its "index" (smallest = 0, next = 1, etc.)
// Now you're sorting [0, 1, 2, 3, 4] instead of weird numbers

// Why this matters: Radix works on bits. 42 in binary is different from index 2. You need consistent, small indices.
// Store this: Either update nbr in your nodes, or add a new field like index to your struct


	
}