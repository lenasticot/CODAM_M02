/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   radixsort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/22 14:48:58 by leodum            #+#    #+#             */
/*   Updated: 2026/01/26 22:35:30 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	stack_size(struct node *a_tail)
{
	int	i;

	i = 0;
	while (a_tail)
	{
		i++;
		a_tail = a_tail->next;
	}
	return (i);
}

int	get_max_bits(int size)
{
	int	i;

	i = 0;
	while (size > 0)
	{
		size = size / 2;
		i++;
	}
	return (i);
}

void	radixsort(struct node **a_tail, struct node **a_head,
	struct node **b_tail, struct node **b_head)
{
	int	max;
	int	bit;
	int	size;
	int	i;

	max = get_max_bits((*a_head)->pos -1);
	bit = 0;
	while (bit < max)
	{
		size = stack_size(*a_tail);
		i = 0;
		while (i < size)
		{
			if (((*a_tail)->ind >> bit) & 1)
				ra(a_head, a_tail);
			else
				pb(a_tail, b_tail, b_head, a_head);
			i++;
		}
		while (*b_tail)
		{
			pa(a_tail, b_tail, a_head, b_head);
		}
		bit++;
	}
}
