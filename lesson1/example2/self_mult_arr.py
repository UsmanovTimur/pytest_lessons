"""
Самопроверка
реализовать функцию поэлементного сложения массивов
"""


def mult_arr(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        return
    if len(arr1) != len(arr2):
        return
    output = []
    for i, v in enumerate(arr1):
        output.append(v + arr2[i])
    return output


if __name__ == "__main__":
    pass
