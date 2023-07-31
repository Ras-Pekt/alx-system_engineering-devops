#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
/**
 * infinite_while - sleeps infintiely
 * Return: 0 on success
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point
 * Return: 0 on success. 1 otherwise
*/
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();

		if (pid == 0)
			exit(0);

		printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
