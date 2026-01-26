/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_llist.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:29:20 by leodum            #+#    #+#             */
/*   Updated: 2026/01/26 22:19:51 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	add_node_below(int data, int pos, struct node **head)
{
	struct node	*new_node;

	new_node = malloc(sizeof(node));
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

	new_node = malloc(sizeof(node));
	if (new_node == NULL)
		return ;
	new_node->nbr = value;
	new_node->pos = pos;
	new_node->prev = NULL;
	new_node->next = NULL;
	*tail = new_node;
	*head = new_node;
}
