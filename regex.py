"""
Файл с регулярными выражениями для разрабатываемого языка программирования
Здесь представлены лексемы
Лексемы:
Переменная (VAR)
Знак арифметической операции (OP)
Знак операции присвоения (ASSIGN_OP)
Число (NUMBER)
Знак логической операции (LOGICAL_OP)
Ключевое слово if (IF_KW)
Ключевое слово else (ELSE_KW)
Ключевое слово while (WHILE_KW)
Ключевое слово do (DO_KW)
Скобки:
( (L_BR)  
) (R_BR)  
"""

# Регулярные выражения для токенов
VAR_R = r'[a-zA-Z]{1}[a-zA-Z_0-9]*'
OP_R = r'[\+\-\*/]{1}'
ASSIGN_OP_R = r'='
NUMBER_R = r'0|-?[1-9][0-9]*'
LOGICAL_OP_R = r'&|\|\||==|!=|<|>|<=|>='
IF_KW_R = r'if'
THEN_KW_R = r'then'
ELSE_KW_R = r'else'
WHILE_KW_R = r'while'
DO_KW_R = r'do'
L_BR_R = r'\('
R_BR_R = r'\)'
MARK_R = r'M[1-9][0-9]*\:?'
ONLY_MARK_R = r'M[1-9][0-9]*'
PUT_VALUE_R = r'put_value'
GET_VALUE_R = r'get_value'
DELETE_VALUE_R = r'delete_value'
EOL_R = r';'
DOUBLE_LINKED_LIST_R = r'DoubleLinkedList'
HASH_TABLE_R = r'HashTable'
INSERT_R = r'insert'
GET_R = r'get'
DELETE_R = r'delete'
PRINT_R = r'print'
COMA_R = r','

checklist = (
    ('IF_KW', IF_KW_R),
    ('ELSE_KW', ELSE_KW_R),
    ('THEN_KW', THEN_KW_R),
    ('WHILE_KW', WHILE_KW_R),
    ('DLL_KW', DOUBLE_LINKED_LIST_R),
    ('INSERT_KW', INSERT_R),
    ('PRINT_KW', PRINT_R),
    ('GET_KW', GET_R),
    ('DELETE_KW', DELETE_R),
    ('DO_KW', DO_KW_R),
    ('PUT_VAL_KW', PUT_VALUE_R),
    ('GET_VAL_KW', GET_VALUE_R),
    ('DEL_VAL_KW', DELETE_VALUE_R),
    ('HT_KW', HASH_TABLE_R),
    ('L_BR', L_BR_R),
    ('R_BR', R_BR_R),
    ('LOGICAL_OP', LOGICAL_OP_R),
    ('VAR', VAR_R),
    ('OP', OP_R),
    ('ASSIGN_OP', ASSIGN_OP_R),
    ('NUMBER', NUMBER_R),
    ('END_OF_LINE', EOL_R),
    ('COMA', COMA_R)
)
