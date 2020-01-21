#include <stdio.h>
#include <stdlib.h>
#include "Python.h"
/**
 * print_python_list_info - python list
 *
 * @p: PyObject
 *
 *
 * Return: list
 */
void print_python_list_info(PyObject *p)
{
	unsigned long int i;

	printf("[*] Size of the Python List = %lu\n",
	       Py_SIZE(p));
	printf("[*] Allocated = %lu\n",
	       ((PyListObject *)p)->allocated);
	for (i = 0; i < PyLis
		     t_Size(p);)
	{
		printf("Element%d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->
		       tp_name);
		i++;
	}
}
