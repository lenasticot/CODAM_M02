/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/26 22:25:07 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	whatnow(int pos, struct node **a_head, struct node **a_tail)
{
	struct node	*b_tail;
	struct node	*b_head;

	b_tail = NULL;
	b_head = NULL;
	if (pos <= 3)
		solvefor3(a_head, a_tail, &b_tail, &b_head);
	else if (pos > 3 && pos <= 5)
		solvefor5(a_head, a_tail, &b_tail, &b_head);
	else if (pos > 5)
		radixsort(a_tail, a_head, &b_tail, &b_head);
}

int	main(int argc, char **argv)
{
	int			i;
	int			start;
	int			node;
	struct node	*curr;
	struct node	*a_tail;
	struct node	*a_head;

	a_tail = NULL;
	a_head = NULL;
	i = 1;
	if (argc < 2)
		return (1);
	if (!only_int_allowed(argv))
		return (1);
	start = atoi(argv[i]);
	init_stack(&a_tail, &a_head, start, i);
	i++;
	while (argv[i])
	{
		node = atoi(argv[i]);
		add_node_below(node, i, &a_head);
		i++;
	}
	curr = a_tail;
	while (curr != NULL)
	{
		curr->ind = parse_for_ind(a_tail, curr->nbr);
		if (ft_verif_double(a_tail, curr->nbr, curr->pos) == 0)
			return (1);
		curr = curr->next;
	}
	whatnow(a_head->pos, &a_head, &a_tail);
}
