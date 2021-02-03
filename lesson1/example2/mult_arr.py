"""
Напишите функцию, которая умножает значения целоцисленного массива на 2
Пример:
Вход: [1,2,3,4]
Выход: [2,4,6,8]
"""


def mult_arr(arr):
    if not isinstance(arr, list):
        return
    output = []
    for i in arr:
        output.append(i * 2)
    return output


if __name__ == "__main__":
    pass
