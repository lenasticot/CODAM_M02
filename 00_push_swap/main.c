/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/19 13:20:37 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"


void whatnow(int pos, struct node **a_head, struct node **a_tail)
{
	struct node *b_tail = NULL;
	struct node *b_head = NULL;
	// i need to initialize the b_stack within each situation
	// because i dont have the info rn
	
	if(pos <= 3)
	{	
		printf("Before solving:\n");
		// printf("%i\n", (*a_tail)->nbr);
		// printf("%i\n", (*a_tail)->next->nbr);
		// printf("%i\n", (*a_tail)->next->next->nbr);
		// solvefor3(a_head, a_tail, &b_tail);
		// printf("After solving:\n");
		// printf("%i\n", (*a_tail)->nbr);
		// printf("%i\n", (*a_tail)->next->nbr);
		// printf("%i\n", (*a_tail)->next->next->nbr);

		
	}
	else if(pos > 3 && pos <= 5)
	{
		printf("Before solving:\n");
		printf("%i\n", (*a_tail)->nbr);
		printf("%i\n", (*a_tail)->next->nbr);
		printf("%i\n", (*a_tail)->next->next->nbr);
		printf("%i\n", (*a_tail)->next->next->next->nbr);
		printf("%i\n", (*a_tail)->next->next->next->next->nbr);
		solvefor5(a_head, a_tail, &b_tail, &b_head);
		printf("After solving:\n");
		printf("%i\n", (*a_tail)->nbr);
		printf("%i\n", (*a_tail)->next->nbr);
		printf("%i\n", (*a_tail)->next->next->nbr);
		printf("%i\n", (*a_tail)->next->next->next->nbr);
		printf("%i\n", (*a_tail)->next->next->next->next->nbr);
	
	}
	else if(pos > 5 && pos <= 100)
	{
		printf("100");
		// solvefor100(stack_a);
	}
	else if(pos > 100)
	{
		printf("500");
		// solvefor500(stack_a);
	}
}

int main(int argc, char **argv)
{
	int i = 1;
	struct node *a_tail = NULL;
	struct node *a_head = NULL;
	//will have to check more error
		// if the string is empty
		// does that count as an error if the string start with a space?
		// to check if the numbers are al
	if(argc < 2)
		return(1);
	int check = only_int_allowed(argv);
	if(check == 1)
		return (1);
	int start = atoi(argv[i]);
	// create the stack
	init_stack(&a_tail, &a_head, start, i);
	i++;
	int node;
	while(argv[i])
	{
		node = atoi(argv[i]);
		weHaveToGoDeeper(node, i, &a_head);
		i++;
	}
	// check for double verification
	// might put it into a helper function
	struct node *curr;
	curr = a_tail;
	while(curr != NULL)
	{
		if(ft_verif_double(a_tail, curr->nbr, curr->pos) == 0)
			return (1);
		curr = curr->next;
	}
	whatnow(a_head->pos, &a_head, &a_tail);
	return (0);
}
