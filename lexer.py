import regex
import re

"""Лексер отвечает за разбиение текста программы на токены"""


# Метод разбиения текста программы на лексемы
def split(file):
    buf = []
    res = []
    for line in file:
        line = line.rstrip("\n")
        print(line)
        buf.append(re.split(
            r'\s*([=><!]?[=]|-?[0-9]*|[-\+\*\{\}\(\)\/\<\>\~]|[&]|[\|]{2}|\bif\b|\belse\b|\bdo\b|\bwhile\b|\w*)\s*', line))
        # buf = re.split(r'\s*(\w*\W*\d*)\s*', line)
    for n in range(len(buf)):
        buf[n] = [i for i in buf[n] if i != '']
    for i in range(len(buf)):
        res += buf[i]
    print(res)
    return res


# Метод создания токенов
def create_token(sep_list):
    token_list = []
    for lexeme in sep_list:
        # print("lexeme", lexeme)
        for rule in regex.checklist:
            # print(rule[1])
            if re.fullmatch(rule[1], lexeme):
                right_token = True
                token_list.append([rule[0], lexeme])
                break
    if len(sep_list) != len(token_list):
        raise Exception('Unknown symbols!')
    print(token_list)
    return token_list
