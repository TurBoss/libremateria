# -*- coding: utf-8 -*-
__author__ = 'TurBoss'

"""
This is a setup script for cx_Freeze.
Usage: python setup_cx_freeze.py build
Tested with cx_Freeze 4.3.4 (latest available version for Python 2.7 on 2015-02-23, released on 2014-12-26).
Environment: Python Portable 2.7.6.1. on Windows 7 32bit.
"""

# Import program components / modules from python standard library / non-standard modules.
import sys

from cx_Freeze import setup, Executable


base = 'Win32GUI' if sys.platform == 'win32' else None  # build a Windows GUI application
icon = 'icon.ico'

executables = [
    Executable(script='Libre.py',
               initScript=None,
               base=base,
               targetName='LibreMateria.exe',
               icon=icon)
]

packages = []
includes = []
excludes = ['Tkinter']
include_files = ['icon.ico']
path = []
build_options = dict(packages=packages, includes=includes, excludes=excludes, include_files=include_files, path=path)

setup(name='LibreMateria',
      version='1.3.3.7',
      description='Tool to modify ff7 materia attributes',
      author='TurBos',
      author_email='m',
      license='GNU GENERAL PUBLIC LICENSE, Version 2, June 1991',
      url='',
      options=dict(build_exe=build_options),
      executables=executables, requires=['cx_Freeze', 'wxPython'])
