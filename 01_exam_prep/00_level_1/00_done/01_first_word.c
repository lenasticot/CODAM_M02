// Write a program that takes a string and displays its first word, followed by a
// newline.

// A word is a section of string delimited by spaces/tabs or by the start/end of
// the string.

// If the number of parameters is not 1, or if there are no words, simply display
// a newline.

#include <unistd.h>

int main(int argv, char **argc)
{
    int i = 0;

    if(argv < 2 || argc[1][i] == '\0')
        return (write(1, "\n", 1));
    
    while (argc[1][i] == ' ' || argc[1][i] == ' ')
        i++;
    while ((argc[1][i] != ' ' || argc[1][i] != ' ') && argc[1][i])
    {
        write(1, &argc[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
}