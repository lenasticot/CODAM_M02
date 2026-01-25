/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radixsort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 14:48:58 by leodum            #+#    #+#             */
/*   Updated: 2026/01/25 19:40:28 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int stackSize(struct node *a_tail)
{
	int i = 0;
	while(a_tail)
	{
		i++;
		a_tail = a_tail->next;
	}
	return (i);
}

int get_max_bits(int size)
{
	int i = 0;

	while(size > 0)
	{
		size = size / 2;
		i++;
	}
	return (i);
}
void radixsort(struct node **a_tail, struct node **a_head, struct node **b_tail, struct node **b_head)
{
	int max = get_max_bits((*a_head)->pos -1);
	int bit = 0;
	int stack_size;
	int i = 0;
	
	while(bit < max)
	{
		stack_size = stackSize(*a_tail);
		i = 0;
		while(i < stack_size)
		{
			if(((*a_tail)->ind >> bit )& 1)
				ra(a_head, a_tail);
			else
				pb(a_tail, b_tail, b_head, a_head);
			i++;
		}
		bit++;
	}
	// Problem here when passing the loop does not stop
	while(b_tail)
		pa(a_tail, b_tail, a_head, b_head);

	while(a_tail)
	{
		printf("%i", (*a_tail)->nbr);
		a_tail = (*a_tail)->next;
	}
}
