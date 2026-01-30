/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_check.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 08:14:30 by marvin            #+#    #+#             */
/*   Updated: 2026/01/30 08:14:30 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int	print_error(void)
{
	write(2, "Error\n", 6);
	return (1);
}

void	free_stack(struct node **stack)
{
	struct node	*curr;
	struct node	*next;

	curr = *stack;
	while (curr != NULL)
	{
		next = curr->next;
		free(curr);
		curr = next;
	}
	*stack = NULL;
}

int	additional_checks(struct node *a_tail)
{
	struct node	*curr;	

	curr = a_tail;
	while (curr != NULL)
	{
		curr->ind = parse_for_ind(a_tail, curr->nbr);
		if (ft_verif_double(a_tail, curr->nbr, curr->pos) == 0)
			return (1);
		curr = curr->next;
	}
	return (0);
}
