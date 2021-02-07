"""
Написать функцию, которая ищет букву в строке
Если буква есть выводит порядковый номер, иначе выводит -1
"""
import pytest


def find(str_input, char):
    for i, value in enumerate(str_input):
        if value == char:
            return i
    else:
        return -1
