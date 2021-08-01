import Sansam.Values.Value as val


class Boolean(val.Value):
    def __init__(self, boolean):
        super().__init__()
        if boolean == 'असत्यम्':
            self.boolean = False
        elif boolean == 'सत्यम्':
            self.boolean = True
        else:
            self.boolean = boolean

    def anded_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.boolean and other.boolean).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def ored_by(self, other):
        if isinstance(other, Boolean):
            return Boolean(self.boolean or other.boolean).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def notted(self):
        return Boolean(False if self.boolean == True else True).set_context(self.context), None

    def copy(self):
        copy = Boolean(self.boolean)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.boolean != False

    def __repr__(self):
        if self.boolean:
            return str("सत्यम्")
        else:
            return str("असत्यम्")

