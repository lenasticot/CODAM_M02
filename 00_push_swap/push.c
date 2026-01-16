// pa (push a): Take the first element at the top of b and put it at the top of a.
// Do nothing if b is empty.
// pb (push b): Take the first element at the top of a and put it at the top of b.
// Do nothing if a is empty

#include "push_swap.h"

void pb(struct node **a_tail, struct node **b_tail)
{
	struct node *tmp = *a_tail;

	*a_tail = (*a_tail)->next;
	if(*a_tail != NULL)
		(*a_tail)->prev = NULL;
	tmp->next = *b_tail;
	tmp->prev = NULL;
	if(*b_tail != NULL)
		(*b_tail)->prev = tmp;
	*b_tail = tmp;
	return ;
}

void pa(struct node **a_tail, struct node **b_tail)
{
	struct node *tmp = *b_tail;
	*b_tail = (*b_tail)->next;
	if(*b_tail != NULL)
		(*b_tail)->prev = NULL;
	tmp->next = *a_tail;
	tmp->prev = NULL;
	if(*a_tail != NULL)
		(*a_tail)->prev = tmp;
	*a_tail = tmp;
	return ;
}