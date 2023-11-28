#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a sorted
 * @head: double pointer
 * @number: insert number
 * Return: the address of the new node otherwise NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *nw = malloc(sizeof(listint_t));

	if (!nw)
		return (NULL);
	nw->n = number;
	nw->next = NULL;

	if (!nd || nw->n < nd->n)
	{
		nw->next = nd;
		return (*head = nw);
	}
	while (nd)
	{
		if (!nd->next || nw->n < nd->next->n)
		{
			nw->next = nd->next;
			nd->next = nw;
			return (nd);
		}
		nd = nd->next;
	}
	return (NULL);
}
