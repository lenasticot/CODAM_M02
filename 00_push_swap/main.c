/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/30 08:30:59 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

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
	if (b_tail != NULL)
		free_stack(&b_tail);
}

int	main(int argc, char **argv)
{
	struct node	*a_tail;
	struct node	*a_head;

	a_tail = NULL;
	a_head = NULL;
	if (argc < 2)
		return (0);
	if (only_int_allowed(argv))
		return (print_error());
	build_stack(&a_tail, &a_head, argv);
	if (additional_checks(a_tail))
	{
		free_stack(&a_tail);
		return (print_error());
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
