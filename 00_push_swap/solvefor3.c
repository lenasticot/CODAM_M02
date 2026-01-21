/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solvefor3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 16:58:24 by leodum            #+#    #+#             */
/*   Updated: 2026/01/21 18:50:53 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void solvefor3(struct node **a_head, struct node **a_tail, struct node **b_tail, struct node **b_head)
{
	printf("solve for 3:\n");
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
			pb(a_tail, b_tail, b_head, a_head);
			sa(a_tail);
			pa(a_tail, b_tail, a_head);
		}
		else
		{
			rra(a_head, a_tail);
		}
	}
	printf("end of solve for 3\n");
}
