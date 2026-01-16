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
# include "ft_printf/ft_printf.h"
# include "libft/libft.h"

typedef struct node
{
    int nbr;
    int pos;
    struct node *prev;  
    struct node *next;
} node;


// void	whatnow(int pos, struct node **stack_a);
void	weHaveToGoDeeper(int data, int pos, struct node **head);
void	init_stack(struct node **tail, struct node **head, int value, int pos);
int		only_int_allowed(char **str);
int		ft_verif_double(struct node *curr, int nbr, int pos);

#endif 