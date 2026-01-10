//il y a du travail

// build the linked list

// receive the list, check if correct

// check if already organized

// need to decide which algorithm to use

// probably have to divide by size
// if the list is 
// 3 
// 5
// 100
// 500


// to do
    // pre check
// check if the received information is correct
// check if it is independent numbers or a string
// if string do an atoi to change it
// when you have the right format go through the linked list and check if there is no double number
// if there is return null
// if everything is correct start the organization
    // algorithm
        // 3 numbers
        // 5 numbers
        // 100 numbers
        // 500 numbers


// this function is returning the first node back to the caller
// will probably update it so that it directly remove top most element 
// and place it to stack b directly


#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

typedef struct node
{
    int nbr;
    int pos;
    struct node *prev;  
    struct node *next;
} node;


// struct node *pop(struct **node stack_a)
// {
//     struct node *tmp;
//     int val;
//     tmp = *stack_a;
//     val = tmp->data;
//     *stack_a = (*stack_a)->link;
//     free(tmp);
//     tmp = NULL;
//     return (val);
// }

void free_node(struct node *node)
{
    if(node->prev != NULL)
        node->prev->next = node->next;
    if(node->next != NULL)
        node->next->prev = node->prev;
    free(node);
}
// find a node
// struct node *find_node(struct node *tail, int pos)
// {
//   struct node *curr;
//   curr = tail;
//   while(curr)
//   { 
//     if(curr->pos == pos)
//         return (curr);
//     curr = curr->next;
//   }
//   return (NULL);
  
// }

void *topBottomSwitch(struct node **head, struct node **tail)
{
    struct node *curr;
    curr = *tail;
    while(curr)
    {
        struct node *next = curr->next;
        curr->next = curr->prev;
        curr->prev = next;
        curr = next;
    }
    struct node *tmp = *tail;
    *tail = *head;
    *head = tmp;
}
struct node *find_node_recursive(struct node *node, int pos)
{
    if(node == NULL)
        return (NULL);
    if(node->pos == pos)
        return (node);
    
        return (find_node_recursive(node->next, pos));
}
// adding a node to the end of the double linked list
void *weHaveToGoDeeper(int data, int pos, struct node **head)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if(newNode == NULL)
        return (NULL);
    newNode->nbr = data;
    newNode->pos = pos;
    newNode->prev = *head;
    newNode->next = NULL;
    (*head)->next = newNode;
    *head = newNode;
}

//insert a node at the middle
void middle_child(int data, int pos, struct node *node)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if(newNode == NULL)
        return ;
    newNode->nbr = data;
    newNode->pos = pos;
    newNode->next = node->next;
    newNode->prev = node;
    if(node->next != NULL)
        node->next->prev = newNode;
    node->next = newNode;
    
}
// creating a new node and pushing it on top
void *love_on_top(int data, int pos, struct node **tail)
{
    struct node *newNode;
    newNode = malloc(sizeof(node));
    if (newNode == NULL)
        return (NULL);
    newNode->nbr = data;
    newNode->pos = pos;

    newNode->prev = NULL;
    newNode->next = *tail;
    if(*tail != NULL)
        (*tail)->prev = newNode;
    *tail = newNode;
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

void push_swap()
{
    char *res;
    struct node *tmp;
    int i = 5;
    int j = 0;
    int data;
    
    struct node *tail = NULL;
    struct node *head = NULL;

    init_stack(&tail, &head, i, j);
    i++;
    j++;
 
    // I think i should dereference the different node
    // more than return the data because there is different 
    // data that i am interested of
    while(j < 5)
    { 
    love_on_top(i, j, &tail);
    j++;
    i++;
    }
    weHaveToGoDeeper(i, j, &head);
    middle_child(i, j, tail->next);

    // will have to think of the int pos because
    // when adding new thing it changes
    struct node *lookup = find_node_recursive(tail, 0);
 topBottomSwitch(&head, &tail);
   struct node *curr;
   curr = tail;
   

    while(curr != NULL)
    {
        printf("%i\n", curr->nbr);
        curr = curr->next;
    }
    printf("%d is the %d node at position: %p\n", lookup->nbr, lookup->pos, lookup);
    
    
    //working on the pop function
    // tmp = pop(&stack_a);
    // stack_a = tmp->link;
    // stack_b = push(tmp->data, j +1, stack_b, prev, next)

    // if(*argv <= 1)
    //     return (NULL)
    // if(*argv == 2)
    //     {
    //         ft_split(argv[2]);
    //         res = ft_atoi(argv[2]);
    //     }
    // else if(*argv > 2)
    // {
    //     while(*argv)
    //     { 
    //     tmp = ft_atoi(argv[i]);
    //     // add it to the linked list, but should I have a special one for the first one? 
    //     //Maybe to do before the while loop
    //     i++;
    //     // do I need to free tmp?
    //     }
    // }
}

int main(void)
{
    push_swap();

}