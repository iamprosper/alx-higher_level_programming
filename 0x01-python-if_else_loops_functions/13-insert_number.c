#include "lists.h"
/**
 * listint_t *insert_node - Insert a numbe into a sorted lkl
 * @head: pointer to the head of the linked list
 * @number: The number to add
 *
 * Return: The address of the nuew node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *last;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	last = current;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if (current->n < number)
			{
				last = current;
				current = current->next;
			}
			else
			{
				if (last == *head)
				{
					new->next = last;
					*head = new;
					break;
				}
				last->next = new;
				new->next = current;
				break;
			}
		}
		last->next = new;
	}
	return (new);
}
