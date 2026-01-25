/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/25 20:24:49 by marvin            #+#    #+#             */
/*   Updated: 2025/12/25 20:24:49 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
// # include "ft_printf/ft_printf.h"
// # include "libft/libft.h"

typedef struct node
{
    int nbr;
    int pos;
	int ind;
    struct node *prev;  
    struct node *next;
} node;


void	whatnow(int pos, struct node **a_head, struct node **a_tail);
void	init_stack(struct node **tail, struct node **head, int value, int pos);
void	weHaveToGoDeeper(int data, int pos, struct node **head);

int		only_int_allowed(char **str);
int		ft_verif_double(struct node *curr, int nbr, int pos);
int	parse_for_ind(struct node *curr, int nbr);

void	sa(struct node **a_tail);
void	sb(struct node **b_tail,  struct node **b_head);
void	ss(struct node **a_tail, struct node **b_tail);
void	pb(struct node **a_tail, struct node **b_tail, struct node **b_head, struct node **a_head);
void	pa(struct node **a_tail, struct node **b_tail, struct node **a_head, struct node **b_head);
void	ra(struct node **a_head, struct node **a_tail);
void	rb(struct node **b_head, struct node **b_tail);
void	rr(struct node **b_head, struct node **b_tail, struct node **a_head, struct node **a_tail);
void	rra(struct node **a_head, struct node **a_tail);
void	rrb(struct node **b_head, struct node **b_tail);
void	rrr(struct node **b_head, struct node **b_tail, struct node **a_head, struct node **a_tail);

void solvefor3(struct node **a_head, struct node **a_tail, struct node **b_tail, struct node **b_head);
void solvefor5(struct node **a_head, struct node **a_tail, struct node **b_tail, struct node **b_head);


void radixsort(struct node **a_tail, struct node **a_head, struct node **b_tail, struct node **b_head);
int get_max_bits(int size);
int stackSize(struct node *a_tail);

#endif