import Sansam.Values.Value as val
import Sansam.Values.Number as num


class String(val.Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def iter(self):
        li=[]
        for i in self.value:
            li.append(i)
        return li

    def length(self):
        counter=0
        for i in self.value:
            counter=counter+1
        return counter

    def addition(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def multiplication(self, other):
        if isinstance(other, num.Number):
            return String(self.value * other.value).set_context(self.context), None
        else:
            return None, val.Value.illegal_operation(self, other)

    def is_true(self):
        return len(self.value) > 0

    def __str__(self):
        return self.value

    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return f'"{self.value}"'