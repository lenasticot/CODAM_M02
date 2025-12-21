// write a program called alpha_mirror that takes a string and displays this string
// after replacing each alphabetical character by the opposite alphabetica characterm followed by a newline

// 'a' becomes 'z', 'Z' becomes 'A'
// 'd' becomes 'w', 'M' becomes 'N'

//Case is not changed
// if the number of arguments is not 1, display only a newline

#include <stdio.h>
#include <unistd.h>

int ft_strlen(char *c)
{
	int i = 0;


	while (c)
	i++;

	return(i);
}

int main(int argv, char **argc)
{
	int i;
	char *result;

	i = 0;
	if(argv == 2)
	{
		while (argc[1][i])
	{
		if(argc[1][i] >= 'a' && argc[1][i] <= 'z')
			result[i] = 122 - argc[1][i] + 97;
		else if(argc[1][i] >= 'A' && argc[1][i] <= 'Z')
			result[i] = 65 - argc[1][i] + 90;
	i++;
	}
	}
	else
		write(1, "\n", 1);

printf("%s", result);
	
	//need some rotation, need to remember how to do it with the ascii
}