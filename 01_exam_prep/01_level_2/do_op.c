#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*Write a program that takes three strings
- the firt and the third one are representation of base-10 signed integers
that fit in an int
- the second one is an arithmetic operator chosen from: + - * / % 

The program must display the result of the requested arithmetic operation,
followed by a newline. If the number of parameters is not 3, the program 
just display a newline

You can assume the string have no mistakes or extraneous characters. Negative
numbers, in input or output, will have one and only one leading '-'. The
result of the operation fits in an int.*/


// not working with  * for some reasons


int whatisthat(char *operator, int first, int second)
{
	int result = 0;

	if(*operator == '-')
		result = first - second;
	if(*operator == '+')
		result = first + second;
	if(*operator ==  '*')
		result = first * second;
	if(*operator == '/')
		result = first / second;

	return(result);
}


int main(int argc, char **argv)
{
	int result = 0;

	if(argc != 4)
		return (write(1, "\n", 1));

	int first = atoi(argv[1]);
	int second = atoi(argv[3]);
	
	result = whatisthat(argv[2], first, second);
	printf("%d %s %d = %d\n", first, argv[2], second, result);

}