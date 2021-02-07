"""
Напишите функцию, которая умножает значения целоцисленного массива на 2
Пример:
Вход: [1,2,3,4]
Выход: [2,4,6,8]
"""

import pytest


def mult_arr(arr):
    if not isinstance(arr, list):
        return
    output = []
    for i in arr:
        output.append(i * 2)
    return output


def test_normal_sum_int():
    assert mult_arr([1, 5]) == [2, 10]


def test_string_sum_int():
    assert mult_arr(112233) is None


if __name__ == "__main__":
    pass
