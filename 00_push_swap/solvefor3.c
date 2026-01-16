/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solvefor3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 16:58:24 by leodum            #+#    #+#             */
/*   Updated: 2026/01/16 19:31:32 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void solvefor3(struct node *stack_a)
{
	if(stack_a->nbr > stack_a->next->nbr)
	{
		if(stack_a->nbr > stack_a->next->next->nbr)
		{
			return ;
		}
	}
}
