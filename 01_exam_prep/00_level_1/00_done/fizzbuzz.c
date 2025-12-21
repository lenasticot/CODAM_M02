// Write a program that prints the number from 1 to 100, each separated by a newline
// if the number if a multiple of 3, it prints fizz instead
// if the number is a multiple of 5, it prints buzz instead
// if the number is both a multiple of 3 and a multiple of 5
// it prints fizzbuzz instead



#include <unistd.h>


void ft_putchar(char c)
{
	write(1, &c, 1);
}
void ft_putnbr(int i)
{
	if (i <= 9)
	{
		ft_putchar(i + '0');
		return ;
	}
	ft_putnbr(i / 10);
	ft_putnbr(i % 10);
}

int main(void)
{
int i;
i = 1;
while (i <= 100)
{ 
	if (i % 3 == 0 && i % 5 == 0)
		write(1, "fizzbuzz", 8);
	else if (i % 3 == 0)
		write(1, "fizz", 4);
	else if (i % 5 == 0)
		write(1, "buzz", 4);
	else 
		ft_putnbr(i);
i++;
write(1, "\n", 1);
}

}