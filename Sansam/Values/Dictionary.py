import Sansam.Values.Value as val
import Sansam.Values.Number as num
import Sansam.Error.Errors as error


class Dictionary(val.Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def division(self, other):
        if isinstance(other, num.Number):
            try:
                c = 0
                for i in self.elements:
                    if c == other.value:
                        result = i
                    c = c + 1
                return result, None
            except:
                return None, error.RunTimeError(
                    other.pos_start, other.pos_end,
                    'Element at this index could not be retrieved from list because index is out of bounds',
                    self.context
                )
        else:
            return None, val.Value.illegal_operation(self, other)

    def copy(self):
        copy = Dictionary(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return str(self.elements).replace(':', '~')
