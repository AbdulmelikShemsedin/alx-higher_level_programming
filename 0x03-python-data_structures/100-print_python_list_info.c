#include <stdio.h>
#include <Python.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info
 * @p: ...
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*]Size of the Python List = %li\n", Py_SIZE(p));
	printf("[*]Allocated = %li\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p; i++))
	{
		printf("Element %i: %s\n", i, Py_TYPE(Py_List_GetItem(p, i))->tp_name);
	}
}
