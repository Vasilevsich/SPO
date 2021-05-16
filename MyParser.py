"""
Парсер отвечает за проверку последовательности токенов
"""

"""""""""
lang -> expr+
expr -> assign_expr | operator_expr | create_struct_expr | bin_op_expr | tri_op_expr | print_expr
print_expr -> PRINT_KW L_BR VAR R_BR END_OF_LINE
operator_expr -> L_BR (if_expr | while_expr) R_BR
create_struct_expr -> (DLL_KW|HT_KW) VAR END_OF_LINE
bin_op_expr -> dll_bin_op | ht_bin_op
dll_del_op -> DELETE_KW L_BR VAR COMA NUMBER R_BR
ht_del_op -> DELETE_VAL_KW L_BR VAR COMA value R_BR
tri_op_expr -> insert_op | put_val_op
insert_val_op -> INSERT_KW L_BR VAR COMA NUMBER COMA NUMBER R_BR
delete_val_op -> PUT_VAL_KW L_BR VAR COMA value COMA value R_BR
value -> NUMBER | VAR | GET_KW L_BR VAR COMA NUMBER R_BR | GET_VAL_KW L_BR VAR COMA value R_BR
if_expr ->  if_head body (else_KW body)? 
if_head -> if_KW logical_expression THEN_KW
body -> expr+
logical_expression -> value (LOGICAL_OP value)*
while_expr ->  while_head body 
while_head -> while_KW logical_expression DO_KW
assign_expr -> VAR ASSIGN_OP value_expr* EOL
value_expr -> (value_expr_brackets | value) (OP value_expr)?
value_expr_brackets -> L_BR value_expr R_BR
"""""


class ParserNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def is_bin(token):
    return token[0] == 'DELETE_KW' or token[0] == 'DEL_VAL_KW'


def is_tri(token):
    return token[0] == 'INSERT_KW' or token[0] == 'PUT_VAL_KW'


def show_tree(root, depth):
    space = ''
    for i in range(depth):
        space += '  '
    print(space, root.name)
    for child in root.children:
        show_tree(child, depth + 1)


