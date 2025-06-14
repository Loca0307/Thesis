#include "main.h"
/**
 * prompt - checks mode and prints prompt if in interactive mode
 * @fd: file stream
 */
void prompt(int fd)
{
    struct stat buf;
    
    if (fstat(fd, &buf) == -1)
    {
        return;
    }

    if (S_ISCHR(buf.st_mode))
        _puts(PROMPT);
}
/**
* _puts - prints a string without a \n
* @str: string to print
* Return: void
*/
void _puts(char *str)
{
	unsigned int length;

	length = _strlen(str);

	write(STDOUT_FILENO, str, length);
}