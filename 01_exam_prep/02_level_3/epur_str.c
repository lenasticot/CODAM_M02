/*write a program that takes a string, and displays this string with
exactly one space between words, with no spaces or tabs either at the
beginning or the end followed by a \n

a word is defined as a part of a string delimited eitherr by spaces/tabs
or by the start/end of the string

if the number of arguments is not 1, or if there are no words to display, 
the program should displays \n
*/

#include <unistd.h>


void ft_putchar(char c)
{
	write(1, &c, 1);
}
int ft_strlen(char *c)
{
	int i = 0;

	while(c[i])
		i++;
return i;
}
int main(int argc, char **argv)
{
	char *result;

	if(argc < 2)
		return(write(1, "\n", 1));
	int i = 0;
	// remove space at the beginning
	while (argv[1][i] && (argv[1][i] == ' ' || argv[1][i] == '\t'))
		i++;
	int size = ft_strlen(argv[1]) -1;
	while(argv[1][size] == ' ' || argv[1][size] == '\t')
		size--;

	while(i <= size)
	{
		while(i <= size && argv[1][i] != ' ' && argv[1][i] != '\t')
		{
		ft_putchar(argv[1][i]);
		i++;
		}
		if(argv[1][i] == ' ' || argv[1][i] == '\t')
		{
			if(i >= size)
				break;
			ft_putchar(' ');
			while(i <= size && (argv[1][i] == ' ' || argv[1][i] == '\t'))
				i++;
		}
	}
}