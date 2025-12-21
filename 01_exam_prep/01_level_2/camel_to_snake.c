// Assignment name  : camel_to_snake
// Expected files   : camel_to_snake.c
// Allowed functions: malloc, realloc, write
// --------------------------------------------------------------------------------

// Write a program that takes a single string in lowerCamelCase format
// and converts it into a string in snake_case format.

// A lowerCamelCase string is a string where each word begins with a capital letter
// except for the first one.

// A snake_case string is a string where each word is in lower case, separated by
// an underscore "_".
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int ft_strlen_upper(char *test)
{
    int i = 0;
    int count = 1;

    while(test[i])
    {
        if(test[i] <= 'A' && test[i] >= 'Z')
            count++;
        i++;
        count++;
    }
    return(count);
}

char *camel_to_snake(char *test, char *result)
{
    int i = 0;
    int j = 0;
    result[j++] = test[i++];

    while(test[i])
    {
        if(test[i] >= 'A' && test[i] <= 'Z')
        {
            result[j++] = '_';
            result[j++] = test[i++] + 32;
        }
        else
        { 
        result[j] = test[i];
        i++;
        j++;
        }
    }
    result[j] = '\0';
    return(result);
}

int main(int argv, char **argc)
{
    char *test = "camelToSnake";
    char *result;
    int count;

    // to see if i need to argc then i have to do the check before

    count = ft_strlen_upper(argc[1]);
    result = malloc(count +1);
    if (!result)
        return (NULL);
    
    result = camel_to_snake(test, result);
    printf("%s", result);

}