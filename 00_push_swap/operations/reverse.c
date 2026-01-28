/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/17 16:53:16 by leodum            #+#    #+#             */
/*   Updated: 2026/01/28 20:48:20 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	rra(struct node **a_head, struct node **a_tail)
{
	struct node	*last;

	if(!*a_head || !(*a_head)->prev)
		return ;

	last = *a_head;
	*a_head = last->prev;
	(*a_head)->next = NULL;
	last->prev = NULL;
	last->next = *a_tail;
	(*a_tail)->prev = last;
	*a_tail = last;
	write(1, "rra\n", 4);
}

// void	rrb(struct node **b_head, struct node **b_tail)
// {
// 	struct node	*tmp;

// 	tmp = *b_head;
// 	*b_head = (*b_head)->prev;
// 	(*b_head)->next = NULL;
// 	(*b_tail)->prev = tmp;
// 	tmp->prev = NULL;
// 	tmp->next = *b_tail;
// 	*b_tail = tmp;
// }
