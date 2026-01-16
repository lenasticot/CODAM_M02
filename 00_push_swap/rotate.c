// ra (rotate a): Shift up all elements of stack a by 1.
// The first element becomes the last one.
// rb (rotate b): Shift up all elements of stack b by 1.
// The first element becomes the last one.
// rr : ra and rb at the same time.


// need to see how to send head and tail from each stack
// to be careful on what to send each time

#include "push_swap.h"

void ra(struct node **a_head, struct node **a_tail)
{
	struct node *curr;
    curr = *a_tail;
    while(curr)
    {
        struct node *next = curr->next;
        curr->next = curr->prev;
        curr->prev = next;
        curr = next;
    }
    struct node *tmp = *a_tail;
    *a_tail = *a_head;
    *a_head = tmp;
	return ;
}
// need to add a check if empty
void rb(struct node **b_head, struct node **b_tail)
{
	struct node *curr;
    curr = *b_tail;
    while(curr)
    {
        struct node *next = curr->next;
        curr->next = curr->prev;
        curr->prev = next;
        curr = next;
    }
    struct node *tmp = *b_tail;
    *b_tail = *b_head;
    *b_head = tmp;
	return ;
}