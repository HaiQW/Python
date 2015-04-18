from distutils.core import setup, Extension

module1 = Extension('wrap',sources = ['wrap.cpp'])

setup(name = 'wrap',
      version = '1.0',
      description = 'add module',
      ext_modules = [module1])
