/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:32:51 by leodum            #+#    #+#             */
/*   Updated: 2026/01/29 21:08:24 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"


int	print_error(void)
{
	write(2, "Error\n", 6);
	return (1);
}

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

int	ft_atol(char *nptr, int *res)
{
	int	i;
	long	result;
	long	sign;

	result = 0;
	i = 0;
	sign = 1;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '+' || nptr[i] == '-')
	{
		if (nptr[i] == '-')
			sign = -1;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		result = result * 10 + (nptr[i] - '0');
		i++;
	}
	result = result * sign;
	if (result > 2147483647 || result < -2147483648)
        return (0); 
	*res = (int)result;
	return (1);
}

void build_stack(struct node **a_tail, struct node **a_head, char **argv)
{
	int i;
	int node;
	int start;

	i = 1;
	if(!ft_atol(argv[i], &start))
	{
		print_error();
		return ;
	}
	init_stack(a_tail, a_head, start, i);
	i++;
	
	while(argv[i])
	{
		if(!ft_atol(argv[i], &node))
		{
			free_stack(a_tail);
			print_error();
			return ;
		}
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

