# different constants for different tokens
INT = 'INT'
FLOAT = 'FLOAT'
LPAR = 'LPAR'
RPAR = 'RPAR'
DIV = 'DIV'
MUL = 'MUL'
ADD = 'ADD'
SUB = 'SUB'
MOD = 'MOD'


class Token:

    
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
     
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr_char = None
        self.move_to_next_character()

    def move_to_next_character(self):
        self.pos = self.pos + 1
        
        if self.pos < len(self.text):
            self.curr_char = self.text[self.pos]
        else:
            self.curr_char = None

    def make_tokens(self):
        tokens = []
        skip_characters = ['\t', ' ']
        while self.curr_char != None:
            if self.curr_char in skip_characters:
                self.move_to_next_character()
            elif self.curr_char == '+':
                tokens.append(Token(ADD, self.curr_char))
            elif self.curr_char == '-':
                tokens.append(Token(SUB, self.curr_char))
            elif self.curr_char == '*':
                tokens.append(Token(MUL, self.curr_char))
            elif self.curr_char == '/':
                tokens.append(Token(DIV, self.curr_char))
            elif self.curr_char == '%':
                tokens.append(Token(MOD, self.curr_char))
            elif self.curr_char == '(':
                tokens.append(Token(LPAR, self.curr_char))
            elif self.curr_char == ')':
                tokens.append(Token(RPAR, self.curr_char))
            
        return tokens    
