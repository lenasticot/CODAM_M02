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

typedef struct node
{
	int			nbr;
	int			pos;
	int			ind;
	struct node	*prev;
	struct node	*next;
}	t_node;

int		ft_atol(char *nptr, int *res);
void	build_stack(struct node **a_tail, struct node **a_head, char **argv);
void	push_swap(int pos, struct node **a_head, struct node **a_tail);
void	init_stack(struct node **tail, struct node **head, int value, int pos);
void	add_node_below(int data, int pos, struct node **head);

int		only_int_allowed(char **str);
int		ft_verif_double(struct node *curr, int nbr, int pos);
int		parse_for_ind(struct node *curr, int nbr);
int		check_for_order(struct node *a_tail);

int		print_error(void);
void	free_stack(struct node **stack);
int		additional_checks(struct node *a_tail);

void	sa(struct node **a_tail, struct node **a_head);
void	sb(struct node **b_tail, struct node **b_head);
void	pb(struct node **a_tail, struct node **b_tail,
			struct node **b_head, struct node **a_head);
void	pa(struct node **a_tail, struct node **b_tail,
			struct node **a_head, struct node **b_head);
void	ra(struct node **a_head, struct node **a_tail);
void	rb(struct node **b_head, struct node **b_tail);
void	rra(struct node **a_head, struct node **a_tail);

void	solvefor2(struct node **a_tail, struct node **a_head);
void	solvefor3(struct node **a_head, struct node **a_tail);
void	solvefor4(struct node **a_head, struct node **a_tail,
			struct node **b_tail, struct node **b_head);
void	solvefor5(struct node **a_head, struct node **a_tail,
			struct node **b_tail, struct node **b_head);
int		find_pos(struct node *a_tail, int ind);
void	radixsort(struct node **a_tail, struct node **a_head,
			struct node **b_tail, struct node **b_head);
int		get_max_bits(int size);
int		stack_size(struct node *a_tail);

#endif