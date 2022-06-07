#include "lists.h"
#include <stdbool.h>
/**
 * is_palindrome - Check whether or not a singly list is a palindrome
 * @head: The head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 in case of success
 */
int is_palindrome(listint_t **head)
{

	listint_t *first_node = NULL;
	listint_t *second_node = NULL;
	listint_t *second_node_reversed = NULL;
	listint_t *current = NULL;

	if (list_size(*head) == 0)
		return (1);

	divide_linked_list(*head, &first_node, &second_node);
	current = second_node;

	while (current != NULL)
	{
		add_nodeint_up(&second_node_reversed, current->n);
		current = current->next;
	}

	/*
	 * print_listint(current);
	 * printf("-----------\n");
	 * print_listint(first_node);
	 * printf("------------\n");
	 * print_listint(second_node);
	 * printf("-------------\n");
	 * print_listint(second_node_reversed);
	 */

	if (are_identic(first_node, second_node_reversed))
		return (1);
	return (0);
}

/**
 * list_size - Get list size
 * @h: The head of the linked list
 *
 * Return: The size of the list
 */
size_t list_size(const listint_t *h)
{
	unsigned int n = 0;
	const listint_t *current;

	current = h;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * divide_linked_list - Divide a linked list by two
 * @head: The head of the linked list
 * @first_node: The first part of the subhead
 * @second_node: The last part of the subhead
 */
void divide_linked_list(listint_t *head, listint_t **first_node,
		listint_t **second_node)
{
	int n = 0;
	int count = 0;
	size_t s = list_size(head);
	listint_t *current;

	n = (int) (s / 2);
	/*printf("The mid of the size of the linked list is %d\n", n);*/
	current = head;

	while (count < n && current != NULL)
	{
		add_nodeint_end(first_node, current->n);
		current = current->next;
		count++;
	}
	if (s % 2 != 0)
	{
		current = current->next;
	}
	while (current != NULL)
	{
		add_nodeint_end(second_node, current->n);
		current = current->next;
	}

}

/**
 * are_identic - Compare two linked list
 * @first_node: The first list
 * @second_node: The second list
 *
 * Return: 0 if the are not equal, 1 in the other case
 */
bool are_identic(listint_t *first_node, listint_t *second_node)
{
	while (first_node != NULL && second_node != NULL)
	{
		if (first_node->n != second_node->n)
			return (false);
		first_node  =  first_node->next;
		second_node = second_node->next;
	}
	return (true);
}

/**
 * add_nodeint_up - Reverse a linked list or creat a stack
 * @head: The head of the linked list
 * @n: The date of each node
 *
 * Return: A linked list newly formed
 */
listint_t *add_nodeint_up(listint_t **head, const int n)
{
	listint_t *new = NULL;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		(*head)->n = n;
		(*head)->next = NULL;
	}
	else
	{
		new = malloc(sizeof(listint_t));
		new->n = n;
		new->next = *head;
		*head = new;
	}
	return (*head);
}
