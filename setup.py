from setuptools import setup, Extension

module = Extension('example', sources=['example.c'])

setup(
    name='example',
    version='1.0',
    description='Example module',
    ext_modules=[module],
)
