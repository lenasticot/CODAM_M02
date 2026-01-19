/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solvefor3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 16:58:24 by leodum            #+#    #+#             */
/*   Updated: 2026/01/18 15:55:30 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void solvefor3(struct node **a_head, struct node **a_tail, struct node **b_tail)
{
	if((*a_tail)->nbr > (*a_tail)->next->nbr)
	{
		if((*a_tail)->nbr > (*a_tail)->next->next->nbr)
		{
			ra(a_head, a_tail);
			if((*a_tail)->nbr > (*a_tail)->next->nbr)
				sa(a_tail);
		}
		else
			sa(a_tail);
	}
	else if((*a_tail)->nbr < (*a_tail)->next->nbr)
	{
		if((*a_tail)->nbr < (*a_tail)->next->next->nbr)
		{
			pb(a_tail, b_tail);
			sa(a_tail);
			pa(a_tail, b_tail);
		}
		else
		{
			rra(a_head, a_tail);
		}
	}
}
