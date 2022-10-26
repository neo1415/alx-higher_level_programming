#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:52:37 2022

@author: Oyeniyi Daniel
"""


def number_of_lines(filename=""):
    """
    Counts the number of lines from the filename
    Arguments:
    filename (str): The name of the file to count in
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)
