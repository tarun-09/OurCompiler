class Boolean:
    def __init__(self, boolean):
        if boolean == 'असत्यम्':
            self.boolean = False
        elif boolean == 'सत्यम्':
            self.boolean = True
        else:
            self.boolean = boolean
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def anded_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.boolean and other.boolean).set_context(self.context), None

    def ored_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.boolean or other.boolean).set_context(self.context), None

    def notted(self):
        return Boolean(False if self.boolean == True else True).set_context(self.context), None

    def copy(self):
        copy = Boolean(self.boolean)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        if self.boolean:
            return str("सत्यम्")
        else:
            return str("असत्यम्")

