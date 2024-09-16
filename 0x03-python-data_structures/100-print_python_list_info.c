#include "lists.h"
#include <listobject.h>
#include <Python.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info
 * @p: ...
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
