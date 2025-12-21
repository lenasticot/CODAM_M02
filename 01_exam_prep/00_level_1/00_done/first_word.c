// Write a progra that takes a string and displays its first word
// Followed by a newline
// a word is a section of string delimited by spaces/tab or by the start.end of the string
// if the number of parameters is not 1, or if there are no words
// simply display a newline

#include <unistd.h>

int main (int argc, char **argv)
{
	char *result;
	int i;

	i = 0;
	if(argc < 2)
		return ('\n');

	while (argv[1][i] == ' ' || argv[1][i] == '	')
		i++;
	while ((argv[1][i] != ' ' || argv[1][i] != '	') && argv[1][i] != '\0')
	{
	write(1, &argv[1][i], 1);
	i++;
	}
}