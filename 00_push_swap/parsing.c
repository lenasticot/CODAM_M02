/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parsing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:29:35 by leodum            #+#    #+#             */
/*   Updated: 2026/01/26 22:16:48 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	only_int_allowed(char **str)
{
	int	i;
	int	j;

	i = 1;
	j = 0;
	while (str[i])
	{
		if (str[i][j] == '-' || str[i][j] == '+')
			j++;
		while (str[i][j])
		{
			if (str[i][j] < 48 || str[i][j] > 57)
				return (1);
			j++;
		}
		j = 0;
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
