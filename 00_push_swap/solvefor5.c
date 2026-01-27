/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solvefor5.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/18 16:20:57 by marvin            #+#    #+#             */
/*   Updated: 2026/01/18 16:20:57 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int find_pos(struct node *a_tail, int ind)
{
	int pos;

	pos = 0;
	while(a_tail)
	{
		if(a_tail->ind == ind)
			return (pos);
		pos++;
		a_tail = a_tail->next;
	}
	return (-1);
}

void	solvefor5(struct node **a_head, struct node **a_tail,
	struct node **b_tail, struct node **b_head)
{
	int pos;
	int size;
	int i;

	i = 0;	
	size = 5;
	while(i < 2)
	{	
		pos = find_pos(*a_tail, i);
		if(pos <= size /2)
		{
			while((*a_tail)->ind != i)
				ra(a_head, a_tail);
			pb(a_tail, b_tail, b_head, a_head);
		}
		else
		{
			while((*a_tail)->ind != i)
				rra(a_head, a_tail);
			pb(a_tail, b_tail, b_head, a_head);
		}
		i++;
		size--;
	}
	solvefor3(a_head, a_tail);
	pa(a_tail, b_tail, a_head, b_head);
	pa(a_tail, b_tail, a_head, b_head);
}
