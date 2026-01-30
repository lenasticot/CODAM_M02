/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_llist.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:29:20 by leodum            #+#    #+#             */
/*   Updated: 2026/01/30 09:02:02 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int	ft_atol(char *nptr, int *res)
{
	int		i;
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

void	build_stack(struct node **a_tail, struct node **a_head, char **argv)
{
	int	i;
	int	node;
	int	start;

	i = 1;
	if (!ft_atol(argv[i], &start))
	{
		print_error();
		return ;
	}
	init_stack(a_tail, a_head, start, i);
	i++;
	while (argv[i])
	{
		if (!ft_atol(argv[i], &node))
		{
			free_stack(a_tail);
			print_error();
			return ;
		}
		add_node_below(node, i, a_head);
		i++;
	}
}

void	add_node_below(int data, int pos, struct node **head)
{
	struct node	*new_node;

	new_node = malloc(sizeof(t_node));
	if (new_node == NULL)
		return ;
	new_node->nbr = data;
	new_node->pos = pos;
	new_node->prev = *head;
	new_node->next = NULL;
	(*head)->next = new_node;
	*head = new_node;
}

void	init_stack(struct node **tail, struct node **head, int value, int pos)
{
	struct node	*new_node;

	new_node = malloc(sizeof(t_node));
	if (new_node == NULL)
		return ;
	new_node->nbr = value;
	new_node->pos = pos;
	new_node->prev = NULL;
	new_node->next = NULL;
	*tail = new_node;
	*head = new_node;
}
