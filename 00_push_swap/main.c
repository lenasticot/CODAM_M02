/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/28 20:34:43 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void free_stack(struct node **stack)
{
    struct node *current = *stack;
    struct node *next;
    
    while (current != NULL)
    {
        next = current->next;
        free(current);
        current = next;
    }
    *stack = NULL;
}

void	push_swap(int pos, struct node **a_head, struct node **a_tail)
{
	struct node	*b_tail;
	struct node	*b_head;

	b_tail = NULL;
	b_head = NULL;
	if (pos <= 2)
		solvefor2(a_tail, a_head);
	else if (pos == 3)
		solvefor3(a_head, a_tail);
	else if (pos == 4)
		solvefor4(a_head, a_tail, &b_tail, &b_head);
	else if (pos > 3 && pos <= 5)
		solvefor5(a_head, a_tail, &b_tail, &b_head);
	else if (pos > 5)
		radixsort(a_tail, a_head, &b_tail, &b_head);
	if(b_tail != NULL)
		free_stack(&b_tail);
}

int validate_input(int argc, char **argv)
{
	if (argc < 2)
		return (1);
	if (only_int_allowed(argv))
		return (1);
	return (0);
}

void build_stack(struct node **a_tail, struct node **a_head, char **argv)
{
	int i;
	int node;

	i = 1;

	init_stack(a_tail, a_head, atoi(argv[i]), i);
	i++;
	
	while(argv[i])
	{
		node = atoi(argv[i]);
		add_node_below(node, i, a_head);
		i++;
	}
}

int additional_checks(struct node *a_tail)
{
	struct node *curr;

	curr = a_tail;
	while(curr != NULL)
	{
		curr->ind = parse_for_ind(a_tail, curr->nbr);
		if(ft_verif_double(a_tail, curr->nbr, curr->pos) == 0)
			return (1);
		curr = curr->next;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	struct node	*a_tail;
	struct node	*a_head;

	a_tail = NULL;
	a_head = NULL;
	if (validate_input(argc, argv))
		return (1);
	build_stack(&a_tail, &a_head, argv);
	if (additional_checks(a_tail))
	{
		free_stack(&a_tail);
		return (1);
	}
	if (check_for_order(a_tail))
	{
		free_stack(&a_tail);
		return (0);
	}
	push_swap(a_head->pos, &a_head, &a_tail);
	free_stack(&a_tail);
	return (0);
}

