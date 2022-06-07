#ifndef LIST_H
#define LIST_H
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/**
 * struct listint_s - Singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: signly linked list node structure for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
size_t list_size(const listint_t *h);

int is_palindrome(listint_t **head);
void divide_linked_list(listint_t *head, listint_t **first_node, listint_t **second_node);
listint_t *add_nodeint_up(listint_t **head, const int n);
bool are_identic(listint_t *first_node, listint_t *second_node);
#endif
