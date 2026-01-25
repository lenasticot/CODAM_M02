/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:53:04 by leodum            #+#    #+#             */
/*   Updated: 2026/01/25 19:32:26 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// pa (push a): Take the first element at the top of b and put it at the top of a.
// Do nothing if b is empty.
// pb (push b): Take the first element at the top of a and put it at the top of b.
// Do nothing if a is empty.
 
void pb(struct node **a_tail, struct node **b_tail, struct node **b_head, struct node **a_head)
{
	if(!a_tail || !(*a_tail))
		return ;
	struct node *tmp = *a_tail;
	*a_tail = (*a_tail)->next; 
	if(*a_tail != NULL)
		(*a_tail)->prev = NULL;
	else
		*a_head = NULL;
	// hope its this
	if((*b_tail) == NULL && (*b_head) == NULL)
	{
		*b_tail = tmp;
		*b_head = tmp;
		tmp->next = NULL;
		tmp->prev = NULL;
	}
	else
	{
		tmp->next = *b_tail;
		tmp->prev = NULL;
		(*b_tail)->prev = tmp;
		*b_tail = tmp;
	}
	printf("pb\n");
	return ;
}

void pa(struct node **a_tail, struct node **b_tail, struct node **a_head, struct node **b_head)
{
	if(!b_tail || !(*b_tail))
		return ;
	struct node *tmp = *b_tail;
	*b_tail = (*b_tail)->next;
	if(*b_tail != NULL)
		(*b_tail)->prev = NULL;
	else
		*b_head = NULL;	
	if((*a_tail) == NULL && (*a_head) == NULL)
	{
		*a_tail = tmp;
		*a_head = tmp;
		tmp->next = NULL;
		tmp->prev = NULL;
	}
	else
	{
		tmp->next = *a_tail;
		tmp->prev = NULL;
		(*a_tail)->prev = tmp;
		*a_tail = tmp;
	}
	printf("pa\n");
	return ;
}