/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_llist.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: leodum <leodum@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:29:20 by leodum            #+#    #+#             */
/*   Updated: 2026/01/16 19:32:02 by leodum           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void add_on_top(int data, int pos, struct node **tail)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if (newNode == NULL)
        return ;
    newNode->nbr = data;
    newNode->pos = pos;

    newNode->prev = NULL;
    newNode->next = *tail;
    if(*tail != NULL)
        (*tail)->prev = newNode;
    *tail = newNode;
}

void weHaveToGoDeeper(int data, int pos, struct node **head)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if(newNode == NULL)
        return ;
    newNode->nbr = data;
    newNode->pos = pos;
    newNode->prev = *head;
    newNode->next = NULL;
    (*head)->next = newNode;
    *head = newNode;
}

void init_stack(struct node **tail, struct node **head, int value, int pos)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if (newNode == NULL)
        return;
    newNode->nbr = value;
    newNode-> pos = pos;
    newNode->prev = NULL;
    newNode->next = NULL;

    *tail = newNode;
    *head = newNode;
}