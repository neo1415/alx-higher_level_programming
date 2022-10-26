#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 3 10:49:57 2022

@author: Oyeniyi Daniel
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
    filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
