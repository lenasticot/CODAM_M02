/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/23 19:04:50 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
// only did 1 star because i just wanna check a_tail but not modify it
int parseForInd(struct node **a_tail)
{
	int i; 
	struct node *curr; 
	while(a_tail)
	{
		curr = a_tail;
		while (curr)
		{
			i = 1;
			if(curr->nbr > curr->next->nbr)
				i++;
				curr = curr->next;
		}
		(*a_tail)->ind = i;
		*a_tail = (*a_tail)->next;
	}
}
void whatnow(int pos, struct node **a_head, struct node **a_tail)
{
	struct node *b_tail = NULL;
	 struct node *b_head = NULL;
	
	if(pos <= 3)
	{	
		printf("Before solving:\n");
		struct node *before = *a_tail;
		while(before)
		{
			printf("%i\n", before->nbr);
			before = before->next;
		}
		solvefor3(a_head, a_tail, &b_tail, &b_head);
		printf("After solving:\n");
	struct node *after = *a_tail;
		while(after)
		{
			printf("%i\n", after->nbr);
			after = after->next;
		}
		
	}
	else if(pos > 3 && pos <= 5)
	{
		printf("Before solving:\n");
	struct node *before = *a_tail;
		while(before)
		{
			printf("%i\n", before->nbr);
			before = before->next;
		}

		solvefor5(a_head, a_tail, &b_tail, &b_head);
		printf("After solving:\n");
	struct node *after = *a_tail;
		while(after)
		{
			printf("%i\n", after->nbr);
			after = after->next;
		}
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
