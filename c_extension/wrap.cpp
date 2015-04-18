#include "Python.h"

int add(int arg1, int arg2)
{
  return arg1 + arg2;
}

/// wrap function of add
static PyObject* wrap_add(PyObject *self, PyObject *args)
{
  int arg1, arg2;
  if(!PyArg_ParseTuple(args, "ii", &arg1, &arg2))
  {
    return NULL;
  }

  int results = add(arg1, arg2);

  return (PyObject*)Py_BuildValue("i",results);
}

static PyMethodDef wrap_methods[] = {
  {"add", wrap_add, METH_VARARGS},
  {NULL,NULL}
};

/// add module initialization function for c extension
PyMODINIT_FUNC initwrap(void)
{
  Py_InitModule("wrap", wrap_methods);
}
