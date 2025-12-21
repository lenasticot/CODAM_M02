// write a program that takes a positive int and displays its prime factors on the
// standard output, followed by a newline
// factors must be displayed in ascending order and separated by '*', so that the expression in the output
// gives the right result

// if the number of parameters is not 1, simply display a newline

#include <unistd.h>
#include <stdio.h>

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_putnbr(int a)
{
    if(a <= 9)
    {
        ft_putchar(a + '0');  
        return ;
    }

    ft_putnbr(a / 10);
    ft_putnbr(a % 10);

}


int ft_atoi(char *c)
{
    int res = 0;
    int i = 0;
    int sign = 1;

    while(c[i] == ' ')
        i++;
    ih(c[i] == '+' || c[i] == '-')
        {
            if(c[i] == '-')
                sign += -1;
            i++;
        }
    while(c[i] && c[i] >= '0' && c[i] <= '9')
    {
        res = res * 10 + (c[i] + '0');
        i++;
    }
    res *= sign;
    return(res);
}

int main(int argv, char **argc)
{
    int res;
    int i = 2;
    if(argv < 2)
        return(write(1, "\n", 1));
    
    res = ft_atoi(argc[1]);
    while(i <= res)
    { 
        if(res % i == 0)
        {
            ft_putnbr(i);
 
            if(res != i)
                write(1, "*", 1);
             res = res / i;
        }
        else
            i++;
    }

}