import Sansam.Values.Value as val
import Sansam.Values.Number as num
import Sansam.Error.Errors as error


class List(val.Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def addition(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subtraction(self, other):
        if isinstance(other, num.Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end,
                    'Element at this index could not be removed from list because index is out of bounds',
                    self.context
                )
        else:
            return None, val.Value.illegal_operation(self, other)

    def multiplication(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, val.Value.illegal_operation(self, other)

    def division(self, other):
        if isinstance(other, num.Number):
            try:
                return self.elements[other.value], None
            except:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end,
                    'Element at this index could not be retrieved from list because index is out of bounds',
                    self.context
                )
        else:
            return None, val.Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements[:])
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return ", ".join([str(x) for x in self.elements])

    def __repr__(self):
        return f'[{", ".join([str(x) for x in self.elements])}]'