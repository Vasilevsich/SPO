import lexer
import MyParser
import rpn
import stack

file = open("complex_test")
# file = open("hashtable_test")
# file = open("inner_conditions")
# file = open("infinite_brackets")
# file = open("dll_test")
raw_text = lexer.split(file)
token_list = lexer.create_token(raw_text)
myParser = MyParser.MyParser(token_list)
myParser.start()
reversePolishNotation = rpn.rpn(token_list)
stack.rpn_calculation(reversePolishNotation)
file.close()

