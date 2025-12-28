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

// creating a new node and pushing it on top

void push(int data, int pos, struct node *top)
{
    struct node *newNode;
    newNode = malloc(sizeof(newNode));
    if (newNode == NULL)
        return (NULL);
    newNode->nbr = data;
    newNode->pos = pos;

    newNode->link = top;
    newNode->prev = 
    newNode->next = 
    top = newNode;
}

void push_swap(char **argv)
{
    char *res;
    int *tmp;
    int i = 2;
    
    struct node *stack_a = NULL;
    struct node *stack_b = NULL;

    if(*argv <= 1)
        return (NULL)
    if(*argv == 2)
        {
            ft_split(argv[2]);
            res = ft_atoi(argv[2]);
        }
    else if(*argv > 2)
    {
        while(*argv)
        { 
        tmp = ft_atoi(argv[i]);
        // add it to the linked list, but should I have a special one for the first one? 
        //Maybe to do before the while loop
        i++;
        // do I need to free tmp?
        }
    }
}