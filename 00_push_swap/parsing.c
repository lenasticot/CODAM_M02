/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:29:35 by leodum            #+#    #+#             */
/*   Updated: 2026/01/29 20:53:54 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"


int is_valid_number(char *str)
{
    int i;
    
    i = 0;

    while (str[i] == ' ' || str[i] == '\t')
        i++;
    if (str[i] == '\0')
        return (0);
    if (str[i] == '+' || str[i] == '-')
        i++;
    if (str[i] < '0' || str[i] > '9')
        return (0);
    while (str[i])
    {
        if (str[i] < '0' || str[i] > '9')
            return (0);
        i++;
    }
    return (1);
}

int only_int_allowed(char **str)
{
    int i;
    
    i = 1;
    while (str[i])
    {
        if (!is_valid_number(str[i]))
            return (1); 
        i++;
    }
    return (0);  
}

int	parse_for_ind(struct node *curr, int nbr)
{
	int	ind;

	ind = 0;
	while (curr)
	{
		if (nbr > curr->nbr)
			ind++;
		curr = curr->next;
	}
	return (ind);
}


int check_for_order(struct node *a_tail)
{
	while(a_tail && a_tail->next)
	{
		if (a_tail->ind > a_tail->next->ind)
			return (0);
		a_tail = a_tail->next;
	}
	return (1);
	
}
int	ft_verif_double(struct node *curr, int nbr, int pos)
{
	int	i;

	i = 1;
	while (i < pos)
	{
		if (curr->nbr == nbr)
			return (0);
		curr = curr->next;
		i++;
	}
	return (1);
}
