// write a program called alpha_mirror that takes a string and displays this string
// after replacing each alphabetical character by the opposite alphabetica characterm followed by a newline

// 'a' becomes 'z', 'Z' becomes 'A'
// 'd' becomes 'w', 'M' becomes 'N'

//Case is not changed
// if the number of arguments is not 1, display only a newline

#include <unistd.h>
#include <stdio.h>

int main(int argv, char **argc)
{
    int i;


    //res = malloc(ft_strlen(argc[1], sizeof(char));
    i = 0;
    if (argv == 2)
    { 
    while(argc[1][i])
    {
        if (argc[1][i] >= 'a' && argc[1][i] <= 'z')
           argc[1][i] = 122 - argc[1][i] + 97;
        if (argc[1][i] >= 'A' && argc[1][i] <= 'Z')
           argc[1][i] = 90 - argc[1][i] + 65;
        write(1, &argc[1][i], 1);
        i++;
    }
    }
    write(1, "\n", 1);

}