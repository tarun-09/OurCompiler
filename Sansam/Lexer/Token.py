T_INT = 'अंकम्'
T_FLOAT = 'चरः'
T_STRING = 'सूत्र'
T_PLUS = 'योजनम्'
T_MINUS = 'ऊन'
T_MUL = 'गुणता'
T_DIV = 'भेद'
T_MOD = 'प्रतिशत'
T_EOF = 'समन्त'
T_KEYWORD = "आरक्षितपद"
T_IDENTIFIER = "नामन्"
T_NL = 'नवीन् पङ्क्ति'
T_THEN = '~'
T_POW = '^'
T_LCURL = '{'
T_RCURL = '}'
T_LPAREN = '('
T_RPAREN = ')'
T_LSQUARE = '['
T_RSQUARE = ']'
T_EQU = "="
T_ISNEQ = '!='
T_ISEQ = '=='
T_ISG = '>'
T_ISL = '<'
T_ISGEQ = '>='
T_ISLEQ = '<='
T_NOT = '!'
T_COMMA = ','
T_SEP = ';'
T_FACT = 'T_FACT'

KEYWORDS = ['च', 'वा', 'न', 'असत्यम्', 'सत्यम्', 'यावद्', 'प्रति', 'कार्य', 'यदि', 'नोचेत्', 'चेत्',
            'अनुवर्तते', 'विघ्नः', 'यच्छ']


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f'{self.type}->{self.value}'
        return f'{self.type}'
