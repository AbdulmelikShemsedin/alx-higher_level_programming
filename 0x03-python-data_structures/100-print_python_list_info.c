<<<<<<< HEAD
#include <object.h>
#include <listobject.h>
=======
#include <stdio.h>
>>>>>>> 5bfdf85f4c9ef06880d2a62e911d1757efc72b3f
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
