/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:54:56 by leodum            #+#    #+#             */
/*   Updated: 2026/01/26 22:47:10 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(struct node **a_tail)
{
	struct node	*first;
	struct node	*second;

	if (!a_tail || !(*a_tail) || !(*a_tail)->next)
		return ;
	first = *a_tail;
	second = (*a_tail)->next;
	*a_tail = second;
	(*a_tail)->prev = NULL;
	first->next = second->next;
	first->prev = second;
	second->next = first;
	if (first->next != NULL)
		first->next->prev = first;
	printf("sa\n");
}

void	sb(struct node **b_tail, struct node **b_head)
{
	struct node	*first;
	struct node	*second;

	if (!b_tail || !(*b_tail) || !(*b_tail)->next)
		return ;
	first = *b_tail;
	second = (*b_tail)->next;
	*b_tail = second;
	(*b_tail)->prev = NULL;
	first->next = second->next;
	first->prev = second;
	second->next = first;
	if (first->next != NULL)
		first->next->prev = first;
	else
		*b_head = first;
	printf("sb\n");
}
