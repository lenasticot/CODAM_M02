# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: leodum <leodum@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/16 15:49:58 by leodum            #+#    #+#              #
#    Updated: 2026/01/17 18:47:57 by leodum           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a

PRINTF_DIR = ft_printf
PRINTF = $(LIBFT_DIR)/libftprintf.a 


SRCS = main.c create_llist.c parsing.c push.c rotate.c reverse.c swap.c solvefor3.c
OBJS = $(SRCS:.c=.o)
HEADER = push_swap.h 

CC = cc
CFLAGS = -Wall -Wextra -Werror

all: $(NAME)

$(LIBFT):
	$(MAKE) -C $(LIBFT_DIR)

$(PRINTF):
	$(MAKE) -C $(PRINTF_DIR)


$(NAME): $(LIBFT) $(PRINTF) $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -L$(LIBFT_DIR) -lft -L$(PRINTF_DIR) -lftprintf -o $(NAME)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)
	$(MAKE) -C $(LIBFT_DIR) clean
	$(MAKE) -C $(PRINTF_DIR) clean

fclean: clean
	rm -f $(NAME)
	$(MAKE) -C $(LIBFT_DIR) clean
	$(MAKE) -C $(PRINTF_DIR) clean

re: fclean all

.PHONY: all clean fclean re