/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 15:35:36 by leodum            #+#    #+#             */
/*   Updated: 2026/01/14 19:36:43 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	free_all(char **result, int i)
{
	while (i >= 0)
	{
		free(result[i]);
		i--;
	}
	free (result);
}

int	isitdelim(char s, char delim)
{
	return (s == delim);
}

char	*put_words(const char *str, char delim)
{
	int		len;
	char	*word;
	int		i;

	len = 0;
	i = 0;
	while (str[len] && !isitdelim(str[len], delim))
		len++;
	word = malloc(sizeof(char) * (len + 1));
	while (i != len)
	{
		word[i] = str[i];
		i++;
	}
	word[len] = '\0';
	return (word);
}

int	count_words(const char *str, char delim)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] && isitdelim(str[i], delim))
			i++;
		if (str[i])
		{
			count++;
			while (str[i] && !isitdelim(str[i], delim))
				i++;
		}
	}
	return (count);
}

char	**ft_split(const char *s, char c)
{
	char	**result;
	int		i;

	i = 0;
	if (s == NULL)
		return (NULL);
	result = (char **)malloc(sizeof(char *) * (count_words(s, c) + 1));
	if (result == NULL)
		return (NULL);
	while (*s)
	{
		while (*s && isitdelim(*s, c))
			s++;
		if (*s)
		{
			result[i] = put_words(s, c);
			if (result[i] == NULL)
				return (free_all(result, i - 1), NULL);
			i++;
			while (*s && isitdelim(*s, c) == 0)
				s++;
		}
	}
	result[i] = NULL;
	return (result);
}
