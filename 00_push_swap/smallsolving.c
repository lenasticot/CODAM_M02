/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   smallsolving.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 16:58:24 by leodum            #+#    #+#             */
/*   Updated: 2026/01/30 08:58:47 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	solvefor2(struct node **a_tail, struct node **a_head)
{
	if ((*a_tail)->ind == 0)
		return ;
	else
		ra(a_head, a_tail);
}

void	solvefor3(struct node **a_head, struct node **a_tail)
{
	int	first;
	int	second;
	int	third;

	first = (*a_tail)->ind;
	second = (*a_tail)->next->ind;
	third = (*a_tail)->next->next->ind;
	if (first > second && first > third)
	{
		ra(a_head, a_tail);
		if ((*a_tail)->ind > (*a_tail)->next->ind)
			sa(a_tail);
	}
	else if (second > first && second > third)
	{
		rra(a_head, a_tail);
		if ((*a_tail)->ind > (*a_tail)->next->ind)
			sa(a_tail);
	}
	else if (first > second)
		sa(a_tail);
}

int	find_pos(struct node *a_tail, int ind)
{
	int	pos;

	pos = 0;
	while (a_tail)
	{
		if (a_tail->ind == ind)
			return (pos);
		pos++;
		a_tail = a_tail->next;
	}
	return (-1);
}

void	solvefor4(struct node **a_head, struct node **a_tail,
struct node **b_tail, struct node **b_head)
{
	int	pos;
	int	size;

	pos = find_pos(*a_tail, 0);
	size = 4;
	if (pos <= size / 2)
		while ((*a_tail)->ind != 0)
			ra(a_head, a_tail);
	else
		while ((*a_tail)->ind != 0)
			rra(a_head, a_tail);
	pb(a_tail, b_tail, b_head, a_head);
	solvefor3(a_head, a_tail);
	pa(a_tail, b_tail, a_head, b_head);
}

void	solvefor5(struct node **a_head, struct node **a_tail,
	struct node **b_tail, struct node **b_head)
{
	int	pos;
	int	i;
	int	size;

	i = 0;
	size = (*a_head)->pos;
	while (i < 2)
	{
		pos = find_pos(*a_tail, i);
		if (pos <= size / 2)
			while ((*a_tail)->ind != i)
				ra(a_head, a_tail);
		else
			while ((*a_tail)->ind != i)
				rra(a_head, a_tail);
		pb(a_tail, b_tail, b_head, a_head);
		size--;
		i++;
	}
	solvefor3(a_head, a_tail);
	pa(a_tail, b_tail, a_head, b_head);
	pa(a_tail, b_tail, a_head, b_head);
}
