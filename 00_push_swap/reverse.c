/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:53:16 by leodum            #+#    #+#             */
/*   Updated: 2026/01/18 15:27:23 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// rra (reverse rotate a): Shift down all elements of stack a by 1.
// The last element becomes the first one.
// rrb (reverse rotate b): Shift down all elements of stack b by 1.
// The last element becomes the first one.
// rrr : rra and rrb at the same time
#include "push_swap.h"

void rra(struct node **a_head, struct node **a_tail)
{
	struct node *tmp;

	tmp = *a_head;
	*a_head = (*a_head)->prev;
	(*a_head)->next = NULL;

	(*a_tail)->prev = tmp;
	tmp->prev = NULL;
	tmp->next = *a_tail;
	*a_tail = tmp;

 	return ;
}

void rrb(struct node **b_head, struct node **b_tail)
{
	struct node *tmp;

	tmp = *b_head;
	*b_head = (*b_head)->prev;
	(*b_head)->next = NULL;

	(*b_tail)->prev = tmp;
	tmp->prev = NULL;
	tmp->next = *b_tail;
	*b_tail = tmp;
	return ;
}

void rrr(struct node **b_head, struct node **b_tail, struct node **a_head, struct node **a_tail)
{
	struct node *a_tmp;
	struct node *b_tmp;

	a_tmp = *a_head;
	*a_head = (*a_head)->prev;
	(*a_head)->next = NULL;

	(*a_tail)->prev = a_tmp;
	a_tmp->prev = NULL;
	a_tmp->next = *a_tail;
	*a_tail = a_tmp;

	b_tmp = *b_head;
	*b_head = (*b_head)->prev;
	(*b_head)->next = NULL;

	(*b_tail)->prev = b_tmp;
	b_tmp->prev = NULL;
	b_tmp->next = *b_tail;
	*b_tail = b_tmp;
	return ;
}