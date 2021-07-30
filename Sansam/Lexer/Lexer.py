import Lexer.Token as token
import Position
import Error.Errors as errors

DIGITS = '0123456789'
LETTERS = "ंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्"
LETTERS_DIGITS = LETTERS + DIGITS


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position.Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(token.Token(token.T_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(token.Token(token.T_MINUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(token.Token(token.T_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(token.Token(token.T_DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(token.Token(token.T_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '=':
                tokens.append(self.make_equals())
            elif self.current_char == '!':
                tokens.append(self.make_not_equals())
            elif self.current_char == '>':
                tokens.append(self.make_greater_than())
            elif self.current_char == '<':
                tokens.append(self.make_less_than())
            elif self.current_char == '(':
                tokens.append(token.Token(token.T_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(token.Token(token.T_RPAREN, pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], errors.IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(token.Token(token.T_EOF, pos_start=self.pos))
        return tokens, None

    def make_identifier(self):
        id_str = ''
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()

        tok_type = token.T_KEYWORD if id_str in token.KEYWORDS else token.T_IDENTIFIER
        return token.Token(tok_type, id_str, pos_start, self.pos)

    def make_number(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return token.Token(token.T_INT, int(num_str), pos_start, self.pos)
        else:
            return token.Token(token.T_FLOAT, float(num_str), pos_start, self.pos)

    def make_equals(self):
        tok_type = token.T_EQU
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = token.T_ISEQ

        return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_not_equals(self):
        tok_type = token.T_NOT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = token.T_ISNEQ

        return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_greater_than(self):
        tok_type = token.T_ISG
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = token.T_ISGEQ

        return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_less_than(self):
        tok_type = token.T_ISL
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = token.T_ISLEQ

        return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)
