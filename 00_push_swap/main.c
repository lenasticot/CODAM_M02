#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    int nbr;
    int pos;
    struct node *prev;  
    struct node *next;
} node;

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

int	ft_atoi(const char *nptr)
{
	int	i;
	int	result;
	int	sign;

	result = 0;
	i = 0;
	sign = 1;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '+' || nptr[i] == '-')
	{
		if (nptr[i] == '-')
			sign *= -1;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		result = result * 10 + (nptr[i] - '0');
		i++;
	}
	return (result * sign);
}
int only_int_allowed(char **str)
{
	int i;
	int j;

	i = 1;
	j = 0;
	while(str[i])
	{
		if(str[i] && str[i][j] >= 0 && str[i][j] <= 9)		
			j++;
		else if(str[i] && str[i][j] < 0 && str[i][j] > 9)
			return (1);

		i++;
	}
	return (0);
}
int main(int argc, char **argv)
{
	int i = 1;

	struct node *stack_a;
	struct node *tail = NULL;
	struct node *head = NULL;
	// so i have to put the result of split somewhere
	if(argc > 2)
		ft_split(**argv);
	int check = only_int_allowed(**argv);
	if(check == 1)
		return ("error");

	init_stack(&tail, &head, argv[i], i);
	i++;
	while(argv[i])
	{
		weHaveToGoDeeper(argv[i], i, &head);
		i++;
	}
	struct node *curr;
	curr = tail;
	while(curr != NULL)
	{
		printf("%i\n", curr->nbr);
		curr = curr->next;
	}
	

}

// if(argc == 2)
	// {
	// 	// act as 1 string and regular split to check the arguments one by one
	// }
	// else if(argc > 2)
	// {
	// 	// array of strings so no need to split and can go directly to the rest of the checks
	// }
	// // if there is less than 2 arguments
	// else
	// 	return("error");
	// // so i have to create the stack here then send it to my push swap function
    // push_swap();