/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 15:01:02 by leodum            #+#    #+#             */
/*   Updated: 2026/01/17 15:42:46 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void ra(struct node **a_head, struct node **a_tail)
{
	struct node *tmp;
	tmp = *a_tail;

	*a_tail = (*a_tail)->next;
	(*a_tail)->prev = NULL;
	(*a_head)->next = tmp;
	tmp->prev = *a_head;
	tmp->next = NULL;
	*a_head = tmp;
	
	return ;
}
// need to add a check if empty
void rb(struct node **b_head, struct node **b_tail)
{
	struct node *tmp;
	tmp = *b_tail;

	*b_tail = (*b_tail)->next;
	(*b_tail)->prev = NULL;
	(*b_tail)->next = tmp;
	tmp->prev = *b_head;
	tmp->next = NULL;
	*b_head = tmp;
	
	return ;
}

void rr(struct node **b_head, struct node **b_tail, struct node **a_head, struct node **a_tail)
{
	struct node *a_tmp;
	struct node *b_tmp;

	a_tmp = *a_tail;
	b_tmp = *b_tail;
	
	*a_tail = (*a_tail)->next;
	(*a_tail)->prev = NULL;
	(*a_head)->next = a_tmp;
	a_tmp->prev = *a_head;
	a_tmp->next = NULL;
	*a_head = a_tmp;

	*b_tail = (*b_tail)->next;
	(*b_tail)->prev = NULL;
	(*b_tail)->next = b_tmp;
	b_tmp->prev = *b_head;
	b_tmp->next = NULL;
	*b_head = b_tmp;
	return ;
}
