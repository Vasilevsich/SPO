"""
Методы, реализующие вычисление обратной польской записи на стеке
"""
import re

import regex

import DoubleLL

import hashTable

math_log_operations = ('+', '-', '*', '/', '&', '||', '==', '<=', '>=', '!=', '<', '>')
# Словарь, в котором хранятся переменные программы и соответствующие им значения
variables = {}


def rpn_calculation(reverse_polish_notation):
    main_stack = []
    i = 0
    while i < len(reverse_polish_notation):
        if reverse_polish_notation[i] in math_log_operations:
            m_l_operation(reverse_polish_notation[i], main_stack.pop(), main_stack.pop(), main_stack)
        elif reverse_polish_notation[i] == '=':
            assign_operation(variables, main_stack.pop(), main_stack.pop())
        elif is_jump(reverse_polish_notation[i]):

            mark = main_stack.pop()
            cond = True
            if reverse_polish_notation[i] == 'УПЛ':
                cond = main_stack.pop()
            if reverse_polish_notation[i] == 'УПЛ' and not cond or reverse_polish_notation[i] == 'БП':
                i = make_jump(main_stack, mark, reverse_polish_notation)
        elif reverse_polish_notation[i] == 'DoubleLinkedList':
            create_dll(variables, main_stack.pop())
        elif reverse_polish_notation[i] == 'insert':
            insert_into_list(main_stack, main_stack.pop(), main_stack.pop(), main_stack.pop())
        elif reverse_polish_notation[i] == 'print':
            print_var(main_stack.pop())
        elif reverse_polish_notation[i] == 'get':
            main_stack.append(get_l(main_stack.pop(), main_stack.pop()))
        elif reverse_polish_notation[i] == 'delete':
            delete_l(main_stack.pop(), main_stack.pop())
        elif reverse_polish_notation[i] == 'HashTable':
            create_ht(variables, main_stack.pop())
        elif reverse_polish_notation[i] == 'put_value':
            put_val(main_stack.pop(), main_stack.pop(), main_stack.pop())
        elif reverse_polish_notation[i] == 'get_value':
            main_stack.append(get_val(main_stack.pop(), main_stack.pop()))
        elif reverse_polish_notation[i] == 'delete_value':
            del_val(main_stack.pop(), main_stack.pop())
        else:
            # print('append')
            main_stack.append(reverse_polish_notation[i])
            # append_format(reverse_polish_notation[i], main_stack)
        i += 1
    print('Variables are: ', variables)


def m_l_operation(token, s_op, f_op, stack):
    result = ''
    op1 = get_value(f_op)
    op2 = get_value(s_op)
    if token == '+':
        result = op1 + op2

    if token == '-':
        result = op1 - op2

    if token == '*':
        result = op1 * op2

    if token == '/':
        result = op1 / op2

    if token == '&':
        result = op1 and op2

    if token == '||':
        result = op1 or op2

    if token == '==':
        result = op1 == op2

    if token == '<=':
        result = op1 <= op2

    if token == '>=':
        result = op1 >= op2

    if token == '!=':
        result = op1 != op2

    if token == '<':
        result = op1 < op2

    if token == '>':
        result = op1 > op2

    stack.append(result)


# Присвоение переменной нового значения
def assign_operation(var_list, value, var):
    var_list[var] = get_value(value)


# Является ли токен переменной
def variable_chek(token):
    return not re.fullmatch(regex.NUMBER_R, token) and not re.fullmatch(regex.MARK_R, token)


# Метод возвращает либо значение переменной, либо число
def get_value(token):
    if token in variables:
        return variables.get(token)
    else:
        return float(token)


def make_jump(stack, mark, string):
    return go_to(stack, mark, string)


def go_to(stack, mark, string):
    stack.clear()
    return string.index(f'{mark}:')


def is_jump(token):
    return token == 'УПЛ' or token == 'БП'


def append_format(token, stack):
    if re.fullmatch(regex.NUMBER_R, token):
        stack.append(int(token))
    else:
        stack.append(token)


# DoubleLinkedList на стеке
def create_dll(var_list, tmp):
    var_list[tmp] = DoubleLL.DoubleLL()


def insert_into_list(stack, first, second, third):
    # 'a', '0', '1', 'insert'
    # get_value(stack[-3]).insert(get_value(stack[-2]), DoubleLL.DllNode(get_value(stack[-1])))
    get_value(third).insert(get_value(second), DoubleLL.DllNode(get_value(first)))


def print_l(ll):
    # print('-----Print_list result-----')
    get_value(ll).print_list()


def get_l(index, ll):
    print('-----Get-----')
    print(get_value(ll).get(get_value(index)))
    return get_value(ll).get(get_value(index))


def delete_l(index, ll):
    get_value(ll).delete(get_value(index))


def put_val(val, key, ht):
    get_value(ht).put_value(str(key), str(val))


def get_val(key, ht):
    return get_value(ht).get_value(str(key))


def del_val(key, ht):
    get_value(ht).delete_value(str(key))


def print_var(var):
    print('PRINT')
    try:
        print_l(var)
    except:
        try:
            get_value(var).print_hash_table()
        except:
            print(get_value(var))


def create_ht(var_list, var):
    var_list[var] = hashTable.HashTable()


"""
DoubleLinkedList a;
insert(a,0,1);
insert(a,0,2);
insert(a,1,3);
get(a,1);
print_list(a);
a = 10;

a = 10;
DoubleLinkedList a;
insert(a,0,1);
insert(a,1,2);
insert(a,1,3);
get(a,1);
a = get(a,1);

"""
