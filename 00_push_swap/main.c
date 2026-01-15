#include <stdlib.h>
#include <stdio.h>

char **ft_split(const char *s, char c);

typedef struct node
{
    int nbr;
    int pos;
    struct node *prev;  
    struct node *next;
} node;

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
		if(str[i][j] == '-' || str[i][j] == '+')
			j++;
		while(str[i][j])
		{ 
		if(str[i][j] < 48 || str[i][j] > 57)
			return (1);
		j++;
		}
		j = 0;
		i++;
	}
	return (0);
}

// need to put it correctly
// like the return value
int ft_verif_double(struct node *curr, int nbr, int pos)
{
	int i = 1;
	while(i < pos)
	{
		if(curr->nbr == nbr)
			return (0);
		curr = curr->next;		
		i++;
	}
	return (1);
}

int main(int argc, char **argv)
{
	int i = 1;
	struct node *tail = NULL;
	struct node *head = NULL;
	//will have to check more error
		// if the string is empty
	if(argc < 2)
		return(1);
	int check = only_int_allowed(argv);
	if(check == 1)
		return (1);
	int start = ft_atoi(argv[i]);
	init_stack(&tail, &head, start, i);
	i++;
	int node;
	while(argv[i])
	{
		node = ft_atoi(argv[i]);
		weHaveToGoDeeper(node, i, &head);
		i++;
	}
	struct node *curr;
	curr = tail;
	// check for double verification
	// might put it into a helper function
	while(curr != NULL)
	{
		if(ft_verif_double(tail, curr->nbr, curr->pos) == 0)
			return (1);
		printf("%i - > %i\n", curr->nbr, curr->pos);
		curr = curr->next;
	}
	return (0);
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