/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solvefor3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 16:58:24 by leodum            #+#    #+#             */
/*   Updated: 2026/01/17 18:53:10 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void solvefor3(struct node **a_head, struct node **a_tail)
{
	if((*a_tail)->nbr > (*a_tail)->next->nbr)
	{
		
		if((*a_tail)->nbr > (*a_tail)->next->next->nbr)
		{
			ra(a_head, a_tail);
		}
	}
}