class MyParser:
    def __init__(self, token_list):
        self.tokens = list(token_list)
        self.root = None

    def start(self):
        self.root = self.lang()
        show_tree(self.root, 0)
        print('All Right!')

    def lang(self):
        node = ParserNode('lang')
        while len(self.tokens) > 0:
            node.add_child(self.expr())
        return node

    def expr(self):
        node = ParserNode('expr')
        if self.tokens[0][0] == 'VAR':
            node.add_child(self.assign_expr())
        elif self.tokens[0][0] == 'L_BR':
            node.add_child(self.operator_expr())
        elif self.tokens[0][0] == 'DLL_KW' or self.tokens[0][0] == 'HT_KW':
            node.add_child(self.create_struct_expr())
        elif is_bin(self.tokens[0]):
            node.add_child(self.bin_op())
        elif is_tri(self.tokens[0]):
            node.add_child(self.tri_op())
        elif self.tokens[0][0] == 'PRINT_KW':
            node.add_child(self.print_expr())
        else:
            raise Exception('Invalid syntax!', self.tokens[0][0])
        return node

    def print_expr(self):
        node = ParserNode('print_expr')
        node.add_child(self.match('PRINT_KW'))
        node.add_child(self.match('L_BR'))
        node.add_child(self.match('VAR'))
        node.add_child(self.match('R_BR'))
        node.add_child(self.match('END_OF_LINE'))
        return node

    def create_struct_expr(self):
        node = ParserNode('create_struct_expr')
        notDoubleLinkedL = True
        notHT = True
        try:
            node.add_child(self.match('DLL_KW'))
        except Exception:
            notDoubleLinkedL = False
        try:
            node.add_child(self.match('HT_KW'))
        except Exception:
            notHT = False
        if notDoubleLinkedL and notHT:
            raise Exception('Invalid syntax!')
        node.add_child(self.match('VAR'))
        node.add_child(self.match('END_OF_LINE'))
        return node

    def bin_op(self):
        node = ParserNode('bin_op')
        if self.tokens[0][0] == 'DELETE_KW':
            node.add_child(self.dll_del_op())
        elif self.tokens[0][0] == 'DEL_VAL_KW':
            node.add_child(self.ht_del_op())
        node.add_child(self.match('END_OF_LINE'))
        return node

    def dll_del_op(self):
        node = ParserNode('dll_del_op')
        node.add_child(self.match('DELETE_KW'))
        node.add_child(self.match('L_BR'))
        node.add_child(self.match('VAR'))
        node.add_child(self.match('COMA'))
        node.add_child(self.match('NUMBER'))
        node.add_child(self.match('R_BR'))
        return node

    def ht_del_op(self):
        node = ParserNode('ht_del_op')
        node.add_child(self.match('DEL_VAL_KW'))
        node.add_child(self.match('L_BR'))
        node.add_child(self.match('VAR'))
        node.add_child(self.match('COMA'))
        node.add_child(self.value())
        node.add_child(self.match('R_BR'))
        return node

    def tri_op(self):
        node = ParserNode('tri_op')
        if self.tokens[0][0] == 'INSERT_KW':
            node.add_child(self.insert_op())
        elif self.tokens[0][0] == 'PUT_VAL_KW':
            node.add_child(self.put_val_op())
        node.add_child(self.match('END_OF_LINE'))
        return node

    def insert_op(self):
        node = ParserNode('insert_op')
        node.add_child(self.match('INSERT_KW'))
        node.add_child(self.match('L_BR'))
        node.add_child(self.match('VAR'))
        node.add_child(self.match('COMA'))
        node.add_child(self.match('NUMBER'))
        node.add_child(self.match('COMA'))
        node.add_child(self.match('NUMBER'))
        node.add_child(self.match('R_BR'))
        return node

    def put_val_op(self):
        node = ParserNode('put_val_op')
        node.add_child(self.match('PUT_VAL_KW'))
        node.add_child(self.match('L_BR'))
        node.add_child(self.match('VAR'))
        node.add_child(self.match('COMA'))
        node.add_child(self.value())
        node.add_child(self.match('COMA'))
        node.add_child(self.value())
        node.add_child(self.match('R_BR'))
        return node

    def assign_expr(self):
        node = ParserNode('assign_expr')
        node.add_child(self.match('VAR'))
        node.add_child(self.match('ASSIGN_OP'))
        node.add_child(self.value_expr())
        node.add_child(self.match('END_OF_LINE'))
        return node

    def value_expr(self):
        node = ParserNode('value_expr')
        first_case = False
        second_case = False
        try:
            node.add_child(self.value_expr_brackets())
        except Exception:
            first_case = True
        try:
            node.add_child(self.value())
        except Exception:
            second_case = True
        if first_case and second_case:
            raise Exception('Invalid syntax!')
        try:
            node.add_child(self.match('OP'))
            node.add_child(self.value_expr())
        except Exception:
            None
        return node

    def value_expr_brackets(self):
        node = ParserNode('value_expr_brackets')
        node.add_child(self.match('L_BR'))
        node.add_child(self.value_expr())
        node.add_child(self.match('R_BR'))
        return node

    def value(self):
        node = ParserNode('value')
        if self.tokens[0][0] == 'NUMBER':
            node.add_child(self.match('NUMBER'))
            return node
        elif self.tokens[0][0] == 'VAR':
            node.add_child(self.match('VAR'))
            return node
        elif self.tokens[0][0] == 'GET_KW':
            node.add_child(self.match('GET_KW'))
            node.add_child(self.match('L_BR'))
            node.add_child(self.match('VAR'))
            node.add_child(self.match('COMA'))
            node.add_child(self.match('NUMBER'))
            node.add_child(self.match('R_BR'))
            return node
        elif self.tokens[0][0] == 'GET_VAL_KW':
            node.add_child(self.match('GET_VAL_KW'))
            node.add_child(self.match('L_BR'))
            node.add_child(self.match('VAR'))
            node.add_child(self.match('COMA'))
            node.add_child(self.value())
            node.add_child(self.match('R_BR'))
            return node
        else:
            raise Exception('Not a number or var: ', self.tokens[0][0])

    def operator_expr(self):
        node = ParserNode('operator_expr')
        not_if_expr = False
        not_while_expr = False
        node.add_child(self.match('L_BR'))
        try:
            node.add_child(self.if_expr())
        except Exception:
            not_if_expr = True
        try:
            node.add_child(self.while_expr())
        except Exception:
            not_while_expr = True
        if not_if_expr and not_while_expr:
            raise Exception('Invalid syntax!', self.tokens[0])
        node.add_child(self.match('R_BR'))
        return node

    def if_expr(self):
        node = ParserNode('if_expr')
        node.add_child(self.if_head())
        node.add_child(self.body())
        try:
            node.add_child(self.match('ELSE_KW'))
            node.add_child(self.body())
        except Exception:
            pass
        return node

    def if_head(self):
        node = ParserNode('if_head')
        node.add_child(self.match('IF_KW'))
        node.add_child(self.logical_expr())
        node.add_child(self.match('THEN_KW'))
        return node

    def body(self):
        node = ParserNode('body')
        node.add_child(self.expr())
        while self.tokens:
            try:
                node.add_child(self.expr())
            except Exception:
                break
        return node

    def logical_expr(self):
        node = ParserNode('logical_expr')
        node.add_child(self.value())
        # while self.tokens:
        # try:
        node.add_child(self.match('LOGICAL_OP'))
        node.add_child(self.value())
        # except Exception: break
        return node

    def while_expr(self):
        node = ParserNode('while_expr')
        node.add_child(self.while_head())
        node.add_child(self.body())
        return node

    def while_head(self):
        node = ParserNode('while_head')
        node.add_child(self.match('WHILE_KW'))
        node.add_child(self.logical_expr())
        node.add_child(self.match('DO_KW'))
        return node

    def match(self, terminal):
        node = ParserNode(self.tokens[0])
        if terminal == self.tokens[0][0]:
            #print('Token:', self.tokens[0][0])
            self.tokens.pop(0)
            return node
        else:
            raise Exception('Invalid syntax!' + self.tokens[0][0])
