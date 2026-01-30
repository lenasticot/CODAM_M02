/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 15:01:02 by leodum            #+#    #+#             */
/*   Updated: 2026/01/30 09:00:33 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ra(struct node **a_head, struct node **a_tail)
{
	struct node	*tmp;

	tmp = *a_tail;
	if (!a_tail || !(*a_tail) || !(*a_tail)->next)
		return ;
	*a_tail = (*a_tail)->next;
	(*a_tail)->prev = NULL;
	(*a_head)->next = tmp;
	tmp->prev = *a_head;
	tmp->next = NULL;
	*a_head = tmp;
	write(1, "ra\n", 3);
}

void	rb(struct node **b_head, struct node **b_tail)
{
	struct node	*tmp;

	if (!b_tail || !(*b_tail) || !(*b_tail)->next)
		return ;
	tmp = *b_tail;
	*b_tail = (*b_tail)->next;
	(*b_tail)->prev = NULL;
	(*b_head)->next = tmp;
	tmp->prev = *b_head;
	tmp->next = NULL;
	*b_head = tmp;
	write(1, "rb\n", 3);
}
