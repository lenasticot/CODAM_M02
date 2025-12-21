// write a program that takes a positive int as argument and displays the sum
// of all prime numbers inferior or equal to it followed by a newline
// if the nbr of arguments is not 1, or the argument is not a positive number, 
// just display 0 followed by a newline

// check for prime numbers on my piscine
#include <unistd.h>
#include <stdio.h>

int is_prime(int nb)
{
    if (nb < 2)
        return (0);

        int i = 2;
    while (i <= nb/2)
    {
        if(nb % i == 0)
            return(0);
        i++;
    }
    return(1);
}

int ft_atoi(char *c)
{
    int i = 0;
    int result;
    int sign = 1;

    while(c[i] == '-' || c[i] == '+')
    {
        if(c[i] == '-')
            sign = -1;
        i++;
    }

    while(c[i] && c[i] >= '0' && c[i] <= '9')
    {
        result *= 10;
        result += c[i] - '0';
        i++;
    }
    result *= sign;
    return (result);

}

int main(int argv, char **argc)
{
    int nb;
    int res = 0;
    if(argv == 2)
    {
        nb = ft_atoi(argc[1]);
        while (nb > 1)
        {
            if(is_prime(nb))
            { 
                printf("%d, ", nb);
                res += nb;
            }
            nb--;
           
        }
    }
    else
            write(1, "0\n", 1);
  
    printf("\n The sum of it is: %i", res);
}