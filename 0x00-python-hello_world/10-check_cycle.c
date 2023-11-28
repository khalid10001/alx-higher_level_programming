#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list
 * @list: pointer list
 * Return: 0 if there is no cycle otherwise 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s;
	listint_t *f;

	s = list;
	f = list;
	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
