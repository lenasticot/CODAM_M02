/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radixsort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 14:48:58 by leodum            #+#    #+#             */
/*   Updated: 2026/01/25 22:10:46 by marvin           ###   ########.fr       */
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
		printf("\n========== BIT POSITION %d ==========\n", bit);
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
		printf("Après séparation:\n");
        printf("Stack A indices: ");
		     struct node *tmp_a = *a_tail;
		   while(tmp_a)
        {
            printf("%d ", tmp_a->ind);
            tmp_a = tmp_a->next;
        }
        printf("\n");
		printf("Stack B indices: ");
        struct node *tmp_b = *b_tail;
        while(tmp_b)
        {
            printf("%d ", tmp_b->ind);
            tmp_b = tmp_b->next;
        }
        printf("\n");
	
		while(*b_tail)
		pa(a_tail, b_tail, a_head, b_head);
		 
        printf("Après avoir tout ramené:\n");
        printf("Stack A indices: ");
	struct node *curr = *a_tail;
	while(curr)
	{
		printf("%i ", curr->ind);
		curr = curr->next;
	}
		bit++;
	}
}
