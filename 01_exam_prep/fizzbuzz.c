// Write a program that prints the number from 1 to 100, each separated by a newline
// if the number if a multiple of 3, it prints fizz instead
// if the number is a multiple of 5, it prints buzz instead
// if the number is both a multiple of 3 and a multiple of 5
// it prints fizzbuzz instead



#include <unistd.h>
char *ft_putnbr(int i)
{
	char *result;


}

int main(void)
{
int i;
i = 1;

while (i < 100)
{
	write(1, i, 1);
	i++;
}


if (i % 3)
	write(1, "fizz", 4);
if (i % 5)
	write(1, "buzz", 4);
if (i)
}