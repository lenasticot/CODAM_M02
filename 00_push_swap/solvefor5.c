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

void solvefor5(struct node **a_head, struct node **a_tail, struct node **b_tail, struct node **b_head)
{
    int i;
    i = 1;
    while(i <= 2)
    {
        pb(a_tail, b_tail);
        i++;
    }
    solvefor3(a_head, a_tail, b_tail);
    if((*a_tail)->nbr > (*a_tail)->next->nbr)
        sa(a_tail);
    while(!*b_tail)
    { 
    if((*b_tail)->nbr > (*a_tail)->nbr)
    {
        pb(a_tail, b_tail);
        rb(b_head, b_tail);
    }
    else if((*b_tail)->nbr < (*a_tail)->nbr)
        pa(a_tail, b_tail);
    }

}
