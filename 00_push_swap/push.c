/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:53:04 by leodum            #+#    #+#             */
/*   Updated: 2026/01/19 21:21:39 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// pa (push a): Take the first element at the top of b and put it at the top of a.
// Do nothing if b is empty.
// pb (push b): Take the first element at the top of a and put it at the top of b.
// Do nothing if a is empty.
 
void pb(struct node **a_tail, struct node **b_tail)
{
	struct node *tmp = *a_tail;
	if(!a_tail || !(*a_tail))
		return ;

	*a_tail = (*a_tail)->next; 
	if(*a_tail != NULL)
		(*a_tail)->prev = NULL;
	tmp->next = *b_tail;
	tmp->prev = NULL;
	if(*b_tail != NULL)
		(*b_tail)->prev = tmp;
	*b_tail = tmp;
	printf("pb\n");
	return ;
}

void pa(struct node **a_tail, struct node **b_tail)
{
	if(!b_tail || !(*b_tail))
		return ;
	struct node *tmp = *b_tail;
	*b_tail = (*b_tail)->next;
	if(*b_tail != NULL)
		(*b_tail)->prev = NULL;
	tmp->next = *a_tail;
	tmp->prev = NULL;
	if(*a_tail != NULL)
		(*a_tail)->prev = tmp;
	*a_tail = tmp;
	printf("pa\n");
	return ;
}