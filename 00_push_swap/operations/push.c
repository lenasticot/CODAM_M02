/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:53:04 by leodum            #+#    #+#             */
/*   Updated: 2026/01/28 20:48:31 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	pb(struct node **a_tail, struct node **b_tail,
	struct node **b_head, struct node **a_head)
{
	struct node	*tmp;

	tmp = *a_tail;
	if (!a_tail || !(*a_tail))
		return ;
	*a_tail = (*a_tail)->next;
	if (*a_tail != NULL)
		(*a_tail)->prev = NULL;
	else
		*a_head = NULL;
	if ((*b_tail) == NULL && (*b_head) == NULL)
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
	write(1, "pb\n", 3);
}

void	pa(struct node **a_tail, struct node **b_tail,
	struct node **a_head, struct node **b_head)
{
	struct node	*tmp;

	tmp = *b_tail;
	if (!b_tail || !(*b_tail))
		return ;
	*b_tail = (*b_tail)->next;
	if (*b_tail != NULL)
		(*b_tail)->prev = NULL;
	else
		*b_head = NULL;
	if ((*a_tail) == NULL && (*a_head) == NULL)
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
	write(1, "pa\n", 3);
}
