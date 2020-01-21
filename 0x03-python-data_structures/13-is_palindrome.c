#include "lists.h"
/**
 * is_palindrome - if palindrome?
 *
 *
 * @head: head
 *
 *
 * Return: 1 else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *second = *head;
	listint_t *new = *head;
	listint_t *ante = NULL;
	unsigned long int res = 0;

	while (second != NULL && second->next != NULL)
	{
		second = second->next->next;
		first = first->next; }
	new = first;
	ante = NULL;
	while (new != NULL)
	{
		second = new->next;
		new->next = ante;
		ante = new;
		new = second; }
	second = *head;
	new = ante;
	while (ante != NULL)
	{
		if (second->n != ante->n)
		{
			res = 1;
			break; }
		second = second->next;
		ante = ante->next; }
	ante = NULL;
	while (new != NULL)
	{
		second = new->next;
		new->next = ante;
		ante = new;
		new = second; }
	return (!res); }
