import os
from setuptools import setup, find_packages
from os import name
import LED

setup(
    name = "comp30670Assignment3 by Otto Hermann aka 16203034",
    description = "comp30670 Assignment 3, Spring 2017",
    author = "Otto Hermann",
    author_email = "otto.hermann@ucdconnect.ie",
    url="www.haha-no-i-do-not-have-one.org",
    py_modules = ['Grid', 'Instructions', 'LED', 'Links', 'Modification', 'Test'],
    data_files = ['LinksSource.txt']
    )