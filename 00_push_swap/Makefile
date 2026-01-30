# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 15:49:58 by leodum            #+#    #+#              #
#    Updated: 2026/01/30 09:06:33 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

SRCS = main.c create_list/create_llist.c create_list/parsing.c operations/push.c operations/rotate.c operations/reverse.c operations/swap.c smallsolving.c radixsort.c create_list/error_check.c
OBJS = $(SRCS:.c=.o)
HEADER = push_swap.h 

CC = cc
CFLAGS = -Wall -Wextra -Werror -g
INCLUDES = -I.

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re