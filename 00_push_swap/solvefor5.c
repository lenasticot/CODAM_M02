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
        pb(a_tail, b_tail, b_head, a_head);
        i++;
    }
    solvefor3(a_head, a_tail, b_tail, b_head);
    printf("solvefor5 :\n");
    if((*b_tail)->nbr < (*b_tail)->next->nbr)
        sb(b_tail, b_head);
    while((*a_tail))
    { 
    if((*a_tail)->nbr > (*b_tail)->nbr)
        pb(a_tail, b_tail, b_head, a_head);
    else if((*a_tail)->nbr < (*b_tail)->nbr)
    {      
        if((*a_tail)->nbr > (*b_tail)->next->nbr)
        {
            pb(a_tail, b_tail, b_head, a_head);
            sb(b_tail, b_head);
        }  
        else
        {
            pb(a_tail, b_tail, b_head, a_head);
            rb(b_head, b_tail);
        }
		// check
	// printf("current a_tail\n");
	// struct node *curr = *a_tail;
	// if(!curr)
	// 	printf("error, stack_a is empty\n");
	// while(curr)
	// 	{
	// 		printf("%i\n", curr->nbr);
	// 		curr = curr->next;
	// 	}
	// free(curr);
	// struct node *bcurr = *b_tail;
	// printf("current b_tail\n");
	// while(bcurr)
	// 	{
	// 		printf("%i\n", bcurr->nbr);
	// 		bcurr = bcurr->next;
	// 	}
	// free(bcurr);
		//end of check
    }
    }

    while((*b_tail))
        pa(a_tail, b_tail, a_head, b_head);
	
printf("current a_tail\n");
	struct node *finalcurr = *a_tail;
	if(!finalcurr)
		printf("error, stack_a is empty\n");
	while(finalcurr)
		{
			printf("%i\n", finalcurr->nbr);
			finalcurr = finalcurr->next;
		}
	free(finalcurr);
    printf("end of solve for 5\n");
}
