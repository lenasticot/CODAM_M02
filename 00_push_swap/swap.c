/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:54:56 by leodum            #+#    #+#             */
/*   Updated: 2026/01/21 12:48:00 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */



// sa (swap a): Swap the first 2 elements at the top of stack a.
// Do nothing if there is only one element or none.
// sb (swap b): Swap the first 2 elements at the top of stack b.
// Do nothing if there is only one element or none.
// ss : sa and sb at the same time.
#include "push_swap.h"

void sa(struct node **a_tail)
{
	struct node *first;
	struct node *second;
	if(!a_tail || !(*a_tail) || !(*a_tail)->next)
		return ;

	first = *a_tail;
	second = (*a_tail)->next;

	*a_tail = second;
	(*a_tail)->prev = NULL;
	
	first->next = second->next;
	first->prev = second;
	second->next = first;
	
	if(first->next != NULL)
		first->next->prev = first;
	printf("sa\n");
	return ;
}

void sb(struct node **b_tail, struct node **b_head)
{
	struct node *first;
	struct node *second;
	if(!b_tail || !(*b_tail) || !(*b_tail)->next)
		return ;

	first = *b_tail;
	second = (*b_tail)->next;

	*b_tail = second;
	(*b_tail)->prev = NULL;
	
	first->next = second->next;
	first->prev = second;
	second->next = first;
	
	if(first->next != NULL)
		first->next->prev = first;
	else
		*b_head = first;
	printf("sb\n");
	return ;
}

// void ss(struct node **a_tail, struct node **b_tail)
// {
// 	sa(a_tail);
// 	sb(b_tail);
// }
