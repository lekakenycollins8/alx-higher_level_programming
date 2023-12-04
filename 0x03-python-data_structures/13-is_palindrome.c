#include <stddef.h>
#include "lists.h"

listint_t *reverse_list(listint_t *head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *prev_slow, *mid_node;
	int is_palindrome = 1;

	slow = fast = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	prev_slow->next = NULL;

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_list(second_half);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
	return (is_palindrome);
}

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
