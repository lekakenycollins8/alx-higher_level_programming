#include "lists.h"

/**
 * check_cycle - Check if a singly list has a cycle in it or loop
 * @head: pointer to the list head
 * Return: 1 if there's a cycle and 0 if there's no cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *previous, *forward;

	if (head == NULL)
	{
		return (0);
	}
	previous = forward = head;
	while (1)
	{
		if (forward->next != NULL && forward->next->next != NULL)
		{
			forward = forward->next->next;
			previous = previous->next;
			if (previous == forward)
			{
				return (1);
			}
		}
		else
		{
			return (0);
		}
	}
}
