"""
написать функцию разделяющую строку по определенному символу
На входе строка и символ разделения,
на выходе массив массивов с итоговыми строками
Символ разделения в итог не входит!
"""


def split(str_input, split_char):
    output = []
    start = 0
    for i, val in enumerate(str_input):
        if val == split_char:
            output.append(str_input[start:i])
            start = i+1
    output.append(str_input[start:len(str_input)])
    return output


if __name__ == "__main__":
    pass
