#include "lists.h"

/**
 * check_cycle - check if listint_t list has a cycle
 * @list: pointer to list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr_list, *next_list;

	if (!list)
	{
		return (0);
	}

	curr_list = list;
	next_list = list->next;
	while (next_list && curr_list && next_list->next)
	{
		curr_list = curr_list->next;
		next_list = next_list->next->next;

        if (curr_list == next_list)
		{
			return (1);
		}
	}

	return (0);
}