"""
Перевод токенов в обратную польскую запись
"""
import re

import regex

stack = []

priority = (
    ['(', 0],
    ['if', 0, '', ''],
    ['while', 0, '', ''],
    ['DoubleLinkedList', 1],
    ['HashTable', 1],
    ['get_value', 6],
    ['put_value', 1],
    ['delete_value', 1],
    ['insert', 1],
    ['print', 1],
    ['get', 6],
    ['delete', 1],
    [')', 1],
    [';', 1],
    ['else', 1],
    ['then', 1],
    ['do', 1],
    ['=', 2],
    ['||', 2],
    ['&', 3],
    ['<', 5],
    ['>', 5],
    ['==', 5],
    ['<=', 5],
    ['>=', 5],
    ['!=', 5],
    ['+', 6],
    ['-', 6],
    ['*', 7],
    ['/', 7]
)
output = []


def rpn(token_list):
    m = 0
    for token in token_list:

        is_op = False
        operation = []

        for op in priority:
            if token[1] == op[0]:
                is_op = True
                operation = list(op)

        is_bracket = operation and (operation[0] == '(' or operation[0] == ')'
                                    or operation[0] == '{' or operation[0] == '}')
        is_condition = operation and (operation[0] == 'if' or operation[0] == 'else' or operation[0] == 'then'
                                      or operation[0] == 'while' or operation[0] == 'do')
        is_eol = operation and operation[0] == ';'
        if is_op:
            # print('Operation', operation, 'Stack: ', stack, 'Output: ', output)
            if not stack:
                stack.append(operation)

            elif stack[-1][1] < operation[1] and not is_bracket and not is_condition and not is_eol:
                stack.append(operation)

            elif stack[-1][1] >= operation[1] and not is_bracket and not is_condition and not is_eol:
                while stack and stack[-1][1] >= operation[1]:
                    push_to_output(stack, output)
                stack.append(operation)

            elif operation[0] == '(':
                stack.append(operation)

            elif operation[0] == ')':

                # Алгоритм для скобок в арифметико-логическом выражении

                while stack and stack[-1][0] != '(':
                    push_to_output(stack, output)
                stack.pop()

            elif operation[0] == '{':
                stack.append(operation)

            elif operation[0] == '}':

                # Алгоритм для скобок в арифметико-логическом выражении

                while stack and stack[-1][0] != '{':
                    push_to_output(stack, output)
                stack.pop()

            elif operation[0] == 'if':
                stack.append(operation)

            elif operation[0] == 'then':
                while stack and stack[-1][0] != 'if':
                    push_to_output(stack, output)
                m += 1
                # print('Priority ', priority)
                # print(f'm is {m}')
                # stack[-1].append(f'M{m}')
                stack[-1][2] = f'M{m}'
                stack[-1][3] = f'M{m}'
                output.append(f'{stack[-1][2]}')
                output.append('УПЛ')
            elif operation[0] == 'else':
                while stack and stack[-1][0] != 'if':
                    push_to_output(stack, output)
                m += 1
                stack[-1][2] = f'M{m}'
                output.append(f'M{m}')
                output.append('БП')
                # output.append(f'M{m-1}:')
                output.append(f'{stack[-1][3]}:')
            elif operation[0] == 'while':
                stack.append(operation)
                m += 1
                output.append(f'M{m}:')
                stack[-1][2] = f'M{m}'
            elif operation[0] == 'do':
                while stack and stack[-1][0] != 'while':
                    push_to_output(stack, output)
                m += 1
                stack[-1][3] = f'M{m}'
                output.append(f'M{m}')
                output.append('УПЛ')
            elif operation[0] == ';':
                while stack and stack[-1][0] != 'if' and stack[-1][0] != 'while':
                    push_to_output(stack, output)
            # elif operation[0] == ',':
                # continue
        else:
            if token[1] == ',':
                continue
            else:
                output.append(token[1])

    stack.reverse()
    if stack and stack[0][0] == ';':
        stack.pop(0)
    for op in stack:
        output.append(op[0])
    stack.clear()

    # numbers_from_string(output)
    print('Result: ', output)
    return output


def push_to_output(st, out):
    if st[-1][0] == 'if':
        out.append(f'{st[-1][2]}:')
    elif st[-1][0] == 'while':
        out.append(f'{st[-1][2]}')
        out.append('БП')
        out.append(f'{st[-1][3]}:')
    else:
        out.append(st[-1][0])

    st.pop()

# a+b<-5&2-c==1+q
# y-(if a>b then x+1 else x+2)
# (if a>b then (if a>b then x+1 else x+2) else x+2)
# (while a>b do x+2)
# (while a>b do (while a>b do x+1))
