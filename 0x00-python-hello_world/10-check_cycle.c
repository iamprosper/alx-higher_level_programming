#include "lists.h"
/**
 * check_cycle - check if a linked list has a cycle
 * @list: A pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;

	while (current->next != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
